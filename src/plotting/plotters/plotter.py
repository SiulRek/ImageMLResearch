import matplotlib.pyplot as plt

from src.plotting.functions.plot_images import plot_images
from src.plotting.functions.plot_text import plot_text
from src.plotting.functions.plot_training_history import plot_training_history
from src.research.attributes.research_attributes import ResearchAttributes


def generate_unique_key_name(name, keys):
    name = name.lower().replace(" ", "_")
    if name not in keys:
        return name
    i = 1
    while f"{name}_{i}" in keys:
        i += 1
    return f"{name}_{i}"


def plot_decorator(default_title, default_show):
    """ Decorator for all plotting functions. It adds a title to the plot and saves
    the figure in the plotter. """

    def decorator(plot_func):
        def wrapper(self, *args, **kwargs):
            title = kwargs.pop("title", default_title)
            show = kwargs.pop("show", default_show)

            fig = plot_func(self, *args, **kwargs)
            fig.subplots_adjust(top=0.90)
            fig.suptitle(title, fontsize=18, fontweight="bold")

            name = title.lower().replace(" ", "_")
            self._add_figure(name, fig)
            if show:
                plt.show()
            return fig

        return wrapper

    return decorator


class Plotter(ResearchAttributes):
    """ A class for plotting images and text using research attributes. """

    def __init__(self):
        """ Initializes the Plotter. """
        self._datasets_container = None
        self._figures = {}  # Name: Figure
        self._outputs_container = (
            None  # Model outputs (y_true, y_pred) are stored here, when available.
        )
        self._training_history = {}

    def _add_figure(self, name, fig):
        """
        Adds a figure to the plotter.

        Args:
            - name: The name of the figure.
            - fig: The figure to be added.
        """
        if not isinstance(fig, plt.Figure):
            msg = "The figure must be an instance of matplotlib.pyplot.Figure."
            raise ValueError(msg)
        name = generate_unique_key_name(name, self._figures.keys())
        self._figures[name] = fig

    @plot_decorator(default_title="Images", default_show=False)
    def plot_images(
        self, grid_size=(2, 2), label_to_title_func=None, **general_plot_kwargs
    ):
        """
        Plots images from the complete dataset.

        Args:
            - grid_size: Tuple containing the grid size (rows, columns).
                Defaults to (2, 2).
            - label_to_title_func: Function to convert the label to a
                string. Defaults to None.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to "Images".
            - show: Whether to show the plot. Defaults to False.

        Returns:
            - The figure containing the images.
        """
        dataset = self._datasets_container.get(
            "complete_dataset"
        ) or self._datasets_container.get("train_dataset")
        if not dataset:
            msg = "Neither 'complete_dataset' nor 'train_dataset' found in dataset container."
            raise ValueError(msg)
        return plot_images(dataset, grid_size, label_to_title_func)

    @plot_decorator(default_title="Text", default_show=False)
    def plot_text(self, text, **general_plot_kwargs):
        """
        Plots the given text.

        Args:
            - text: The text to be plotted.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to 'Text'.
            - show: Whether to show the plot. Defaults to False.

        Returns:
            - The figure containing the text.
        """
        return plot_text(text)

    def _retrieve_output_data(self):
        """
        Retrieves the output required for various plots.

        Returns:
            - (Tuple): (y_true, y_pred, class_names)
        """
        def get_labels(name):
            try:
                return self._outputs_container[name]
            except AttributeError as e:
                msg = f"No {name} found in the outputs container."
                raise ValueError(msg) from e

        y_true = get_labels("y_true")
        y_pred = get_labels("y_pred")

        try:
            class_names = self.label_manager.class_names
        except AttributeError:
            class_names = None
        return y_true, y_pred, class_names

    @plot_decorator(default_title="Training History", default_show=False)
    def plot_training_history(self, **general_plot_kwargs):
        """
        Plots the training history of the model.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to "Training
                History".
            - show: Whether to show the plot. Defaults to False.

        Returns:
            - The figure containing the training history.
        """
        if not self._training_history:
            msg = "No training history found to plot."
            raise ValueError(msg)
        return plot_training_history(self._training_history)