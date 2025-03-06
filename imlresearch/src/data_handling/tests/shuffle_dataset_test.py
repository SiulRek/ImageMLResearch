import unittest

import tensorflow as tf

from imlresearch.src.data_handling.manipulation.shuffle_dataset import (
    shuffle_dataset,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestShuffleDataset(BaseTestCase):
    """
    Test suite for the `shuffle_dataset` function.
    """

    def setUp(self):
        """
        Sets up the test case by initializing a dataset and a random seed.
        """
        super().setUp()
        self.dataset = tf.data.Dataset.range(100)
        self.random_seed = 42

    def test_shuffling_changes_order(self):
        """
        Tests that shuffling changes the order of dataset elements.
        """
        original_elements = list(self.dataset.as_numpy_iterator())
        shuffled_dataset = shuffle_dataset(self.dataset, self.random_seed)
        shuffled_elements = list(shuffled_dataset.as_numpy_iterator())

        self.assertNotEqual(
            original_elements,
            shuffled_elements,
            "Shuffling did not change the dataset order.",
        )

    def test_shuffling_is_consistent_with_seed(self):
        """
        Tests that shuffling with the same seed produces the same order.
        """
        shuffled_dataset_1 = shuffle_dataset(self.dataset, self.random_seed)
        shuffled_elements_1 = list(shuffled_dataset_1.as_numpy_iterator())

        shuffled_dataset_2 = shuffle_dataset(self.dataset, self.random_seed)
        shuffled_elements_2 = list(shuffled_dataset_2.as_numpy_iterator())

        self.assertEqual(
            shuffled_elements_1,
            shuffled_elements_2,
            "Shuffling with the same seed should produce the same order.",
        )

    def test_shuffling_with_different_seeds(self):
        """
        Tests that shuffling with different seeds produces different orders.
        """
        shuffled_dataset_1 = shuffle_dataset(self.dataset, self.random_seed)
        shuffled_elements_1 = list(shuffled_dataset_1.as_numpy_iterator())

        different_seed = self.random_seed + 1
        shuffled_dataset_2 = shuffle_dataset(self.dataset, different_seed)
        shuffled_elements_2 = list(shuffled_dataset_2.as_numpy_iterator())

        self.assertNotEqual(
            shuffled_elements_1,
            shuffled_elements_2,
            "Shuffling with different seeds should produce different orders.",
        )

    def test_shuffling_of_batched_datasets(self):
        """
        Tests that shuffling works correctly with batched datasets.
        """
        batched_dataset = self.dataset.batch(10)
        shuffled_dataset = shuffle_dataset(batched_dataset, self.random_seed)
        shuffled_elements = list(shuffled_dataset.as_numpy_iterator())

        self.assertEqual(
            len(shuffled_elements),
            10,
            "Shuffling should retain all original batches.",
        )

    def test_shuffling_order_stays_consistent(self):
        """
        Tests that shuffling produces the same order in multiple iterations.
        """
        shuffled_dataset = shuffle_dataset(self.dataset, self.random_seed)
        shuffled_elements = list(shuffled_dataset.as_numpy_iterator())

        new_list = []
        for sample in shuffled_elements:
            new_list.append(sample)
        new_dataset = tf.data.Dataset.from_tensor_slices(new_list)
        new_elements = list(new_dataset.as_numpy_iterator())

        self.assertEqual(
            shuffled_elements,
            new_elements,
            "Shuffling should produce the same order in multiple iterations.",
        )

    def test_shuffling_of_dataset_with_features_and_labels(self):
        """
        Tests that shuffling works correctly for datasets containing
        both features and labels.
        """
        features = tf.random.normal((100, 28, 28, 1))
        labels = tf.constant([i for i in range(100)])
        dataset = tf.data.Dataset.from_tensor_slices((features, labels))

        shuffled_dataset = shuffle_dataset(dataset, self.random_seed)
        shuffled_elements = list(shuffled_dataset.as_numpy_iterator())

        self.assertEqual(
            len(shuffled_elements),
            100,
            "Shuffling should retain all original elements.",
        )


if __name__ == "__main__":
    unittest.main()
