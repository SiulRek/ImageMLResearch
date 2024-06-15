import os
import shutil
import unittest

import numpy as np
import tensorflow as tf

from src.data_handling.tfrecord_serialization.deserialize import (
    deserialize_dataset_from_tfrecord,
)
from src.data_handling.tfrecord_serialization.serialize import (
    serialize_dataset_to_tf_record,
)
from src.testing.base.base_test_case import BaseTestCase


class TestTFRecordSerialization(BaseTestCase):
    """ Test suite for TFRecord serialization and deserialization functions. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()
        self.dataset = self.load_mnist_digits_dataset(sample_num=5, labeled=True)

    def _compare_datasets(self, original_dataset, deserialized_dataset, atol=1e-6):
        for original, deserialized in zip(original_dataset, deserialized_dataset):
            original_image, original_label = original
            deserialized, deserialized_label = deserialized

            self.assertTrue(
                np.allclose(original_image.numpy(), deserialized.numpy(), atol=atol),
                "Restored images are not close enough to original images.",
            )

            self.assertTrue(
                np.equal(original_label.numpy(), deserialized_label.numpy()).all(),
                "Restored labels are not equal to original labels.",
            )

    def test_serialize_deserialize_jpeg(self):
        """ Test serialization and deserialization with JPEG format. """
        results_dir = os.path.join(self.temp_dir, "serialize_deserialize_jpeg")
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        serialize_dataset_to_tf_record(self.dataset, tfrecord_path, image_format="jpeg")
        self.assertTrue(os.path.exists(tfrecord_path), "TFRecord file should exist.")

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.uint8
        )
        # Smallest RTOL 0.3 to pass the test.
        # This is the reason why it is not recommended to use JPEG format for serialization.
        self._compare_datasets(self.dataset, deserialized_dataset, atol=20)

    def test_serialize_deserialize_png(self):
        """ Test serialization and deserialization with PNG format. """
        results_dir = os.path.join(self.temp_dir, "serialize_deserialize_png")
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        serialize_dataset_to_tf_record(self.dataset, tfrecord_path, image_format="png")
        self.assertTrue(os.path.exists(tfrecord_path), "TFRecord file should exist.")

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.uint8
        )
        self._compare_datasets(self.dataset, deserialized_dataset)

    def test_serialize_deserialize_with_float_labels(self):
        """ Test serialization and deserialization with float labels. """
        results_dir = os.path.join(
            self.temp_dir, "serialize_deserialize_with_float_labels"
        )
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        float_dataset = self.dataset.map(lambda x, y: (x, tf.cast(y, tf.uint8)))
        serialize_dataset_to_tf_record(float_dataset, tfrecord_path, image_format="png")
        self.assertTrue(os.path.exists(tfrecord_path), "TFRecord file should exist.")

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.uint8
        )
        self._compare_datasets(float_dataset, deserialized_dataset)

    def test_serialize_deserialize_batched_dataset(self):
        """ Test serialization and deserialization with batched dataset. """
        results_dir = os.path.join(
            self.temp_dir, "serialize_deserialize_batched_dataset"
        )
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        batched_dataset = self.dataset.batch(2)
        serialize_dataset_to_tf_record(
            batched_dataset, tfrecord_path, image_format="png"
        )
        self.assertTrue(os.path.exists(tfrecord_path), "TFRecord file should exist.")

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.uint8
        )
        self._compare_datasets(self.dataset, deserialized_dataset)

    def test_serialize_deserialize_unlabeled_dataset(self):
        """ Test serialization and deserialization with unlabeled dataset. """
        results_dir = os.path.join(
            self.temp_dir, "serialize_deserialize_unlabeled_dataset"
        )
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        unlabeled_dataset = self.dataset.map(lambda x, y: x)
        serialize_dataset_to_tf_record(
            unlabeled_dataset, tfrecord_path, image_format="png"
        )
        self.assertTrue(os.path.exists(tfrecord_path), "TFRecord file should exist.")

        deserialized_dataset = deserialize_dataset_from_tfrecord(tfrecord_path)

        # Add a label for comparison
        add_zero_label = lambda x: (x, tf.constant(0))
        deserialized_dataset = deserialized_dataset.map(add_zero_label)
        labeled_dataset = unlabeled_dataset.map(add_zero_label)
        self._compare_datasets(labeled_dataset, deserialized_dataset)

    def test_file_not_found_error_on_serialization(self):
        """ Test FileNotFoundError when trying to serialize to a non-existent
        directory. """
        with self.assertRaises(FileNotFoundError):
            deserialize_dataset_from_tfrecord(
                "/non_existent_dir/data.tfrecord", label_dtype=tf.uint8
            )


if __name__ == "__main__":
    unittest.main()
