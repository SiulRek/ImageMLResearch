import os
import unittest

import matplotlib.pyplot as plt
import numpy as np

from imlresearch.src.plotting.functions.plot_results import (
    plot_multi_class_classification_results,
    plot_binary_classification_results,
)
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotMultiClassClassificationResults(PlottingTestCase):
    """
    Test suite for the plot_multi_class_classification_results function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample data for multi-class classification.
        """
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(
            sample_num=8, labeled=True
        )
        cls.class_names = [f"Class {i}" for i in range(10)]
        cls.images = []
        cls.y_true = []
        for image, label in cls.image_dataset:
            cls.images.append(image.numpy())
            cls.y_true.append(label.numpy())

        cls.images = np.array(cls.images)
        cls.y_true = np.array(cls.y_true)
        cls.y_pred = np.random.rand(cls.y_true.shape[0], cls.y_true.shape[1])

    def test_plot_results_without_prediction_bar(self):
        """
        Tests plotting multi-class classification results without prediction
        bars.
        """
        fig = plot_multi_class_classification_results(
            x=self.images,
            y_true=self.y_true,
            y_pred=self.y_pred,
            class_names=self.class_names,
            grid_size=(2, 4),
            prediction_bar=False,
        )
        self._save_and_close_figure(fig, "without_prediction_bar.png")

    def test_plot_results_with_prediction_bar(self):
        """
        Tests plotting multi-class classification results with prediction bars.
        """
        fig = plot_multi_class_classification_results(
            x=self.images,
            y_true=self.y_true,
            y_pred=self.y_pred,
            class_names=self.class_names,
            grid_size=(2, 4),
            prediction_bar=True,
        )
        self._save_and_close_figure(fig, "with_prediction_bar.png")


class TestPlotBinaryClassificationResults(PlottingTestCase):
    """
    Test suite for the plot_binary_classification_results function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample data for binary classification.
        """
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(
            sample_num=8, labeled=True, binary=True
        )
        cls.class_names = ["Class 0", "Class 1"]
        cls.images = []
        cls.y_true = []
        for image, label in cls.image_dataset:
            cls.images.append(image.numpy())
            cls.y_true.append(label.numpy())

        cls.images = np.array(cls.images)
        cls.y_true = np.array(cls.y_true)
        cls.y_pred = np.random.rand(cls.y_true.shape[0])

    def test_plot_results_without_prediction_bar(self):
        """
        Tests plotting binary classification results without prediction bars.
        """
        fig = plot_binary_classification_results(
            x=self.images,
            y_true=self.y_true,
            y_pred=self.y_pred,
            class_names=self.class_names,
            grid_size=(2, 4),
        )
        path = os.path.join(self.results_dir, "results.png")
        fig.savefig(path)
        plt.close(fig)


if __name__ == "__main__":
    unittest.main()
