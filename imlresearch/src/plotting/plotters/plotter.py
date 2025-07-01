import matplotlib.pyplot as plt

from imlresearch.src.plotting.functions.plot_images import plot_images
from imlresearch.src.plotting.functions.plot_model_summary import (
    plot_model_summary,
)
from imlresearch.src.plotting.functions.plot_text import plot_text
from imlresearch.src.plotting.functions.plot_training_history import (
    plot_training_history,
)
from imlresearch.src.research.helpers.data_retriever import DataRetriever


def generate_unique_key_name(name, keys):
    """
    Generates a unique key name by appending a numeric suffix if necessary.

    Parameters
    ----------
    name : str
        The base name to be used as a key.
    keys : set
        Existing keys to ensure uniqueness.

    Returns
    -------
    str
        A unique key name.
    """
    name = name.lower().replace(" ", "_")
    if name not in keys:
        return name
    i = 1
    while f"{name}_{i}" in keys:
        i += 1
    return f"{name}_{i}"


def plot_decorator(default_title, default_show):
    """
    Decorator for all plotting functions.

    Adds a title to the plot and saves the figure in the plotter.

    Parameters
    ----------
    default_title : str
        Default title for the plot.
    default_show : bool
        Whether to show the plot by default.

    Returns
    -------
    function
        Decorated plotting function.
    """

    def decorator(plot_func):
        def wrapper(self, *args, **kwargs):
            title = kwargs.pop("title", default_title)
            show = kwargs.pop("show", default_show)

            fig = plot_func(self, *args, **kwargs)

            if not isinstance(fig, plt.Figure):
                msg = (
                    "The plot function must return a "
                    "matplotlib.pyplot.Figure."
                )
                raise ValueError(msg)

            fig.subplots_adjust(top=0.90)
            fig.suptitle(title, fontsize=18, fontweight="bold")

            name = title.lower().replace(" ", "_")
            self._add_figure(name, fig)
            if show:
                plt.show()
            else:
                plt.close(fig)
            return fig

        return wrapper

    return decorator


class Plotter(DataRetriever):
    """
    A class for plotting images and text using research attributes.
    """

    def __init__(self):
        """
        Initializes the Plotter.
        """
        # Not initializing ResearchAttributes here, prefer calling
        # synchronize_research_attributes explicitly.

        # Initialize research attributes used in the Plotter
        self._datasets_container = {}
        self._figures = {}
        self._outputs_container = {}
        self._training_history = {}
        self._model = None

    def _add_figure(self, name, fig):
        """
        Adds a figure to the plotter.

        Parameters
        ----------
        name : str
            The name of the figure.
        fig : matplotlib.figure.Figure
            The figure to be added.
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
        Plots images from the complete dataset. If dataset is bigger than
        the grid size, a random skip value is determined to avoid plotting
        the same images every time.

        Parameters
        ----------
        grid_size : tuple, optional
            Tuple specifying the grid size as (rows, columns).
            Defaults to (2, 2).
        label_to_title_func : callable, optional
            Function to convert the label to a string. Defaults to None.
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to "Images".
            - show : bool, optional
                Whether to show the plot. Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the images.
        """
        dataset = self._datasets_container.get("complete_dataset") or \
                  self._datasets_container.get("train_dataset")
        if not dataset:
            msg = (
                "Neither 'complete_dataset' nor 'train_dataset' "
                "found in dataset container."
            )
            raise ValueError(msg)
        return plot_images(dataset, grid_size, label_to_title_func)

    @plot_decorator(default_title="Text", default_show=False)
    def plot_text(self, text, **general_plot_kwargs):
        """
        Plots the given text.

        Parameters
        ----------
        text : str
            The text to be plotted.
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to 'Text'.
            - show : bool, optional
                Whether to show the plot. Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the text.
        """
        return plot_text(text)

    @plot_decorator(default_title="Model Summary", default_show=False)
    def plot_model_summary(self, **general_plot_kwargs):
        """
        Plots the summary of the given model.

        Parameters
        ----------
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot. Defaults to "Model Summary".
            - show : bool, optional
                Whether to show the plot. Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the model summary.
        """
        if not self._model:
            msg = "No model found to plot."
            raise ValueError(msg)
        return plot_model_summary(self._model)

    @plot_decorator(default_title="Training History", default_show=False)
    def plot_training_history(self, **general_plot_kwargs):
        """
        Plots the training history of the model.

        Parameters
        ----------
        **general_plot_kwargs : dict, optional
            General plot keyword arguments.
            - title : str, optional
                Optional title for the plot.
            - show : bool, optional
                Whether to show the plot. Defaults to False.

        Returns
        -------
        matplotlib.figure.Figure
            The figure containing the training history.
        """
        if not self._training_history:
            msg = "No training history found to plot."
            raise ValueError(msg)
        return plot_training_history(self._training_history)
