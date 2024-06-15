import os
import unittest

import matplotlib.pyplot as plt

from src.plotting.functions.plot_text import plot_text
from src.testing.base_test_case import BaseTestCase


class TestPlotText(BaseTestCase):
    """ Test suite for the plot_text function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.text_sample = """This is an example of a long text that will be plotted
on a matplotlib figure. The function will automatically
determine the size of the figure based on the length of the text."""
        cls.visualization_path = os.path.join(cls.results_dir, "plot_text_test.png")

    def test_plot_text(self):
        """ Test plotting text. """
        fig = plot_text(self.text_sample)
        fig.savefig(os.path.join(self.results_dir, "plot_text.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plot_text.png")),
            "Plot text was not saved.",
        )

    def test_plot_empty_text(self):
        """ Test plotting empty text. """
        fig = plot_text("")
        fig.savefig(os.path.join(self.results_dir, "plot_empty_text.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plot_empty_text.png")),
            "Plot empty text was not saved.",
        )

    def test_plot_multiline_text(self):
        """ Test plotting multiline text. """
        multiline_text = "Line 1\nLine 2\nLine 3"
        fig = plot_text(multiline_text)
        fig.savefig(os.path.join(self.results_dir, "plot_multiline_text.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plot_multiline_text.png")),
            "Plot multiline text was not saved.",
        )

    def test_plot_text_with_title(self):
        """ Test plotting text with title. """
        fig = plot_text(self.text_sample, title="Sample Text Plot")
        fig.savefig(os.path.join(self.results_dir, "plot_text_with_title.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(os.path.join(self.results_dir, "plot_text_with_title.png")),
            "Plot text with title was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
