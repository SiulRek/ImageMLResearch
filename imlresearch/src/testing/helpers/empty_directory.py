import os
import shutil


def empty_directory(directory):
    """
    Empty the contents of the specified directory.

    Parameters
    ----------
    directory : str
        The path to the directory to be emptied.
    """
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
