import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from src.plotting.plotters.binary_plotter import BinaryPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestBinaryPlotter(BaseTestCase):
    """ Test suite for the BinaryPlotter class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.y_true = [0, 1, 0, 1, 0, 1, 0, 1]
        cls.y_pred = [0, 0, 0, 1, 1, 1, 0, 1]
        cls.class_names = ["Class 0", "Class 1"]
        cls.binary_plotter = BinaryPlotter()
        research_attributes = ResearchAttributes(
            label_type="binary", class_names=cls.class_names
        )
        cls.binary_plotter.update_research_attributes(research_attributes)
        cls.binary_plotter._retrieve_output_data = MagicMock(
            return_value=(cls.y_true, cls.y_pred, cls.class_names)
        )

    def setUp(self):
        super().setUp()
        self.binary_plotter._figures = {}  # Reset figures before each test

    def test_plot_confusion_matrix(self):
        """ Test the plot_confusion_matrix method. """
        fig = self.binary_plotter.plot_confusion_matrix(
            title="Test Confusion Matrix", show=False
        )
        self.assertEqual(
            len(self.binary_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_confusion_matrix",
            self.binary_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(
            os.path.join(self.results_dir, "binary_plotter_plot_confusion_matrix.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "binary_plotter_plot_confusion_matrix.png"
                )
            ),
            "Confusion matrix figure was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
