import os
import unittest

import matplotlib.pyplot as plt

from src.plotting.functions.plot_confusion_matrix import plot_confusion_matrix
from src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotConfusionMatrix(PlottingTestCase):
    """ Test suite for the plot_confusion_matrix function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.y_true = [0, 1, 2, 2, 0, 1, 0, 2, 1, 1]
        cls.y_pred = [0, 2, 2, 2, 0, 1, 0, 0, 1, 1]
        cls.class_names = ["Class A", "Class B", "Class C"]
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_confusion_matrix_test.png"
        )

    def test_plot_confusion_matrix(self):
        """ Test plotting confusion matrix. """
        fig = plot_confusion_matrix(self.y_true, self.y_pred, self.class_names)
        self._save_and_close_figure(fig, "confusion_matrix.png")


if __name__ == "__main__":
    unittest.main()
