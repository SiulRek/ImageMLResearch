import pandas as pd

from src.data_handling.io.create_dataset import create_dataset
from tiny_defect_project.managing.categories import CATEGORY_NAMES
from tiny_defect_project.managing.get_dataframe import (
    get_dataframe,
    get_paths_by_defect_name,
)


def get_dataset():
    """
    Gets the Tiny Defect dataset.

    Returns:
        - dataset (pandas.DataFrame): The Tiny Defect dataset.
    """
    df = get_dataframe()
    df = df.rename(columns={"category_code": "label"})
    return create_dataset(df, class_names=CATEGORY_NAMES, label_type="multi_class")


def get_binary_dataset(defect_name):
    """
    Retrieves a binary balanced dataset consisting of defect and no_defect images.

    Args:
        defect_name (str): The name of the defect.

    Returns:
        dataset (tf.data.Dataset): The binary dataset containing defect and no_defect images.
    """
    defect_paths = get_paths_by_defect_name(defect_name)
    no_defect_paths = get_paths_by_defect_name("no_defect")
    # As the number of defect paths is greater than the number of no defect
    # paths we repeat to create a balanced dataset and apply data augmentation
    # later.
    no_defect_paths = no_defect_paths * round(len(defect_paths) / len(no_defect_paths))
    defect_labels = ["defect"] * len(defect_paths)
    no_defect_labels = ["no_defect"] * len(no_defect_paths)
    dataset = {
        "path": defect_paths + no_defect_paths,
        "label": defect_labels + no_defect_labels,
    }
    df = pd.DataFrame(dataset)
    return create_dataset(df, class_names=["defect", "no_defect"], label_type="binary")
