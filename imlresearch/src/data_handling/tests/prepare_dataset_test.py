import unittest

import tensorflow as tf

from imlresearch.src.data_handling.manipulation.prepare_dataset import (
    prepare_dataset,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestPrepareDataset(BaseTestCase):
    """
    Test suite for the `prepare_dataset` function.
    """

    def setUp(self):
        """
        Sets up the test case by loading a sample dataset.
        """
        super().setUp()
        self.dataset = self.load_mnist_digits_dataset(sample_num=100)

    def test_shuffling(self):
        """
        Tests that shuffling changes the order of dataset elements.
        """
        original_first_element = next(iter(self.dataset)).numpy()
        enhanced = prepare_dataset(self.dataset, shuffle_seed=42)
        enhanced_first_element = next(iter(enhanced)).numpy()
        self.assertFalse(
            tf.reduce_all(
                tf.equal(original_first_element, enhanced_first_element)
            ),
            "Shuffling did not change the order of the dataset.",
        )

    def test_batching(self):
        """
        Tests that batching correctly groups dataset elements.
        """
        enhanced = prepare_dataset(self.dataset, batch_size=10)
        self.assertEqual(
            enhanced.cardinality().numpy(),
            10,
            "Batching should create 10 batches from 100 elements.",
        )

    def test_repeating(self):
        """
        Tests that repeating extends the dataset size correctly.
        """
        repeated = prepare_dataset(self.dataset, repeat_num=3)
        self.assertEqual(
            repeated.cardinality().numpy(),
            300,
            "Dataset should be repeated 3 times, totaling 300 elements.",
        )


if __name__ == "__main__":
    unittest.main()
