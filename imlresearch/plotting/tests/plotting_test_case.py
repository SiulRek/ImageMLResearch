from abc import ABC
import os

import matplotlib.pyplot as plt

from imlresearch.testing.bases.base_test_case import BaseTestCase


class PlottingTestCase(ABC, BaseTestCase):
    """ Base test case for the Plotting module tests. """

    def _save_and_close_figure(self, figure, file_name):
        path = os.path.join(self.results_dir, file_name)
        figure.savefig(path)
        plt.close(figure)
