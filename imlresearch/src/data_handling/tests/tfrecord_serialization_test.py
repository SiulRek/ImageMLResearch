import os
import shutil
import unittest

import numpy as np
import tensorflow as tf

from imlresearch.src.data_handling.tfrecord_serialization.deserialize import (
    deserialize_dataset_from_tfrecord,
)
from imlresearch.src.data_handling.tfrecord_serialization.serialize import (
    serialize_dataset_to_tf_record,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestTFRecordSerialization(BaseTestCase):
    """
    Test suite for TFRecord serialization and deserialization functions.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class.
        """
        super().setUpClass()

    def setUp(self):
        """
        Sets up each test by loading a sample labeled dataset.
        """
        super().setUp()
        self.dataset = self.load_mnist_digits_dataset(
            sample_num=5, labeled=True
        )

    def _compare_datasets(
        self, original_dataset, deserialized_dataset, atol=1e-6
    ):
        """
        Compares two datasets to ensure their contents are nearly identical.

        Parameters
        ----------
        original_dataset : tf.data.Dataset
            The original dataset.
        deserialized_dataset : tf.data.Dataset
            The dataset after serialization and deserialization.
        atol : float, optional
            Absolute tolerance for numerical comparisons.
        """
        zip_datasets = zip(original_dataset, deserialized_dataset)
        for original, deserialized in zip_datasets:
            original_image, original_label = original
            deserialized_image, deserialized_label = deserialized

            self.assertTrue(
                np.allclose(
                    original_image.numpy(), deserialized_image.numpy(),
                    atol=atol
                ),
                "Restored images are not close enough to original images.",
            )

            self.assertTrue(
                np.equal(
                    original_label.numpy(), deserialized_label.numpy()
                ).all(),
                "Restored labels are not equal to original labels.",
            )

    def test_serialize_deserialize_jpeg(self):
        """
        Tests serialization and deserialization with JPEG format.
        """
        results_dir = os.path.join(self.temp_dir, "serialize_deserialize_jpeg")
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        serialize_dataset_to_tf_record(
            self.dataset, tfrecord_path, image_format="jpeg"
        )
        self.assertTrue(
            os.path.exists(tfrecord_path), "TFRecord file should exist."
        )

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.float32
        )
        # Smallest ATOL 20 to pass the test due to JPEG compression artifacts.
        self._compare_datasets(self.dataset, deserialized_dataset, atol=20)

    def test_serialize_deserialize_png(self):
        """
        Tests serialization and deserialization with PNG format.
        """
        results_dir = os.path.join(self.temp_dir, "serialize_deserialize_png")
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        serialize_dataset_to_tf_record(
            self.dataset, tfrecord_path, image_format="png"
        )
        self.assertTrue(
            os.path.exists(tfrecord_path), "TFRecord file should exist."
        )

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.float32
        )
        self._compare_datasets(self.dataset, deserialized_dataset)

    def test_serialize_deserialize_with_uint8_labels(self):
        """
        Tests serialization and deserialization with unsigned uint8 labels.
        """
        results_dir = os.path.join(
            self.temp_dir, "serialize_deserialize_with_uint8_labels"
        )
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        tfrecord_path = os.path.join(results_dir, "data.tfrecord")

        uint_dataset = self.dataset.map(lambda x, y: (x, tf.cast(y, tf.uint8)))
        serialize_dataset_to_tf_record(
            uint_dataset, tfrecord_path, image_format="png"
        )
        self.assertTrue(
            os.path.exists(tfrecord_path), "TFRecord file should exist."
        )

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.uint8
        )
        self._compare_datasets(uint_dataset, deserialized_dataset)

    def test_serialize_deserialize_batched_dataset(self):
        """
        Tests serialization and deserialization with a batched dataset.
        """
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
        self.assertTrue(
            os.path.exists(tfrecord_path), "TFRecord file should exist."
        )

        deserialized_dataset = deserialize_dataset_from_tfrecord(
            tfrecord_path, label_dtype=tf.float32
        )
        self._compare_datasets(self.dataset, deserialized_dataset)

    def test_serialize_deserialize_unlabeled_dataset(self):
        """
        Tests serialization and deserialization with an unlabeled dataset.
        """
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
        self.assertTrue(
            os.path.exists(tfrecord_path), "TFRecord file should exist."
        )

        deserialized_dataset = deserialize_dataset_from_tfrecord(tfrecord_path)

        # Add a dummy label for comparison
        def add_zero_label(x):
            return x, tf.constant(0)

        deserialized_dataset = deserialized_dataset.map(add_zero_label)
        labeled_dataset = unlabeled_dataset.map(add_zero_label)
        self._compare_datasets(labeled_dataset, deserialized_dataset)

    def test_file_not_found_error_on_serialization(self):
        """
        Tests that `FileNotFoundError` is raised when trying to deserialize
        from a non-existent file.
        """
        with self.assertRaises(FileNotFoundError):
            deserialize_dataset_from_tfrecord(
                "/non_existent_dir/data.tfrecord", label_dtype=tf.float32
            )


if __name__ == "__main__":
    unittest.main()
