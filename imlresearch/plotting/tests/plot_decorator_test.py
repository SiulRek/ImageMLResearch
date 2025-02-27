import unittest
from unittest.mock import MagicMock, patch

import matplotlib.pyplot as plt

from imlresearch.plotting.plotters.plotter import plot_decorator, Plotter
from imlresearch.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotDecorator(PlottingTestCase):
    """ Test suite for the plot_decorator function. """

    def setUp(self):
        super().setUp()
        self.plotter = Plotter()
        self.plotter._figures = {}
        self.plotter._add_figure = MagicMock(side_effect=self.plotter._add_figure)

    def test_plot_decorator_with_default_title_and_show(self):
        """ Test plot_decorator with default title and show parameters. """

        @plot_decorator(default_title="Default Title", default_show=False)
        def sample_plot_func(self):
            fig, ax = plt.subplots()
            ax.plot([0, 1], [0, 1])
            return fig

        fig = sample_plot_func(self.plotter)

        self.plotter._add_figure.assert_called_once_with("default_title", fig)
        self.assertEqual(fig._suptitle.get_text(), "Default Title")
        self.assertEqual(len(self.plotter._figures), 1)
        plt.close(fig)

    def test_plot_decorator_with_custom_title_and_show(self):
        """ Test plot_decorator with custom title and show parameters. """

        @plot_decorator(default_title="Default Title", default_show=False)
        def sample_plot_func(self):
            fig, ax = plt.subplots()
            ax.plot([0, 1], [0, 1])
            return fig

        with patch("matplotlib.pyplot.show") as mock_show:
            fig = sample_plot_func(self.plotter, title="Custom Title", show=True)
            mock_show.assert_called_once()

        self.plotter._add_figure.assert_called_once_with("custom_title", fig)
        self.assertEqual(fig._suptitle.get_text(), "Custom Title")
        self.assertEqual(len(self.plotter._figures), 1)
        plt.close(fig)

    def test_plot_decorator_without_title_and_show(self):
        """ Test plot_decorator without title and show parameters. """

        @plot_decorator(default_title="Default Title", default_show=False)
        def sample_plot_func(self):
            fig, ax = plt.subplots()
            ax.plot([0, 1], [0, 1])
            return fig

        fig = sample_plot_func(self.plotter)

        self.plotter._add_figure.assert_called_once_with("default_title", fig)
        self.assertEqual(fig._suptitle.get_text(), "Default Title")
        self.assertEqual(len(self.plotter._figures), 1)
        plt.close(fig)

    def test_plot_decorator_with_invalid_figure(self):
        """ Test plot_decorator raises ValueError for invalid figure. """

        @plot_decorator(default_title="Invalid Figure", default_show=False)
        def sample_plot_func(self):
            return "Not a figure"

        # Mock the _add_figure method to raise ValueError if the figure is not valid
        self.plotter._add_figure = MagicMock(
            side_effect=ValueError(
                "The figure must be an instance of matplotlib.pyplot.Figure."
            )
        )

        with self.assertRaises(ValueError):
            sample_plot_func(self.plotter)


if __name__ == "__main__":
    unittest.main()
