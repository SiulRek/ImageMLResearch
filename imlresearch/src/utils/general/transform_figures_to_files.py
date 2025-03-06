import os

import matplotlib.pyplot as plt


def transform_figures_to_files(figures, directory, close_figures=True):
    """
    Save figures to a specified directory and return a dictionary of file paths.

    This function does not modify the input dictionary but creates a new one.
    After saving, figures are closed if `close_figures` is True.

    Parameters
    ----------
    figures : dict
        Dictionary mapping names to Matplotlib figures.
    directory : str
        Directory where figures will be saved.
    close_figures : bool, optional
        Whether to close figures after saving, by default True.

    Returns
    -------
    dict
        Dictionary mapping figure names to saved file paths.
    """
    figure_paths = {}

    for name, figure in figures.items():
        figure_path = os.path.join(directory, f"{name}.png")
        figure_paths[name] = figure_path
        figure.savefig(figure_path)

        if close_figures:
            plt.close(figure)
            del figure

    return figure_paths
