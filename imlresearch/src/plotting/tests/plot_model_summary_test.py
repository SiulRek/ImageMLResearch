import os
import unittest

from keras.layers import Dense
from keras.models import Sequential

from imlresearch.src.plotting.functions.plot_model_summary import (
    plot_model_summary,
)
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotModelSummary(PlottingTestCase):
    """
    Test suite for the plot_model_summary function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by creating a simple model for testing.
        """
        super().setUpClass()
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_model_summary_test.png"
        )

        # Create a simple model for testing
        cls.model = Sequential(
            [
                Dense(32, input_shape=(784,), activation="relu"),
                Dense(10, activation="softmax"),
            ]
        )

    def test_plot_model_summary(self):
        """
        Tests the plot_model_summary function.
        """
        fig = plot_model_summary(self.model)
        self._save_and_close_figure(fig, "model_summary.png")


if __name__ == "__main__":
    unittest.main()
