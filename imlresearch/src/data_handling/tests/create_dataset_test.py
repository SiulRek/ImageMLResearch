import unittest

import numpy as np
import tensorflow as tf

from imlresearch.src.data_handling.io.create_dataset import create_dataset
from imlresearch.src.testing.bases.base_test_case import BaseTestCase

try:
    import pandas as pd

    pandas_installed = True
except ImportError:
    pandas_installed = False


class TestCreateDataset(BaseTestCase):
    """
    Test suite for the `create_dataset` function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by loading sample data.
        """
        super().setUpClass()
        cls.jpg_dict, cls.png_dict = cls.load_mnist_digits_dicts()

    def setUp(self):
        """
        Sets up each test by defining class names.
        """
        super().setUp()
        self.class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def _normalize_label(self, label):
        """
        Normalizes a label to a predefined format.

        Parameters
        ----------
        label : str, list, or tf.Tensor
            The label to normalize.

        Returns
        -------
        int
            The normalized label.
        """
        if isinstance(label, str):
            return int(label)
        if isinstance(label, list):
            return label.index(1)
        if isinstance(label, tf.Tensor):
            if label.shape[-1] == len(self.class_names):
                return tf.argmax(label).numpy()
            return label.numpy()
        msg = f"Invalid label type: {type(label)}"
        raise ValueError(msg)

    def _expected_one_hot_label(self, label):
        """
        Generates the expected one-hot encoding for a given label.

        Parameters
        ----------
        label : int
            The class label.

        Returns
        -------
        np.array
            A one-hot encoded representation of the label.
        """
        one_hot_label = np.zeros(len(self.class_names))
        one_hot_label[int(label)] = 1
        return one_hot_label

    def _assert_label(self, label, expected_label):
        """
        Checks if the given label matches the expected label.

        Parameters
        ----------
        label : str, list, or tf.Tensor
            The label to check.
        expected_label : str, list, or tf.Tensor
            The expected label.
        """
        label = self._normalize_label(label)
        expected_label = self._normalize_label(expected_label)
        self.assertEqual(
            label, expected_label, f"Label mismatch {label} != {expected_label}"
        )

    def test_create_dataset_from_dicts_jpg(self):
        """
        Tests `create_dataset` with a dictionary containing JPG images.
        """
        data = self.jpg_dict
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            self._assert_label(label, data["label"][i])

    def test_create_dataset_from_dicts_png(self):
        """
        Tests `create_dataset` with a dictionary containing PNG images.
        """
        data = self.png_dict
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            self._assert_label(label, data["label"][i])

    @unittest.skipUnless(pandas_installed, "Pandas is not installed.")
    def test_create_dataset_from_dataframe_jpg(self):
        """
        Tests `create_dataset` with a pandas DataFrame containing JPG images.
        """
        data = pd.DataFrame(self.jpg_dict)
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            self._assert_label(label, self.jpg_dict["label"][i])

    @unittest.skipUnless(pandas_installed, "Pandas is not installed.")
    def test_create_dataset_from_dataframe_png(self):
        """
        Tests `create_dataset` with a pandas DataFrame containing PNG images.
        """
        data = pd.DataFrame(self.png_dict)
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            self._assert_label(label, self.png_dict["label"][i])

    def test_dataset_from_dicts(self):
        """
        Tests dataset creation from a list of dictionaries.
        """
        data = [
            {"path": self.png_dict["path"][0],
             "label": self.png_dict["label"][0]},
            {"path": self.jpg_dict["path"][1],
             "label": self.jpg_dict["label"][1]},
        ]
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            self._assert_label(label, data[i]["label"])

    @unittest.skipUnless(pandas_installed, "Pandas is not installed.")
    def test_one_hot_encoding(self):
        """
        Tests that one-hot encoding is applied correctly to class labels.
        """
        data = pd.DataFrame(self.jpg_dict)
        dataset = create_dataset(data, "multi_class", self.class_names)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for i, (image, label) in enumerate(dataset):
            self.assertIsInstance(image, tf.Tensor)
            self.assertIsInstance(label, tf.Tensor)
            expected_label = self._expected_one_hot_label(
                self.jpg_dict["label"][i]
            )
            self.assertTrue(np.array_equal(label.numpy(), expected_label))

    @unittest.skipUnless(pandas_installed, "Pandas is not installed.")
    def test_no_label(self):
        """
        Tests dataset creation without labels.
        """
        data = pd.DataFrame(self.jpg_dict)
        dataset = create_dataset(data)
        self.assertIsInstance(dataset, tf.data.Dataset)
        for image in dataset:
            self.assertIsInstance(image, tf.Tensor)

    def test_invalid_data_type(self):
        """
        Tests that `ValueError` is raised for invalid data types.
        """
        data = "invalid_data_type"
        with self.assertRaises(ValueError):
            create_dataset(data, "multi_class", self.class_names)


if __name__ == "__main__":
    unittest.main()
