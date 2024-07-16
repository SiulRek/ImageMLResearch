import unittest

import numpy as np
import tensorflow as tf

from src.research.helpers.data_retriever import DataRetriever
from src.testing.base.base_test_case import BaseTestCase


class TestDataRetriever(BaseTestCase):
    """ Test suite for the DataRetriever class. """

    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.data_retriever = DataRetriever()

        # Create some mock data
        cls.y_true = np.array([0, 1, 1, 0])
        cls.y_pred = np.array([0, 1, 0, 0])
        cls.dataset = tf.data.Dataset.from_tensor_slices(
            (cls.y_true, cls.y_pred)
        ).batch(2)

        cls.data_retriever._datasets_container = {"complete_dataset": cls.dataset}
        cls.data_retriever._outputs_container = {
            "complete_output": (cls.y_true, cls.y_pred)
        }

    def test_to_numpy_array(self):
        """ Test conversion to numpy array. """
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

    def test_retrieve_output_data(self):
        """ Test retrieval of output data. """
        y_true, y_pred, class_names = self.data_retriever._retrieve_output_data()
        self.assertTrue(np.array_equal(y_true, self.y_true))
        self.assertTrue(np.array_equal(y_pred, self.y_pred))
        self.assertIsNone(class_names)

        with self.assertRaises(ValueError):
            self.data_retriever._outputs_container = {}
            self.data_retriever._retrieve_output_data()

    def test_retrieve_input_data_by_name(self):
        """ Test retrieval of input data by name. """
        x = self.data_retriever._retrieve_input_data_by_name("complete_dataset")
        expected_tensor = tf.constant([[0, 1], [1, 0]], dtype=tf.int64)

        self.assertTrue(tf.reduce_all(tf.equal(x, expected_tensor)))

        with self.assertRaises(ValueError):
            self.data_retriever._datasets_container = {}
            self.data_retriever._retrieve_input_data_by_name("complete_dataset")

    def test_retrieve_input_output_data(self):
        """ Test retrieval of input and output data for plotting. """
        x, y_true, y_pred, class_names = (
            self.data_retriever._retrieve_input_output_data()
        )
        expected_tensor = tf.constant([[0, 1], [1, 0]], dtype=tf.int64)

        self.assertTrue(tf.reduce_all(tf.equal(x, expected_tensor)))
        self.assertTrue(np.array_equal(y_true, self.y_true))
        self.assertTrue(np.array_equal(y_pred, self.y_pred))
        self.assertIsNone(class_names)

        with self.assertRaises(ValueError):
            self.data_retriever._datasets_container = {}
            self.data_retriever._retrieve_input_output_data()


if __name__ == "__main__":
    unittest.main()
