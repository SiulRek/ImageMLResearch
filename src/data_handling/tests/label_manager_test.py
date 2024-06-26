import unittest

import tensorflow as tf

from src.data_handling.labelling.label_manager import LabelManager
from src.testing.base.base_test_case import BaseTestCase


class TestLabelManager(BaseTestCase):
    """ Test suite for the LabelManager class. """

    def setUp(self):
        super().setUp()
        self.binary_label = 1
        self.invalid_binary_label = 2
        self.multi_class_label = 2
        self.invalid_label_key = {"wrong_key": 3}

    def test_binary_labels_valid_input(self):
        manager = LabelManager("binary")
        result = manager.encode_label(self.binary_label)
        expected = tf.constant(1, dtype=tf.float32)
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
            "The binary labels do not match expected output.",
        )

    def test_binary_labels_invalid_value(self):
        manager = LabelManager("binary")
        with self.assertRaises(ValueError):
            manager.encode_label(self.invalid_binary_label)

    def test_multi_class_labels_valid_input(self):
        manager = LabelManager("multi_class", category_names=["a", "b", "c", "d"])
        result = manager.encode_label(self.multi_class_label)
        expected = tf.constant([0, 0, 1, 0], dtype=tf.float32)
        self.assertTrue(
            tf.reduce_all(tf.equal(result, expected)),
            "The multi_class labels do not match expected output.",
        )

    def test_multi_label_not_implemented(self):
        manager = LabelManager("multi_label")
        with self.assertRaises(NotImplementedError):
            manager.encode_label(self.multi_class_label)

    def test_multi_class_multi_label_not_implemented(self):
        manager = LabelManager("multi_class_multi_label")
        with self.assertRaises(NotImplementedError):
            manager.encode_label(self.multi_class_label)

    def test_object_detection_labels_not_implemented(self):
        manager = LabelManager("object_detection")
        with self.assertRaises(NotImplementedError):
            manager.encode_label(self.multi_class_label)

    def test_label_dtype(self):
        manager = LabelManager("multi_class", category_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
            "Label dtype for multi_class should be tf.float32",
        )

        manager = LabelManager("object_detection")
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
            "Label dtype for object_detection should be tf.float32",
        )

        manager = LabelManager("binary")
        self.assertEqual(
            manager.label_dtype,
            tf.float32,
            "Label dtype for binary should be tf.float32",
        )

    def test_label_conversion_dtype(self):
        manager = LabelManager("multi_class", category_names=["a", "b", "c", "d"])
        result = manager.encode_label(self.multi_class_label)
        self.assertEqual(
            result.dtype,
            tf.float32,
            "The dtype of the encoded multi_class label should be tf.float32",
        )

        manager = LabelManager(
            "multi_class", category_names=["a", "b", "c", "d"], dtype=tf.int32
        )
        result = manager.encode_label(self.multi_class_label)
        self.assertEqual(
            result.dtype,
            tf.int32,
            "The dtype of the encoded multi_class label should be tf.int32",
        )

        manager = LabelManager("binary", category_names=["a", "b"])
        result = manager.encode_label(self.binary_label)
        self.assertEqual(
            result.dtype,
            tf.float32,
            "The dtype of the encoded binary label should be tf.float32",
        )

        manager = LabelManager("binary", dtype=tf.int32)
        result = manager.encode_label(self.binary_label)
        self.assertEqual(
            result.dtype,
            tf.int32,
            "The dtype of the encoded binary label should be tf.int32",
        )

        manager = LabelManager("object_detection")
        with self.assertRaises(NotImplementedError):
            manager.encode_label(self.multi_class_label)

    def test_get_index(self):
        manager = LabelManager("multi_class", category_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.get_index("c"),
            2,
            "Conversion to numeric failed for valid string label.",
        )
        with self.assertRaises(ValueError):
            manager.get_index("e")

    def test_get_category(self):
        manager = LabelManager("multi_class", category_names=["a", "b", "c", "d"])
        self.assertEqual(
            manager.get_category(2),
            "c",
            "Decoding failed for valid numeric label.",
        )
        self.assertEqual(
            manager.get_category(tf.constant(2)),
            "c",
            "Decoding failed for valid tensor label.",
        )
        with self.assertRaises(ValueError):
            manager.get_category(5)
        with self.assertRaises(ValueError):
            manager.get_category("c")


if __name__ == "__main__":
    unittest.main()
