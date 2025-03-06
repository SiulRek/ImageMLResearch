import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential

from imlresearch.src.plotting.plotters.plotter import Plotter
from imlresearch.src.plotting.tests.plotting_test_case import (
    PlottingTestCase,
)
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)


class TestPlotter(PlottingTestCase):
    """
    Test suite for the Plotter class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample data for testing.
        """
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(
            sample_num=10, labeled=True
        )
        cls.text_sample = (
            "This is a sample text to plot.\n"
            "This is a sample text to plot.\n"
            "This is a sample text to plot.\n"
        )
        cls.visualization_path = os.path.join(
            cls.results_dir, "plotter_test.png"
        )

    @classmethod
    def _create_model(cls):
        """
        Creates a simple Keras model for testing.

        Returns
        -------
        keras.models.Sequential
            A simple feedforward neural network model.
        """
        model = Sequential([
            Dense(32, input_shape=(784,), activation="relu"),
            Dense(10, activation="softmax"),
        ])
        return model

    def setUp(self):
        """
        Sets up each test with a new instance of Plotter.
        """
        super().setUp()
        research_attributes = ResearchAttributes(
            label_type="multi_class",
            class_names=[str(i) for i in range(10)],
        )
        research_attributes._datasets_container[
            "complete_dataset"
        ] = self.image_dataset
        self.plotter = Plotter()
        self.plotter.synchronize_research_attributes(research_attributes)
        self.plotter._model = self._create_model()

    def test_add_figure(self):
        """
        Tests the _add_figure method to ensure a figure is added correctly.
        """
        fig = plt.figure()
        self.plotter._add_figure("test_figure", fig)
        self.assertEqual(
            len(self.plotter._figures), 1, "The figure was not added."
        )
        self.assertEqual(
            self.plotter._figures["test_figure"],
            fig,
            "The figure was not added correctly.",
        )

    def test_plot_images(self):
        """
        Tests the plot_images method.
        """

        def label_to_title(label):
            return "Label: " + str(label.numpy())

        fig = self.plotter.plot_images(
            grid_size=(2, 2),
            label_to_title_func=label_to_title,
            title="Test Plot Images",
            show=False,
        )
        self.assertEqual(
            len(self.plotter._figures), 1, "The figure was not added."
        )
        self._save_and_close_figure(fig, "plotter_plot_images.png")

    def test_plot_text(self):
        """
        Tests the plot_text method.
        """
        fig = self.plotter.plot_text(
            self.text_sample, title="Sample Text Plot", show=False
        )
        self.assertEqual(
            len(self.plotter._figures), 1, "The figure was not added."
        )
        self._save_and_close_figure(fig, "plotter_plot_text.png")

    def test_plot_training_history(self):
        """
        Tests the plot_training_history method.
        """
        self.plotter._training_history = MagicMock()
        self.plotter._training_history = {
            "loss": [0.25, 0.15, 0.1],
            "val_loss": [0.3, 0.2, 0.15],
            "accuracy": [0.9, 0.95, 0.97],
            "val_accuracy": [0.88, 0.93, 0.95],
        }
        fig = self.plotter.plot_training_history(
            title="Test Training History", show=False
        )
        fig.savefig(
            os.path.join(
                self.results_dir, "plotter_plot_training_history.png"
            )
        )
        self.assertEqual(
            len(self.plotter._figures), 1, "The figure was not added."
        )
        self._save_and_close_figure(fig, "plotter_plot_training_history.png")

    def test_plot_model_summary(self):
        """
        Tests the plot_model_summary method.
        """
        fig = self.plotter.plot_model_summary(
            title="Test Model Summary", show=False
        )
        self.assertEqual(
            len(self.plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_model_summary",
            self.plotter._figures,
            "The figure name is incorrect.",
        )
        self._save_and_close_figure(fig, "plotter_plot_model_summary.png")


if __name__ == "__main__":
    unittest.main()
