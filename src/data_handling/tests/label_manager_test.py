import unittest

import tensorflow as tf

from src.data_handling.labelling.label_manager import LabelManager
from src.testing.base.base_test_case import BaseTestCase


class TestLabelManager(BaseTestCase):
    """ Test suite for the LabelManager class. """

    def test_binary_labels_valid_input(self):
        manager = LabelManager("binary")
        expected = tf.constant(1, dtype=tf.float32)

        # String input
        result = manager.encode_label("1")
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
            "The binary labels do not match expected output.",
        )

        # Integer input
        result = manager.encode_label(1)
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
            "The binary labels do not match expected output.",
        )

    def test_binary_labels_invalid_value(self):
        manager = LabelManager("binary")
        with self.assertRaises(ValueError):
            manager.encode_label(2)

    def test_multi_class_labels_valid_input(self):
        manager = LabelManager("multi_class", class_names=["a", "b", "c", "d"])
        expected = tf.constant([0, 0, 1, 0], dtype=tf.float32)

        # String input
        result = manager.encode_label("c")
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
        )

        # Integer input
        result = manager.encode_label(2)
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
        )

    def test_multi_label_not_implemented(self):
        manager = LabelManager("multi_label")
        with self.assertRaises(NotImplementedError):
            manager.encode_label("c")

    def test_multi_class_multi_label_not_implemented(self):
        manager = LabelManager("multi_class_multi_label")
        with self.assertRaises(NotImplementedError):
            manager.encode_label("c")

    def test_object_detection_labels_not_implemented(self):
        manager = LabelManager("object_detection")
        with self.assertRaises(NotImplementedError):
            manager.encode_label("c")

    def test_default_dtype(self):
        manager = LabelManager("multi_class", class_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
        )

        manager = LabelManager("object_detection")
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
        )

        manager = LabelManager("binary")
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
        )

    def test_label_conversion_dtype(self):
        manager = LabelManager("multi_class", class_names=["a", "b", "c", "d"])
        result = manager.encode_label("c")
        self.assertEqual(
            result.dtype,
            tf.float32,
        )

        manager = LabelManager(
            "multi_class", class_names=["a", "b", "c", "d"], dtype=tf.int32
        )
        result = manager.encode_label("c")
        self.assertEqual(
            result.dtype,
            tf.int32,
        )

        manager = LabelManager("binary", class_names=["a", "b"])
        result = manager.encode_label(1)
        self.assertEqual(
            result.dtype,
            tf.float32,
        )

        manager = LabelManager("binary", dtype=tf.int32)
        result = manager.encode_label(1)
        self.assertEqual(
            result.dtype,
            tf.int32,
        )

        manager = LabelManager("object_detection")
        with self.assertRaises(NotImplementedError):
            manager.encode_label("c")

    def test_get_index(self):
        manager = LabelManager("multi_class", class_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.get_index("c"),
            2,
        )
        with self.assertRaises(ValueError):
            manager.get_index("e")

    def test_get_class(self):
        manager = LabelManager("multi_class", class_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.get_class(2),
            "c",
        )
        self.assertEqual(
            manager.get_class(tf.constant(2)),
            "c",
        )
        with self.assertRaises(ValueError):
            manager.get_class(5)
        with self.assertRaises(ValueError):
            manager.get_class("c")


if __name__ == "__main__":
    unittest.main()
