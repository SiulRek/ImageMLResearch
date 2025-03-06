import os
import unittest

from imlresearch.src.plotting.functions.plot_roc_curve import plot_roc_curve
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotRocCurve(PlottingTestCase):
    """
    Test suite for the plot_roc_curve function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample data for testing.
        """
        super().setUpClass()
        cls.y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
        cls.y_pred_proba = [0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 0.3, 0.9, 0.6, 0.15]
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_roc_curve_test.png"
        )

    def test_plot_roc_curve(self):
        """
        Tests the plot_roc_curve function.
        """
        fig = plot_roc_curve(self.y_true, self.y_pred_proba)
        self._save_and_close_figure(fig, "roc_curve.png")


if __name__ == "__main__":
    unittest.main()
