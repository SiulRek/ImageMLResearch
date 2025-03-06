import os
import unittest

from imlresearch.src.plotting.functions.plot_pr_curve import plot_pr_curve
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotPRCurve(PlottingTestCase):
    """
    Test suite for the plot_pr_curve function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample data for testing.
        """
        super().setUpClass()
        cls.y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
        cls.y_pred = [0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 0.3, 0.9, 0.6, 0.15]
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_pr_curve_test.png"
        )

    def test_plot_pr_curve(self):
        """
        Tests the plot_pr_curve function.
        """
        fig = plot_pr_curve(self.y_true, self.y_pred)
        self._save_and_close_figure(fig, "pr_curve.png")


if __name__ == "__main__":
    unittest.main()
