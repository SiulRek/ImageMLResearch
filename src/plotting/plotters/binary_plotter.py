from src.plotting.functions.plot_confusion_matrix import plot_confusion_matrix
from src.plotting.plotters.plotter import Plotter, plot_decorator


class BinaryPlotter(Plotter):
    """ A class for plotting images and text using research attributes. """

    @plot_decorator(default_title="Confusion Matrix", default_show=True)
    def plot_confusion_matrix(self, **general_plot_kwargs):
        """
        Plots the confusion matrix for binary classification.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to 'Confusion
                Matrix'.
            - show: Whether to show the plot. Defaults to True.

        Returns:
            - The figure containing the confusion matrix.
        """
        y_true, y_pred, class_names = self._retrieve_output_data()
        fig = plot_confusion_matrix(y_true, y_pred, class_names)
        return fig
