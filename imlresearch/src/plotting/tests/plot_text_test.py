import os
import unittest

from imlresearch.src.plotting.functions.plot_text import plot_text
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotText(PlottingTestCase):
    """
    Test suite for the plot_text function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with sample text for testing.
        """
        super().setUpClass()
        cls.text_sample = (
            "This is an example of a long text that will be plotted on a "
            "matplotlib figure. The function will automatically determine "
            "the size of the figure based on the length of the text."
        )
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_text_test.png"
        )

    def test_plot_text(self):
        """
        Tests the plot_text function with a sample text.
        """
        fig = plot_text(self.text_sample)
        self._save_and_close_figure(fig, "plot_text.png")

    def test_plot_empty_text(self):
        """
        Tests the plot_text function with an empty string.
        """
        fig = plot_text("")
        self._save_and_close_figure(fig, "plot_empty_text.png")

    def test_plot_multiline_text(self):
        """
        Tests the plot_text function with multiline text.
        """
        multiline_text = "Line 1\nLine 2\nLine 3"
        fig = plot_text(multiline_text)
        self._save_and_close_figure(fig, "plot_multiline_text.png")


if __name__ == "__main__":
    unittest.main()
