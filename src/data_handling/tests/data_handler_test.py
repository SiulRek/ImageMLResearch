import os
import unittest

import tensorflow as tf

from src.data_handling.data_handler import DataHandler
from src.testing.base.base_test_case import BaseTestCase


class TestDataHandler(BaseTestCase):
    """ Test suite for the DataHandler class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.jpg_dict, cls.png_dict = cls.load_mnist_digits_dicts()
        cls.data_handler = DataHandler(
            label_type="categorical", category_names=[str(i) for i in range(10)]
        )

    def setUp(self):
        super().setUp()
        self.data_handler.create_dataset(self.jpg_dict)

    def test_create_dataset(self):
        """ Test creation of dataset and storage in the dataset container. """
        self.assertIn("complete_dataset", self.data_handler.dataset_container)
        self.assertIsInstance(
            self.data_handler.dataset_container["complete_dataset"], tf.data.Dataset
        )

    def test_enhance_dataset(self):
        """ Test enhancement of dataset and updating in the dataset container. """
        original_dataset = list(self.data_handler.dataset_container["complete_dataset"])
        self.data_handler.enhance_dataset(
            ["complete_dataset"], batch_size=2, shuffle=True, random_seed=42
        )
        self.assertIn("complete_dataset", self.data_handler.dataset_container)
        enhanced_dataset = self.data_handler.dataset_container["complete_dataset"]
        self.assertIsInstance(enhanced_dataset, tf.data.Dataset)

        for batch in enhanced_dataset:
            self.assertEqual(batch[0].shape[0], 2)
            break

        enhanced_dataset_unbatched = enhanced_dataset.unbatch()
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
        self.data_handler.split_dataset(train_size=0.6, val_size=0.2, test_size=0.2)
        self.assertIn("train_dataset", self.data_handler.dataset_container)
        self.assertIn("val_dataset", self.data_handler.dataset_container)
        self.assertIn("test_dataset", self.data_handler.dataset_container)
        train_dataset = self.data_handler.dataset_container["train_dataset"]
        val_dataset = self.data_handler.dataset_container["val_dataset"]
        test_dataset = self.data_handler.dataset_container["test_dataset"]
        self.assertEqual(train_dataset.cardinality().numpy(), 3)
        self.assertEqual(val_dataset.cardinality().numpy(), 1)
        self.assertEqual(test_dataset.cardinality().numpy(), 1)

    def test_save_images(self):
        """ Test saving images from dataset to specified directory. """
        output_dir = self.temp_dir
        self.data_handler.save_images("complete_dataset", output_dir)
        saved_files = os.listdir(output_dir)
        self.assertGreater(len(saved_files), 0)

    def test_get_dataset(self):
        """ Test retrieval of dataset from the dataset container. """
        dataset = self.data_handler.get_dataset("complete_dataset")
        self.assertIsInstance(dataset, tf.data.Dataset)

    def test_get_nonexistent_dataset(self):
        """ Test retrieval of a non-existent dataset raises ValueError. """
        with self.assertRaises(ValueError):
            self.data_handler.get_dataset("nonexistent_dataset")


if __name__ == "__main__":
    unittest.main()
