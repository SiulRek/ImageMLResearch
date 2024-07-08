import os
import unittest

from keras.layers import Dense
from keras.models import Sequential
import matplotlib.pyplot as plt

from src.plotting.functions.plot_model_summary import plot_model_summary
from src.testing.base.base_test_case import BaseTestCase


class TestPlotModelSummary(BaseTestCase):
    """ Test suite for the plot_model_summary function. """

    @classmethod
    def setUpClass(cls):
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
        """ Test plotting the model summary. """
        fig = plot_model_summary(self.model)
        fig.savefig(os.path.join(self.results_dir, "plot_model_summary.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plot_model_summary.png")),
            "Model summary plot was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
