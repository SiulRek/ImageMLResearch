import numpy as np

from imlresearch.src.plotting.functions.plot_confusion_matrix import (
    plot_confusion_matrix,
)
from imlresearch.src.plotting.functions.plot_pr_curve import plot_pr_curve
from imlresearch.src.plotting.functions.plot_roc_curve import plot_roc_curve
from imlresearch.src.plotting.plotters.plotter import Plotter, plot_decorator


class BinaryPlotter(Plotter):
    """
    A class for plotting images and text using research attributes.
    """

    def plot_images(self, grid_size=(2, 2)):
        """
        Plots a grid of images from a TensorFlow dataset.

        Parameters
        ----------
        grid_size : tuple, optional
            Tuple specifying the grid size as (rows, columns). Defaults
            to (2, 2).

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the images.
        """
        label_to_title_func = self.label_manager.get_class
        return super().plot_images(grid_size, label_to_title_func)

    @plot_decorator(default_title="Confusion Matrix", default_show=False)
    def plot_confusion_matrix(self, **general_plot_kwargs):
        """
        Plots the confusion matrix for binary classification.

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
        y_pred_rounded = [np.round(pred) for pred in y_pred]
        fig = plot_confusion_matrix(y_true, y_pred_rounded, class_names)
        return fig

    @plot_decorator(default_title="ROC Curve", default_show=False)
    def plot_roc_curve(self, **general_plot_kwargs):
        """
        Plots the ROC curve for binary classification.

        Parameters
        ----------
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to 'ROC Curve'.
            - show : bool, optional
                Whether to show the plot. Defaults to True.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the ROC curve.
        """
        y_true, y_pred = self._retrieve_test_output_data()
        fig = plot_roc_curve(y_true, y_pred)
        return fig

    @plot_decorator(default_title="Precision-Recall Curve", default_show=False)
    def plot_pr_curve(self, **general_plot_kwargs):
        """
        Plots the Precision-Recall curve for binary classification.

        Parameters
        ----------
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to 'PR Curve'.
            - show : bool, optional
                Whether to show the plot. Defaults to True.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the PR curve.
        """
        y_true, y_pred = self._retrieve_test_output_data()
        fig = plot_pr_curve(y_true, y_pred)
        return fig

    @plot_decorator(default_title="Results", default_show=False)
    def plot_results(self, grid_size=(2, 2)):
        """
        Plots the results of a binary classification model.

        Parameters
        ----------
        grid_size : tuple, optional
            Tuple specifying the grid size as (rows, columns).
            Defaults to (2, 2).

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the classification results.
        """
        from imlresearch.src.plotting.functions.plot_results import (
            plot_binary_classification_results,
        )

        data = self._retrieve_test_input_output_data()
        x, y_true, y_pred = data
        class_names = self._retrieve_class_names()
        x = self._to_numpy_array(x)
        fig = plot_binary_classification_results(
            x=x,
            y_true=y_true,
            y_pred=y_pred,
            class_names=class_names,
            grid_size=grid_size,
        )
        return fig
