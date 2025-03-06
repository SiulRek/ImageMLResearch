import os
import unittest

import tensorflow as tf

from imlresearch.src.data_handling.data_handler import DataHandler
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestDataHandler(BaseTestCase):
    """
    Test suite for the `DataHandler` class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by loading test data and initializing
        the `DataHandler` instance.
        """
        super().setUpClass()
        cls.jpg_dict, cls.png_dict = cls.load_mnist_digits_dicts()
        research_attributes = ResearchAttributes(
            label_type="multi_class",
            class_names=[str(i) for i in range(10)],
        )
        cls.data_handler = DataHandler()
        cls.data_handler.synchronize_research_attributes(research_attributes)

    def _assert_dataset(self, dataset):
        """
        Asserts that the dataset is of type `tf.data.Dataset` and that the
        images and labels have the correct shapes.

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset to check.
        """
        self.assertIsInstance(
            dataset, tf.data.Dataset,
            "Dataset is not of type `tf.data.Dataset`."
        )
        for image, label in dataset.take(1):
            self.assertIn(image.shape, [(28, 28, 1), (28, 28, 3)])
            self.assertEqual(label.shape, (10,))

    def _create_dataset(self, image_shape, label_shape=None):
        """
        Creates a dataset with random images and labels.

        Parameters
        ----------
        image_shape : tuple
            Shape of the image data.
        label_shape : tuple, optional
            Shape of the label data.

        Returns
        -------
        tf.data.Dataset
            A TensorFlow dataset with random images and labels.
        """
        images = tf.random.normal(image_shape)
        if label_shape is None:
            return tf.data.Dataset.from_tensor_slices(images)
        labels = tf.random.normal(label_shape)
        return tf.data.Dataset.from_tensor_slices((images, labels))

    def test_assert_dataset_format_passes(self):
        """
        Tests that the `_assert_dataset_format` method passes for valid dataset
        formats.
        """
        shapes_parameters = [
            ((10, 28, 28, 1), (10,)),
            ((10, 28, 28, 3), (10,)),
            ((10, 28, 28, 1), (10, 10)),
            ((10, 28, 28, 3), (10, 10)),
        ]
        for image_shape, label_shape in shapes_parameters:
            with self.subTest(
                image_shape=image_shape, label_shape=label_shape
            ):
                dataset = self._create_dataset(image_shape, label_shape)
                self.data_handler._assert_dataset_format(dataset)

    def test_assert_dataset_format_fails(self):
        """
        Tests that the `_assert_dataset_format` method fails for invalid dataset
        formats.
        """
        shapes_parameters = [
            ((10, 28, 28, 2), (10,)),
            ((10, 28, 28, 28, 3), (10,)),
            ((10, 10, 1), (10, 10)),
        ]
        for image_shape, label_shape in shapes_parameters:
            with self.subTest(
                image_shape=image_shape, label_shape=label_shape
            ):
                dataset = self._create_dataset(image_shape, label_shape)
                with self.assertRaises(ValueError):
                    self.data_handler._assert_dataset_format(dataset)

    def test_load_dataset_from_dict(self):
        """
        Tests dataset creation from a dictionary and storage in the dataset
        container.
        """
        self.data_handler.load_dataset(self.jpg_dict)
        self.assertIn(
            "complete_dataset", self.data_handler.datasets_container
        )
        dataset = self.data_handler.datasets_container["complete_dataset"]
        self.assertIsInstance(dataset, tf.data.Dataset)
        self._assert_dataset(dataset)

    def test_load_dataset_from_tf_dataset(self):
        """
        Tests loading a dataset from a TensorFlow `Dataset`.
        """
        images = tf.random.normal((10, 28, 28, 1))
        labels = tf.constant([i for i in range(10)])
        labels = tf.one_hot(labels, 10)
        dataset = tf.data.Dataset.from_tensor_slices((images, labels))

        self.data_handler.load_dataset(dataset)
        self.assertIn(
            "complete_dataset", self.data_handler._datasets_container
        )
        dataset = self.data_handler.datasets_container["complete_dataset"]
        self._assert_dataset(dataset)

    def test_enhance_dataset(self):
        """
        Tests enhancement of the dataset and updating it in the container.
        """
        self.data_handler.load_dataset(self.jpg_dict)
        original_dataset = list(
            self.data_handler.datasets_container["complete_dataset"]
        )
        self.data_handler.prepare_datasets(batch_size=2, shuffle_seed=42)
        self.assertIn(
            "complete_dataset", self.data_handler.datasets_container
        )
        enhanced_dataset = self.data_handler.datasets_container[
            "complete_dataset"
        ]

        for batch in enhanced_dataset:
            self.assertEqual(batch[0].shape[0], 2)
            break

        enhanced_dataset_unbatched = enhanced_dataset.unbatch()
        self._assert_dataset(enhanced_dataset_unbatched)
        for original, enhanced in zip(
            original_dataset, enhanced_dataset_unbatched
        ):
            if not tf.reduce_all(tf.equal(original[0], enhanced[0])):
                break
        else:
            self.fail(
                "All tensors are equal after enhancement, "
                "indicating no shuffling occurred."
            )

    def test_split_dataset(self):
        """
        Tests splitting the dataset and storing the resulting splits.
        """
        self.data_handler.load_dataset(self.jpg_dict)
        self.data_handler.split_dataset(
            train_split=0.6, val_split=0.2, test_split=0.2
        )
        self.assertIn("train_dataset", self.data_handler.datasets_container)
        self.assertIn("val_dataset", self.data_handler.datasets_container)
        self.assertIn("test_dataset", self.data_handler.datasets_container)
        self.assertNotIn(
            "complete_dataset", self.data_handler.datasets_container
        )
        train_dataset = self.data_handler.datasets_container["train_dataset"]
        val_dataset = self.data_handler.datasets_container["val_dataset"]
        test_dataset = self.data_handler.datasets_container["test_dataset"]
        self._assert_dataset(train_dataset)
        self._assert_dataset(val_dataset)
        self._assert_dataset(test_dataset)
        self.assertEqual(train_dataset.cardinality().numpy(), 3)
        self.assertEqual(val_dataset.cardinality().numpy(), 1)
        self.assertEqual(test_dataset.cardinality().numpy(), 1)

    def test_save_images(self):
        """
        Tests saving images from the dataset to a specified directory.
        """
        self.data_handler.load_dataset(self.jpg_dict)
        output_dir = self.temp_dir
        self.data_handler.save_images(output_dir)
        saved_files = os.listdir(output_dir)
        self.assertGreater(len(saved_files), 0)

    def test_backup_and_restore_datasets(self):
        """
        Tests backing up and restoring datasets.
        """
        self.data_handler.load_dataset(self.jpg_dict)
        self.assertTrue(
            "complete_dataset" in self.data_handler.datasets_container
        )
        self.data_handler.backup_datasets()
        self.data_handler.datasets_container.pop("complete_dataset")
        self.data_handler.restore_datasets()
        self.assertTrue(
            "complete_dataset" in self.data_handler.datasets_container
        )
        self._assert_dataset(
            self.data_handler.datasets_container["complete_dataset"]
        )

    def _same_datasets_containers(self, container1, container2):
        """
        Asserts that two dataset containers are equal.

        Parameters
        ----------
        container1 : dict
            First dataset container.
        container2 : dict
            Second dataset container.
        """
        self.assertEqual(len(container1), len(container2))
        for key, dataset1 in container1.items():
            dataset2 = container2[key]
            self.assertEqual(dataset1, dataset2)

    def test_update_datasets_container(self):
        """
        Tests correct updating of the dataset container dictionary.
        """
        images = tf.random.normal((10, 28, 28, 1))
        labels = tf.constant([i for i in range(10)])
        dataset = tf.data.Dataset.from_tensor_slices((images, labels))

        reference_container = self.data_handler.datasets_container
        self.data_handler.load_dataset(dataset)
        self._same_datasets_containers(
            reference_container, self.data_handler.datasets_container
        )


if __name__ == "__main__":
    unittest.main()
