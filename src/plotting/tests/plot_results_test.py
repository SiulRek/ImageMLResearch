import os
import unittest

import matplotlib.pyplot as plt
import numpy as np

from src.plotting.functions.plot_results import plot_multi_class_classification_results
from src.testing.base.base_test_case import BaseTestCase


class TestPlotMultiClassClassificationResults(BaseTestCase):
    """ Test suite for the plot_multi_class_classification_results function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image_dataset = cls.load_mnist_digits_dataset(sample_num=8, labeled=True)
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
        """ Test plotting multi-class classification results without prediction
        bars. """
        fig = plot_multi_class_classification_results(
            x=self.images,
            y_true=self.y_true,
            y_pred=self.y_pred,
            class_names=self.class_names,
            grid_size=(2, 4),
            prediction_bar=False,
        )
        fig.savefig(os.path.join(self.results_dir, "without_prediction_bar.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "without_prediction_bar.png")
            ),
            "Plot without prediction bars was not saved.",
        )

    def test_plot_results_with_prediction_bar(self):
        """ Test plotting multi-class classification results with prediction bars. """
        fig = plot_multi_class_classification_results(
            x=self.images,
            y_true=self.y_true,
            y_pred=self.y_pred,
            class_names=self.class_names,
            grid_size=(2, 4),
            prediction_bar=False,
        )
        fig.savefig(os.path.join(self.results_dir, "with_prediction_bar.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "with_prediction_bar.png")),
            "Plot with prediction bars was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
