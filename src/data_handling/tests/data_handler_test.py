import os
import unittest

import tensorflow as tf

from src.data_handling.data_handler import DataHandler
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestDataHandler(BaseTestCase):
    """ Test suite for the DataHandler class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.jpg_dict, cls.png_dict = cls.load_mnist_digits_dicts()
        research_attributes = ResearchAttributes(
            label_type="multi_class",
            class_names=[str(i) for i in range(10)],
        )
        cls.data_handler = DataHandler()
        cls.data_handler.synchronize_research_attributes(research_attributes)

    def _assert_dataset(self, dataset):
        """ Asserts that the dataset is of type tf.data.Dataset and that the images
        and labels have the correct shapes. """
        self.assertIsInstance(
            dataset, tf.data.Dataset, "Dataset is not of type tf.data.Dataset."
        )

        for image, label in dataset.take(1):
            self.assertIn(image.shape, [(28, 28, 1), (28, 28, 3)])
            self.assertEqual(label.shape, (10,))

    def test_load_dataset_from_dict(self):
        """ Test creation of dataset and storage in the dataset container. """
        self.data_handler.load_dataset(self.jpg_dict)
        self.assertIn("complete_dataset", self.data_handler.datasets_container)
        dataset = self.data_handler.datasets_container["complete_dataset"]
        self.assertIsInstance(dataset, tf.data.Dataset)
        self._assert_dataset(dataset)

    def test_load_dataset_from_tf_dataset(self):
        """ Test loading of dataset from a TensorFlow Dataset. """
        images = tf.random.normal((10, 28, 28, 1))
        labels = tf.constant([i for i in range(10)])
        labels = tf.one_hot(labels, 10)
        dataset = tf.data.Dataset.from_tensor_slices((images, labels))

        self.data_handler.load_dataset(dataset)
        self.assertIn("complete_dataset", self.data_handler._datasets_container)
        dataset = self.data_handler.datasets_container["complete_dataset"]
        self._assert_dataset(dataset)

    def test_enhance_dataset(self):
        """ Test enhancement of dataset and updating in the dataset container. """
        self.data_handler.load_dataset(self.jpg_dict)
        original_dataset = list(
            self.data_handler.datasets_container["complete_dataset"]
        )
        self.data_handler.enhance_datasets(batch_size=2, shuffle=True, random_seed=42)
        self.assertIn("complete_dataset", self.data_handler.datasets_container)
        enhanced_dataset = self.data_handler.datasets_container["complete_dataset"]

        for batch in enhanced_dataset:
            self.assertEqual(batch[0].shape[0], 2)
            break

        enhanced_dataset_unbatched = enhanced_dataset.unbatch()
        self._assert_dataset(enhanced_dataset_unbatched)
        for original, enhanced in zip(original_dataset, enhanced_dataset_unbatched):
            if not tf.reduce_all(tf.equal(original[0], enhanced[0])):
                break
        else:
            self.fail(
                "All tensors are equal after enhancement, indicating no shuffling occurred"
            )

    def test_split_dataset(self):
        """ Test splitting of dataset and storage of splits in the dataset
        container. """
        self.data_handler.load_dataset(self.jpg_dict)
        self.data_handler.split_dataset(train_size=0.6, val_size=0.2, test_size=0.2)
        self.assertIn("train_dataset", self.data_handler.datasets_container)
        self.assertIn("val_dataset", self.data_handler.datasets_container)
        self.assertIn("test_dataset", self.data_handler.datasets_container)
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
        """ Test saving images from dataset to specified directory. """
        self.data_handler.load_dataset(self.jpg_dict)
        output_dir = self.temp_dir
        self.data_handler.save_images(output_dir)
        saved_files = os.listdir(output_dir)
        self.assertGreater(len(saved_files), 0)

    def test_backup_and_restore_datasets(self):
        """ Test backup and restore of datasets. """
        self.data_handler.load_dataset(self.jpg_dict)
        self.assertTrue("complete_dataset" in self.data_handler.datasets_container)
        self.data_handler.backup_datasets()
        self.data_handler.datasets_container.pop("complete_dataset")
        self.data_handler.restore_datasets()
        self.assertTrue("complete_dataset" in self.data_handler.datasets_container)
        self._assert_dataset(self.data_handler.datasets_container["complete_dataset"])


if __name__ == "__main__":
    unittest.main()
