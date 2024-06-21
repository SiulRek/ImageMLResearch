import os
import unittest

import matplotlib.pyplot as plt

from src.plotting.plotters.plotter import Plotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestPlotter(BaseTestCase):
    """ Test suite for the Plotter class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(sample_num=10, labeled=True)
        cls.text_sample = (
            "This is a sample text to plot.\n"
            "This is a sample text to plot.\n"
            "This is a sample text to plot.\n"
        )
        cls.visualization_path = os.path.join(cls.results_dir, "plotter_test.png")

    def setUp(self):
        super().setUp()
        research_attributes = ResearchAttributes(
            label_type="categorical",
            category_names=[str(i) for i in range(10)],
        )
        research_attributes._dataset_container["complete_dataset"] = self.image_dataset
        self.plotter = Plotter()
        self.plotter.update_research_attributes(research_attributes)

    def test_add_figure(self):
        """ Test the _add_figure method. """
        fig = plt.figure()
        self.plotter._add_figure("test_figure", fig)
        self.assertEqual(len(self.plotter._figures), 1, "The figure was not added.")
        self.assertEqual(
            self.plotter._figures["test_figure"],
            fig,
            "The figure was not added correctly.",
        )

    def test_plot_images(self):
        """ Test the plot_images method. """

        def label_to_title(label):
            return "Label: " + str(label.numpy())

        fig = self.plotter.plot_images(
            grid_size=(2, 2),
            label_to_title_func=label_to_title,
            title="Test Plot Images",
            show=False,
        )
        self.assertEqual(len(self.plotter._figures), 1, "The figure was not added.")
        fig.savefig(os.path.join(self.results_dir, "plotter_plot_images.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plotter_plot_images.png")),
            "Plot images figure was not saved.",
        )

    def test_plot_text(self):
        """ Test the plot_text method. """
        fig = self.plotter.plot_text(
            self.text_sample, title="Sample Text Plot", show=False
        )
        fig.savefig(os.path.join(self.results_dir, "plotter_plot_text.png"))
        self.assertEqual(len(self.plotter._figures), 1, "The figure was not added.")
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plotter_plot_text.png")),
            "Plot text figure was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
