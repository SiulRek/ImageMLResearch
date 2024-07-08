import matplotlib.pyplot as plt
import tensorflow as tf

from src.plotting.functions.plot_images import plot_images
from src.plotting.functions.plot_model_summary import plot_model_summary
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
        super().__init__()

        # Initialize research attributes used in the Plotter
        self._datasets_container = None  # Read only
        self._figures = {
            # Name: Figure
        }  # Read only
        self._outputs_container = None  # Model outputs (y_true, y_pred) are stored here, when available.  # Read only
        self._training_history = {}  # Read only
        self._model = None  # Read only

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

    @plot_decorator(default_title="Model Summary", default_show=False)
    def plot_model_summary(self, **general_plot_kwargs):
        """
        Plots the summary of the given model.

        General plot keyword arguments:
            - title: Optional title for the plot. Defaults to "Model
                Summary".
            - show: Whether to show the plot. Defaults to False.

        Returns:
            - The figure containing the model summary.
        """
        if not self._model:
            msg = "No model found to plot."
            raise ValueError(msg)
        return plot_model_summary(self._model)

    def _retrieve_output_data(self, output_name=None):
        """
        Retrieves the output required for various plots.

        Args:
            - output_name (optional): The name of the output to retrieve.
                Defaults to None, than the output is retrieved from either
                'complete_output' or 'test_output' from the ´output_container´.

        Returns:
            - (Tuple): (y_true, y_pred, class_names)
        """
        if output_name is not None:
            output = self._outputs_container.get(output_name)
        else:
            complete_output = self._outputs_container.get("complete_output")
            test_output = self._outputs_container.get("test_output")
            output = complete_output or test_output
        if output is None:
            msg = "No output data found to plot."
            raise ValueError(msg)
        y_true = output[0]
        y_pred = output[1]

        try:
            class_names = self.label_manager.class_names
        except AttributeError:
            class_names = None
        return y_true, y_pred, class_names

    def _get_inputs(self, dataset):
        """
        Retrieves the input data from the dataset.

        Args:
            - dataset: The dataset from which to retrieve the input data.

        Returns:
            - The input data.
        """
        try:
            dataset = dataset.unbatch()
        except (AttributeError, ValueError):
            pass
        inputs_list = []
        for inputs, _ in dataset:
            inputs_list.append(tf.expand_dims(inputs, axis=0))
        inputs_tensor = tf.concat(inputs_list, axis=0)
        return inputs_tensor

    def _retrieve_input_output_data(self):
        """
        Retrieves the input and output data required for various plots.

        Returns:
            - (Tuple): (x, y_true, y_pred, class_names)
        """
        for dataset_name in ["complete_dataset", "test_dataset"]:
            if (
                dataset_name in self._datasets_container
                and self._datasets_container[dataset_name]
            ):
                output_name = dataset_name.replace("dataset", "output")
                if output_name in self._outputs_container:
                    dataset = self._datasets_container[dataset_name]
                    break
        else:
            msg = "No dataset synced with outputs found to plot. Probably due"
            msg += "to two reasons: 1. Neither 'complete_dataset' nor"
            msg += "'train_dataset' found in datasets container. 2. No output"
            msg += "data synced with the dataset found in outputs container."
            raise ValueError(msg)
        x = self._get_inputs(dataset)
        y_true, y_pred, class_names = self._retrieve_output_data(output_name)

        return x, y_true, y_pred, class_names

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
