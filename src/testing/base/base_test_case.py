import os
import shutil
import sys
import unittest

import numpy as np
import tensorflow as tf

from src.testing.helpers.load_dataset_from_tf_records import (
    load_dataset_from_tf_records,
)
from src.testing.helpers.test_result_logger import TestResultLogger

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(FILE_DIR, "..", "..", "..")
DATA_DIR = os.path.join(ROOT_DIR, "src", "testing", "image_data")


class BaseTestCase(unittest.TestCase):
    """
    Abstract base class for all test cases, providing setup and teardown
    operations that are common across various tests. This class ensures that all
    derived test classes are prepared with necessary directories and logging
    capabilities.

    Attributes:
        - output_dir (str): Directory where test outputs will be saved.
        - temp_dir (str): Temporary directory for use during tests.
        - log_file (str): Path to the log file used to record test results.
        - logger (TestResultLogger): Logger instance to log test outcomes.
        - remove_temp_dir (bool): Indicates whether the temp directory
            should be removed after tests.
    """

    remove_temp_dir = True

    @classmethod
    def _infere_test_file_path(cls):
        # 1. Attempt: infer file path from sys.modules
        module = cls.__module__
        if module in sys.modules:
            return sys.modules[module].__file__
        # 2. Attempt: infer file path from sys.argv, for the case called from Command Line
        if len(sys.argv) > 1:
            # 1st arg expected is the executor file
            # 2nd arg expected is the actual test file
            return sys.argv[1]
        msg = "Cannot infer test file path."
        raise FileNotFoundError(msg)

    @classmethod
    def _compute_output_dir(cls, parent_folder="tests"):
        """
        Computes the directory path for test outputs by traversing up the file
        hierarchy until a directory named 'tests' is found. It then returns the
        path to the 'outputs' subdirectory within 'tests'.

        Args:
            - parent_folder (str, optional): The name of the parent folder
                containing the 'tests' directory.

        Returns:
            - str: The path to the output directory.
        """
        current_dir = os.path.dirname(cls._infere_test_file_path())

        while parent_folder not in os.listdir(current_dir):
            current_dir = os.path.dirname(current_dir)
            if current_dir == os.path.dirname(current_dir):
                msg = "Tests directory not found in the path hierarchy."
                raise NotADirectoryError(msg)

        return os.path.join(current_dir, parent_folder, "outputs")

    @classmethod
    def _get_test_case_title(cls):
        """
        Generates a formatted test case name to be used as the title in the log.

        Returns:
            - str: The formatted test case name.
        """
        name = cls.__name__
        if name.startswith("Test"):
            name = name[4:]
        name = [letter if not letter.isupper() else f" {letter}" for letter in name]
        name = "".join(name).strip()
        name = name.replace("_", " ")
        name = name.replace("  ", " ")
        return name.strip() + " Test"

    @classmethod
    def _get_test_case_folder_name(cls):
        """
        Generates a formatted test case name to be used as the folder name.

        Returns:
            - str: The formatted test case name.
        """
        name = cls.__name__
        if name.startswith("Test"):
            name = name[4:]
        name = [
            letter if not letter.isupper() else f"_{letter.lower()}" for letter in name
        ]
        name = "".join(name).strip()
        name = name.replace(" ", "")
        if name.startswith("_"):
            name = name[1:]
        return name + "_test"

    @classmethod
    def setUpClass(cls):
        """ Class-level setup method that ensures necessary directories are created
        and initializes logging for the test case. """
        cls.root_dir = ROOT_DIR
        cls.root_dir = os.path.normpath(cls.root_dir)
        cls.data_dir = DATA_DIR
        cls.output_dir = cls._compute_output_dir()
        cls.results_dir = os.path.join(cls.output_dir, cls._get_test_case_folder_name())
        cls.visualizations_dir = os.path.join(cls.output_dir, "visualizations")
        cls.temp_dir = os.path.join(cls.output_dir, "temp")

        os.makedirs(cls.output_dir, exist_ok=True)
        os.makedirs(cls.results_dir, exist_ok=True)
        os.makedirs(cls.visualizations_dir, exist_ok=True)

        cls.log_file = os.path.join(cls.output_dir, "test_results.log")
        cls.logger = TestResultLogger(cls.log_file, cls._get_test_case_title())

    @classmethod
    def tearDownClass(cls):
        """ Class-level teardown method that removes the results directory if it is
        empy. """
        for dir_ in [cls.results_dir, cls.visualizations_dir]:
            if os.path.exists(dir_) and os.listdir(dir_) == []:
                shutil.rmtree(dir_)

    def setUp(self):
        """ Instance-level setup method that creates a temporary directory for use
        during the test. """
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        """ Instance-level teardown method that logs the outcome of each test method
        and removes the temporary directory created during the test setup. """
        self.logger.log_test_outcome(self._outcome.result, self._testMethodName)
        if os.path.exists(self.temp_dir) and self.remove_temp_dir:
            shutil.rmtree(self.temp_dir)

    @classmethod
    def load_geometrical_forms_dataset(cls):
        """
        Load the image dataset used for testing. The dataset is unlabeled!

        Returns:
            - tf.data.Dataset: The image dataset to be used for testing.
        """
        tf_records_path = os.path.join(
            cls.data_dir, "tf_records", "geometrical_forms.tfrecord"
        )
        return load_dataset_from_tf_records(tf_records_path)

    @classmethod
    def load_mnist_digits_dataset(cls, sample_num=5, labeled=False):
        """
        Load the MNIST digits dataset used for testing. This method is intended
        to be overridden by derived test classes to return the appropriate
        dataset.

        Returns:
            - tf.data.Dataset: The MNIST digits dataset to be used for
                testing.
        """
        dataset = tf.keras.datasets.mnist.load_data()

        (X_train, Y_train), _ = dataset
        X_train = np.stack([X_train] * 3, axis=-1)
        if sample_num:
            X_train = X_train[:sample_num]
            Y_train = Y_train[:sample_num]
        if labeled:
            return tf.data.Dataset.from_tensor_slices((X_train, Y_train))
        return tf.data.Dataset.from_tensor_slices(X_train)

    @classmethod
    def load_mnist_digits_dicts(cls):
        """
        Load the mnist digits dataset as dictionaries. This method loads the
        dataset and returns it as two separate dictionaries for images in JPG
        and PNG formats.

        Returns:
            - tuple: A tuple containing two dictionaries, one for JPG images
                and one for PNG images. Each dictionary contains 'path' and
                'label' keys.
        """
        dataset_dir = os.path.join(cls.data_dir, "mnist_digits")
        jpg_dict = {"path": [], "label": []}
        png_dict = {"path": [], "label": []}
        for file in os.listdir(dataset_dir):
            label = file.split(".")[0].split("_")[-1]
            file_path = os.path.join(dataset_dir, file)
            if file.endswith(".jpg"):
                jpg_dict["path"].append(file_path)
                jpg_dict["label"].append(label)
            elif file.endswith(".png"):
                png_dict["path"].append(file_path)
                png_dict["label"].append(label)

        return jpg_dict, png_dict


if __name__ == "__main__":
    # load the mnist digits dataset
    mnist_digits_dataset = BaseTestCase.load_mnist_digits_dataset()
    print(mnist_digits_dataset)
