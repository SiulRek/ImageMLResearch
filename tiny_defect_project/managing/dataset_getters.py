from src.data_handling.io.create_dataset import create_dataset
from tiny_defect_project.managing.categories import CATEGORY_NAMES
from tiny_defect_project.managing.get_dataframe import get_dataframe


def get_dataset():
    """
    Gets the Tiny Defect dataset.

    Returns:
        - dataset (pandas.DataFrame): The Tiny Defect dataset.
    """
    df = get_dataframe()
    df = df.rename(columns={"category_code": "label"})
    return create_dataset(
        df, class_names=CATEGORY_NAMES, label_type="multi_class"
    )


if __name__ == "__main__":
    dataset = get_dataset()
    for sample in dataset:
        print(sample)
        break