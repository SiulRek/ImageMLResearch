import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt
import numpy as np

from src.plotting.plotters.multi_class_plotter import MultiClassPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestMultiClassPlotter(BaseTestCase):
    """ Test suite for the MultiClassPlotter class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # One-hot encoded true and predicted labels for 3 classes
        cls.y_true = np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 0],
                [0, 1, 0],
            ]
        )
        cls.y_pred = np.array(
            [
                [1, 0, 0],
                [1, 0, 0],
                [0, 0, 1],
                [1, 0, 0],
                [0, 0, 1],
                [0, 0, 1],
                [1, 0, 0],
                [0, 1, 0],
            ]
        )
        cls.class_names = ["Class 0", "Class 1", "Class 2"]
        cls.multi_class_plotter = MultiClassPlotter()
        research_attributes = ResearchAttributes(
            label_type="multi_class", class_names=cls.class_names
        )
        cls.multi_class_plotter.update_research_attributes(research_attributes)
        cls.multi_class_plotter._retrieve_output_data = MagicMock(
            return_value=(cls.y_true, cls.y_pred, cls.class_names)
        )

    def setUp(self):
        super().setUp()
        self.multi_class_plotter._figures = {}  # Reset figures before each test

    def test_plot_confusion_matrix(self):
        """ Test the plot_confusion_matrix method. """
        fig = self.multi_class_plotter.plot_confusion_matrix(
            title="Test Confusion Matrix", show=False
        )
        self.assertEqual(
            len(self.multi_class_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_confusion_matrix",
            self.multi_class_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(
            os.path.join(
                self.results_dir, "multi_class_plotter_plot_confusion_matrix.png"
            )
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "multi_class_plotter_plot_confusion_matrix.png"
                )
            ),
            "Confusion matrix figure was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
