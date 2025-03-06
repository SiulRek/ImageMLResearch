import unittest

from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.utils import unbatch_dataset_if_batched


class TestUnbatchDatasetIfBatched(BaseTestCase):
    """
    Test suite for the unbatch_dataset_if_batched function.
    """

    def test_unbatch_mnist_images_batched(self):
        """
        Test unbatching when the dataset is batched.
        """
        dataset = self.load_mnist_digits_dataset(labeled=False).batch(2)
        result_dataset = unbatch_dataset_if_batched(dataset)
        for sample in result_dataset.take(1):
            self.assertEqual(sample.shape.ndims, 3)

    def test_unbatch_mnist_images_unbatched(self):
        """
        Test unbatching when the dataset is already unbatched.
        """
        dataset = self.load_mnist_digits_dataset(labeled=False)
        result_dataset = unbatch_dataset_if_batched(dataset)
        for sample in result_dataset.take(1):
            self.assertEqual(sample.shape.ndims, 3)

    def test_invalid_input(self):
        """
        Test handling of invalid input types.
        """
        with self.assertRaises(ValueError):
            unbatch_dataset_if_batched([1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
