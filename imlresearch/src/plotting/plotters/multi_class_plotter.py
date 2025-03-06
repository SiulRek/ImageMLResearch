import numpy as np

from imlresearch.src.data_handling.labelling.label_utils import reverse_one_hot
from imlresearch.src.plotting.functions.plot_confusion_matrix import (
    plot_confusion_matrix,
)
from imlresearch.src.plotting.functions.plot_results import (
    plot_multi_class_classification_results,
)
from imlresearch.src.plotting.plotters.plotter import Plotter, plot_decorator


class MultiClassPlotter(Plotter):
    """
    A class for plotting images and text using research attributes for
    multi-class classification.
    """

    @plot_decorator(default_title="Confusion Matrix", default_show=False)
    def plot_confusion_matrix(self, **general_plot_kwargs):
        """
        Plots the confusion matrix for multi-class classification.

        Parameters
        ----------
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to 'Confusion Matrix'.
            - show : bool, optional
                Whether to show the plot. Defaults to True.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the confusion matrix.
        """
        y_true, y_pred = self._retrieve_test_output_data()
        class_names = self._retrieve_class_names()
        y_true = np.argmax(y_true, axis=1)
        y_pred = np.argmax(y_pred, axis=1)
        fig = plot_confusion_matrix(y_true, y_pred, class_names)
        return fig

    def plot_images(self, grid_size=(2, 2), **general_plot_kwargs):
        """
        Plots a grid of images from a TensorFlow dataset.

        Parameters
        ----------
        grid_size : tuple, optional
            Tuple specifying the grid size as (rows, columns).
            Defaults to (2, 2).
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to 'Images'.
            - show : bool, optional
                Whether to show the plot. Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the images.
        """

        def label_to_title_func(label):
            label = reverse_one_hot(label)
            name = self.label_manager.get_class(label)
            return name

        return super().plot_images(
            grid_size, label_to_title_func, **general_plot_kwargs
        )

    @plot_decorator(default_title="Results", default_show=False)
    def plot_results(self, grid_size=(2, 2), prediction_bar=False):
        """
        Plots a grid of images with their true and predicted labels.

        If the `prediction_bar` parameter is set to True, it also shows a
        bar plot with the predicted probabilities.

        Parameters
        ----------
        grid_size : tuple, optional
            Tuple specifying the grid size as (rows, columns).
            Defaults to (2, 2).
        prediction_bar : bool, optional
            Whether to show the predicted probabilities as a bar plot.
            Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the images and labels.
        """
        data = self._retrieve_test_input_output_data()
        x, y_true, y_pred = data
        class_names = self._retrieve_class_names()
        x = self._to_numpy_array(x)
        return plot_multi_class_classification_results(
            x, y_true, y_pred, class_names, grid_size, prediction_bar
        )
