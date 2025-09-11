import unittest

import numpy as np
import tensorflow as tf

from imlresearch.src.research.helpers.data_retriever import DataRetriever
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestDataRetriever(BaseTestCase):
    """
    Test suite for the DataRetriever class.
    """

    def setUp(self):
        """
        Set up the test environment for DataRetriever.

        This initializes a DataRetriever instance and creates mock datasets
        and outputs for testing.
        """
        super().setUp()
        self.data_retriever = DataRetriever()

        # Create some mock data
        self.y_true = np.array([0, 1, 1, 0], dtype=np.int32)
        self.y_pred = np.array([0, 1, 0, 0], dtype=np.int32)
        self.dataset = tf.data.Dataset.from_tensor_slices(
            (self.y_true, self.y_pred)
        ).batch(2)

        self.data_retriever._datasets_container = {
            "complete_dataset": self.dataset
        }
        self.data_retriever._outputs_container = {
            "complete_output": (self.y_true, self.y_pred)
        }

    def test_to_numpy_array(self):
        """
        Test conversion of various data types to NumPy arrays.
        """
        tensor = tf.constant([1, 2, 3])
        numpy_array = np.array([1, 2, 3])

        # Test with tensor
        result = self.data_retriever._to_numpy_array(tensor)
        self.assertTrue(np.array_equal(result, numpy_array))

        # Test with numpy array
        result = self.data_retriever._to_numpy_array(numpy_array)
        self.assertTrue(np.array_equal(result, numpy_array))

        # Test with list
        result = self.data_retriever._to_numpy_array([1, 2, 3])
        self.assertTrue(np.array_equal(result, numpy_array))

    def test_retrieve_class_names(self):
        """
        Test retrieval of class names from the label manager.

        This test expects an AttributeError since no label manager
        is initialized.
        """
        with self.assertRaises(AttributeError):
            self.data_retriever._retrieve_class_names()

    def test_retrieve_test_output_data(self):
        """
        Test retrieval of output data for the test dataset.
        """
        y_true, y_pred = self.data_retriever._retrieve_test_output_data()
        self.assertTrue(np.array_equal(y_true, self.y_true))
        self.assertTrue(np.array_equal(y_pred, self.y_pred))

        with self.assertRaises(ValueError):
            self.data_retriever._outputs_container = {}
            self.data_retriever._retrieve_test_output_data()

    def test_retrieve_output_data_by_name(self):
        """
        Test retrieval of output data by its name.
        """
        y_true, y_pred = self.data_retriever._retrieve_output_data_by_name(
            "complete_output"
        )
        self.assertTrue(np.array_equal(y_true, self.y_true))
        self.assertTrue(np.array_equal(y_pred, self.y_pred))

        with self.assertRaises(ValueError):
            self.data_retriever._retrieve_output_data_by_name(
                "invalid_output_name"
            )

    def test_retrieve_input_data_by_name(self):
        """
        Test retrieval of input data from the dataset.
        """
        x = self.data_retriever._retrieve_input_data_by_name(
            "complete_dataset"
        )
        expected_tensor = tf.constant([[0, 1], [1, 0]], dtype=tf.int32)

        self.assertTrue(tf.reduce_all(tf.equal(x, expected_tensor)))

        with self.assertRaises(ValueError):
            self.data_retriever._retrieve_input_data_by_name(
                "invalid_dataset_name"
            )

    def test_retrieve_test_input_output_data(self):
        """
        Test retrieval of input and output data for the test dataset.
        """
        x, y_true, y_pred = self.data_retriever._retrieve_test_input_output_data()  # noqa
        expected_tensor = tf.constant([[0, 1], [1, 0]], dtype=tf.int32)

        self.assertTrue(tf.reduce_all(tf.equal(x, expected_tensor)))
        self.assertTrue(np.array_equal(y_true, self.y_true))
        self.assertTrue(np.array_equal(y_pred, self.y_pred))

        with self.assertRaises(ValueError):
            self.data_retriever._datasets_container = {}
            self.data_retriever._retrieve_test_input_output_data()


if __name__ == "__main__":
    unittest.main()
