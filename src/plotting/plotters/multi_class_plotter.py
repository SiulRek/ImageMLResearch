import numpy as np

from src.data_handling.labelling.label_utils import reverse_one_hot
from src.plotting.functions.plot_confusion_matrix import plot_confusion_matrix
from src.plotting.plotters.plotter import Plotter, plot_decorator


class MultiClassPlotter(Plotter):
    """ A class for plotting images and text using research attributes for
    multi-class classification. """

    @plot_decorator(default_title="Confusion Matrix", default_show=True)
    def plot_confusion_matrix(self, **general_plot_kwargs):
        """
        Plots the confusion matrix for multi-class classification.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to 'Confusion
                Matrix'.
            - show: Whether to show the plot. Defaults to True.

        Returns:
            - The figure containing the confusion matrix.
        """
        y_true, y_pred, class_names = self._retrieve_output_data()
        y_true = np.argmax(y_true, axis=1)
        y_pred = np.argmax(y_pred, axis=1)
        fig = plot_confusion_matrix(y_true, y_pred, class_names)
        return fig

    def plot_images(self, grid_size=(2, 2)):
        """
        Plots a grid of images from a TensorFlow dataset.

        Args:
            - grid_size (Tuple): Tuple containing the grid size (rows,
                columns). Defaults to (2, 2).

        Returns:
            - The figure containing the images.
        """
        def label_to_title_func(label):
            label = reverse_one_hot(label)
            name = self.label_manager.get_class(label)
            return name
        
        return super().plot_images(grid_size, label_to_title_func)