import os


def map_figures_to_paths(figures, directory):
    """
    Converts the key-figure pairs to key-path pairs and saves the figures. It
    does not modify the input dictionary, instead it creates a new one.

    Args:
        - figures (dict): The dictionary of figures.
        - directory (str): The directory to save the figures.

    Returns:
        - dict: The dictionary of file paths for the figures.
    """
    figure_paths = {}
    for name, figure in figures.items():
        figure_path = os.path.join(directory, f"{name}.png")
        figure_paths[name] = figure_path
        figure.savefig(figure_path)
    return figure_paths
