import os
import unittest

import matplotlib.pyplot as plt

from src.plotting.functions.plot_roc_curve import plot_roc_curve
from src.testing.base.base_test_case import BaseTestCase


class TestPlotRocCurve(BaseTestCase):
    """ Test suite for the plot_roc_curve function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
        cls.y_pred_proba = [0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 0.3, 0.9, 0.6, 0.15]
        cls.class_names = ["Class 0", "Class 1"]
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_roc_curve_test.png"
        )

    def test_plot_roc_curve(self):
        """ Test plotting ROC curve. """
        fig = plot_roc_curve(self.y_true, self.y_pred_proba, self.class_names)
        fig.savefig(os.path.join(self.results_dir, "roc_curve.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "roc_curve.png")),
            "ROC curve plot was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
