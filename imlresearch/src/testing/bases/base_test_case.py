import os
import shutil
import sys
import unittest

import numpy as np
import tensorflow as tf

from imlresearch.src.testing.helpers.load_dataset_from_tf_records import (
    load_dataset_from_tf_records,
)
from imlresearch.src.testing.helpers.test_result_logger import TestResultLogger

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(FILE_DIR, "..", "..", "..", "..")
DATA_DIR = os.path.join(
    ROOT_DIR, "imlresearch", "src", "testing", "image_data"
)


class BaseTestCase(unittest.TestCase):
    """
    Abstract base class for test cases, providing setup and teardown
    operations common across tests.

    Attributes:
        - output_dir (str): Directory where test outputs will be saved.
        - temp_dir (str): Temporary directory for use during tests.
        - log_file (str): Path to the log file used to record test results.
        - logger (TestResultLogger): Logger instance for test outcomes.
        - remove_temp_dir (bool): Whether to remove the temp directory
          after tests.
    """

    remove_temp_dir = True

    @classmethod
    def _infere_test_file_path(cls):
        """
        Infers the file path of the test file.

        Returns:
            - str: The inferred file path.

        Raises:
            - FileNotFoundError: If the file path cannot be inferred.
        """
        module = cls.__module__
        if module in sys.modules:
            return sys.modules[module].__file__

        if len(sys.argv) > 1:
            return sys.argv[1]  # First argument is expected to be the test file

        raise FileNotFoundError("Cannot infer test file path.")

    @classmethod
    def _compute_output_dir(cls, parent_folder="tests"):
        """
        Computes the test output directory path.

        Traverses up the file hierarchy until a directory named 'tests' is
        found, then returns the path to the 'outputs' subdirectory.

        Args:
            - parent_folder (str, optional): The parent folder name.

        Returns:
            - str: The output directory path.

        Raises:
            - NotADirectoryError: If the 'tests' directory is not found.
        """
        current_dir = os.path.dirname(cls._infere_test_file_path())

        while parent_folder not in os.listdir(current_dir):
            current_dir = os.path.dirname(current_dir)
            if current_dir == os.path.dirname(current_dir):
                raise NotADirectoryError(
                    "Tests directory not found in the path hierarchy."
                )

        return os.path.join(current_dir, parent_folder, "outputs")

    @classmethod
    def _get_test_case_title(cls):
        """
        Generates a formatted test case title for logging.

        Returns:
            - str: The formatted test case title.
        """
        name = cls.__name__.removeprefix("Test")
        name = "".join(
            letter if not letter.isupper() else f" {letter}"
            for letter in name
        ).strip()
        return name.replace("_", " ").replace("  ", " ") + " Test"

    @classmethod
    def _get_test_case_folder_name(cls):
        """
        Generates a formatted test case folder name.

        Returns:
            - str: The formatted test case name.
        """
        name = cls.__name__.removeprefix("Test")
        name = "".join(
            letter if not letter.isupper() else f"_{letter.lower()}"
            for letter in name
        ).strip()
        return name.replace(" ", "").removeprefix("_") + "_test"

    @classmethod
    def setUpClass(cls):
        """
        Class-level setup: creates necessary directories and initializes logging.
        """
        cls.root_dir = os.path.normpath(ROOT_DIR)
        cls.data_dir = DATA_DIR
        cls.output_dir = cls._compute_output_dir()
        cls.results_dir = os.path.join(
            cls.output_dir, cls._get_test_case_folder_name()
        )
        cls.visualizations_dir = os.path.join(cls.output_dir, "visualizations")
        cls.temp_dir = os.path.join(cls.output_dir, "temp")

        os.makedirs(cls.output_dir, exist_ok=True)
        os.makedirs(cls.results_dir, exist_ok=True)
        os.makedirs(cls.visualizations_dir, exist_ok=True)

        cls.log_file = os.path.join(cls.output_dir, "test_results.log")
        cls.logger = TestResultLogger(cls.log_file)
        cls.logger.log_title(cls._get_test_case_title())

    @classmethod
    def tearDownClass(cls):
        """
        Class-level teardown: removes empty result directories.
        """
        for dir_ in [cls.results_dir, cls.visualizations_dir]:
            if os.path.exists(dir_) and not os.listdir(dir_):
                shutil.rmtree(dir_)

    def setUp(self):
        """
        Instance-level setup: creates a temporary directory for tests.
        """
        os.makedirs(self.temp_dir, exist_ok=True)

    def run(self, result=None):
        """
        Overrides the run method to log the test outcome.
        """
        result = super().run(result)
        self.logger.log_test_outcome(result, self._testMethodName)
        return result

    def tearDown(self):
        """
        Instance-level teardown: logs test outcome and removes the temp directory.
        """
        if os.path.exists(self.temp_dir) and self.remove_temp_dir:
            shutil.rmtree(self.temp_dir)

    @classmethod
    def load_geometrical_forms_dataset(cls):
        """
        Load the unlabeled image dataset for testing.

        Returns:
            - tf.data.Dataset: The dataset to be used for testing.
        """
        tf_records_path = os.path.join(
            cls.data_dir, "tf_records", "geometrical_forms.tfrecord"
        )
        return load_dataset_from_tf_records(tf_records_path)

    @classmethod
    def load_mnist_digits_dataset(
        cls, sample_num=None, labeled=False, binary=False
    ):
        """
        Load the MNIST digits dataset for testing.

        Args:
            - sample_num (int, optional): Number of samples to load.
            - labeled (bool, optional): Whether to return dataset with labels.
            - binary (bool, optional): Whether labels should be in binary format.

        Returns:
            - tf.data.Dataset: The MNIST digits dataset.
        """
        dataset = tf.keras.datasets.mnist.load_data()
        (X_train, Y_train), (X_test, Y_test) = dataset

        X = np.concatenate([X_train, X_test], axis=0)
        Y = np.concatenate([Y_train, Y_test], axis=0)
        X = np.stack([X] * 3, axis=-1)  # Convert grayscale to 3-channel

        if binary:
            mask = (Y == 0) | (Y == 1)
            X, Y = X[mask], Y[mask]

        if sample_num and sample_num < len(X):
            X, Y = X[:sample_num], Y[:sample_num]

        if labeled:
            Y = tf.one_hot(Y, 10) if not binary else Y
            return tf.data.Dataset.from_tensor_slices((X, Y))

        return tf.data.Dataset.from_tensor_slices(X)

    @classmethod
    def load_mnist_digits_dicts(cls):
        """
        Load the MNIST digits dataset as dictionaries with JPG and PNG formats.

        Returns:
            - tuple: Two dictionaries containing file paths and labels.
        """
        dataset_dir = os.path.join(cls.data_dir, "mnist_digits")
        jpg_dict, png_dict = {"path": [], "label": []}, {"path": [], "label": []}

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
    mnist_digits_dataset = BaseTestCase.load_mnist_digits_dataset()
    print(mnist_digits_dataset)
