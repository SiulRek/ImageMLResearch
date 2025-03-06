from abc import ABC
import os
import matplotlib.pyplot as plt

from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class PlottingTestCase(ABC, BaseTestCase):
    """
    Base test case for the Plotting module tests.
    """

    def _save_and_close_figure(self, figure, file_name):
        """
        Saves and closes a Matplotlib figure.

        Parameters
        ----------
        figure : matplotlib.figure.Figure
            The figure to be saved.
        file_name : str
            The name of the file to save the figure as.

        Returns
        -------
        None
        """
        path = os.path.join(self.results_dir, file_name)
        figure.savefig(path)
        plt.close(figure)
