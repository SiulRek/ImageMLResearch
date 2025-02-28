import os

import matplotlib.pyplot as plt


def transform_figures_to_files(figures, directory, close_figures=True):
    """
    Transforms the key-figure pairs to key-path pairs. It does not modify the
    input dictionary, instead it creates a new one. After saving the figures, it
    closes them if close_figures is set to True.

    Args:
        - figures (dict): The dictionary of figures.
        - directory (str): The directory to save the figures.
        - close_figures (bool, optional): Whether to close the figures after
            saving them. Defaults to True.

    Returns:
        - dict: The dictionary of file paths for the figures.
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
