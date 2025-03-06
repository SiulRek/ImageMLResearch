import unittest

import tensorflow as tf

from imlresearch.src.data_handling.manipulation.split_dataset import (
    split_dataset,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestDatasetFunctions(BaseTestCase):
    """
    Test suite for the `split_dataset` function.
    """

    def setUp(self):
        """
        Sets up each test by creating a sample dataset.
        """
        super().setUp()
        self.dataset = tf.data.Dataset.range(100)

    def test_split_proportions(self):
        """
        Tests that the dataset is split into correct proportions.
        """
        train, val, test = split_dataset(self.dataset)
        self.assertEqual(
            train.cardinality().numpy(), 80,
            "Training set size should be 80% of total."
        )
        self.assertEqual(
            val.cardinality().numpy(), 10,
            "Validation set size should be 10% of total."
        )
        self.assertEqual(
            test.cardinality().numpy(), 10,
            "Test set size should be 10% of total."
        )

    def test_split_proportions_error(self):
        """
        Tests that an error is raised when the split proportions do not sum
        to 1.0.
        """
        with self.assertRaises(ValueError):
            split_dataset(
                self.dataset, train_split=0.7, val_split=0.2, test_split=0.2
            )

    def test_split_with_zero_size(self):
        """
        Tests handling of zero-size splits.
        """
        train, val, test = split_dataset(
            self.dataset, train_split=0.0, val_split=0.5, test_split=0.5
        )
        self.assertIsNone(train, "Training set should be None when size is 0.")
        self.assertEqual(
            val.cardinality().numpy(), 50,
            "Validation set size should be 50% of total."
        )
        self.assertEqual(
            test.cardinality().numpy(), 50,
            "Test set size should be 50% of total."
        )

        train, val, test = split_dataset(
            self.dataset, train_split=0.5, val_split=0.0, test_split=0.5
        )
        self.assertEqual(
            train.cardinality().numpy(), 50,
            "Training set size should be 50% of total."
        )
        self.assertIsNone(val, "Validation set should be None when size is 0.")
        self.assertEqual(
            test.cardinality().numpy(), 50,
            "Test set size should be 50% of total."
        )

        train, val, test = split_dataset(
            self.dataset, train_split=0.5, val_split=0.5, test_split=0.0
        )
        self.assertEqual(
            train.cardinality().numpy(), 50,
            "Training set size should be 50% of total."
        )
        self.assertEqual(
            val.cardinality().numpy(), 50,
            "Validation set size should be 50% of total."
        )
        self.assertIsNone(test, "Test set should be None when size is 0.")

    def test_split_with_manual_dataset_size(self):
        """
        Tests that `split_dataset` correctly handles a manually provided
        dataset size.
        """
        train, val, test = split_dataset(self.dataset, dataset_size=100)

        self.assertEqual(
            train.cardinality().numpy(),
            80,
            "Training set size should be 80% of the specified dataset size."
        )
        self.assertEqual(
            val.cardinality().numpy(),
            10,
            "Validation set size should be 10% of the specified dataset size."
        )
        self.assertEqual(
            test.cardinality().numpy(),
            10,
            "Test set size should be 10% of the specified dataset size."
        )


if __name__ == "__main__":
    unittest.main()
