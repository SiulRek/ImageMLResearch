import os
import unittest

from imlresearch.src.plotting.functions.plot_images import plot_images
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotImages(PlottingTestCase):
    """
    Test suite for the plot_images function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample image datasets.
        """
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(sample_num=10)
        cls.labeled_dataset = cls.load_mnist_digits_dataset(
            sample_num=10, labeled=True
        )
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_images_test.png"
        )

    def test_plot_images_without_labels(self):
        """
        Tests plotting images without labels.
        """
        fig = plot_images(self.image_dataset, grid_size=(2, 2))
        self._save_and_close_figure(fig, "plot_images_without_labels.png")

    def test_plot_images_with_labels(self):
        """
        Tests plotting images with labels.
        """

        def label_to_title(label):
            return "Label:" + str(label.numpy())

        fig = plot_images(
            self.labeled_dataset,
            grid_size=(2, 2),
            label_to_title_func=label_to_title,
        )
        self._save_and_close_figure(fig, "plot_images_with_labels.png")

    def test_plot_images_with_invalid_label_to_title_func(self):
        """
        Tests plotting images with an invalid label_to_title_func.
        """

        def invalid_label_to_title(label):
            msg = "Invalid label"
            raise ValueError(msg)

        with self.assertRaises(ValueError):
            plot_images(
                self.labeled_dataset,
                grid_size=(2, 2),
                label_to_title_func=invalid_label_to_title,
            )


if __name__ == "__main__":
    unittest.main()
