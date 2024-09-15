from copy import deepcopy
import os
import xml.etree.ElementTree as ET

import pandas as pd

from tiny_defect_project.managing.categories import Category

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..", "..")
DATA_DIR = os.path.join(ROOT_DIR, "tiny_defect_project/data")
ANNO_DIR = os.path.join(DATA_DIR, "Annotations")
IMGS_DIR = os.path.join(DATA_DIR, "images")
PCB_USED_DIR = os.path.join(DATA_DIR, "PCB_USED")
ANNO_SUMMARY_FILE = os.path.join(DATA_DIR, "Annotations/annotation_summary.csv")

EMPTY_DATADICT = {
    "class": [],
    "xmin": [],
    "ymin": [],
    "xmax": [],
    "ymax": [],
    "file": [],
    "defect_x_center": [],  # Relative to image_width.
    "defect_y_center": [],  # Relative to image_heigth.
    "defect_width": [],
    "defect_height": [],
    "image_width": [],
    "image_height": [],
    "width_ratio": [],  # Defect width/Image width.
    "height_ratio": [],  # Defect heigth/Image heigth.
    "path": [],
    "category_code": [],
}


def _standardize_path(path):
    """
    Normalizes and computes the relative path of a file.

    Args:
        - path (str): The path to the file.

    Returns:
        - path (str): The normalized path to the file.
    """
    path = os.path.normpath(path)
    path = os.path.relpath(path, ROOT_DIR)
    return path


def _create_annotation_summary():
    """
    Creates the summary of annotations derived from XML files of the Tiny Defect
    dataset and saves it as a CSV file.

    Returns:
        - dataframe (pandas.DataFrame): The summary of annotations as a
            pandas DataFrame.
    """
    dataset = deepcopy(EMPTY_DATADICT)

    all_files = []  # Stores the path to all files

    for path, _, files in os.walk(ANNO_DIR):
        for name in files:
            if not name.endswith(".csv"):
                normalized_path = os.path.normpath(path)
                rel_path = os.path.relpath(normalized_path, ROOT_DIR)
                all_files.append(os.path.join(rel_path, name))

    for anno in all_files:
        tree = ET.parse(anno)
        cnt = 0
        for elem in tree.iter():
            if "size" in elem.tag:
                for attr in list(elem):
                    if "width" in attr.tag:
                        image_width = int(round(float(attr.text)))
                    if "height" in attr.tag:
                        image_height = int(round(float(attr.text)))

            if "object" in elem.tag:
                cnt += 1
                for attr in list(elem):
                    if "name" in attr.tag:
                        name = attr.text
                        dataset["class"].append(name)

                        if name == "missing_hole":
                            dataset["category_code"].append(Category.MISSING_HOLE.value)
                        elif name == "mouse_bite":
                            dataset["category_code"].append(Category.MOUSE_BITE.value)
                        elif name == "open_circuit":
                            dataset["category_code"].append(Category.OPEN_CIRCUIT.value)
                        elif name == "short":
                            dataset["category_code"].append(Category.SHORT.value)
                        elif name == "spur":
                            dataset["category_code"].append(Category.SPUR.value)
                        elif name == "spurious_copper":
                            dataset["category_code"].append(
                                Category.SPURIOUS_COPPER.value
                            )

                        dataset["image_width"].append(image_width)
                        dataset["image_height"].append(image_height)
                        dataset["file"].append(anno.split("/")[-1][0:-4])

                    if "bndbox" in attr.tag:
                        xmin, ymin, xmax, ymax = -1, -1, -1, -1
                        for dim in list(attr):
                            if "xmin" in dim.tag:
                                xmin = int(round(float(dim.text)))
                                dataset["xmin"].append(xmin)
                            if "ymin" in dim.tag:
                                ymin = int(round(float(dim.text)))
                                dataset["ymin"].append(ymin)
                            if "xmax" in dim.tag:
                                xmax = int(round(float(dim.text)))
                                dataset["xmax"].append(xmax)
                            if "ymax" in dim.tag:
                                ymax = int(round(float(dim.text)))
                                dataset["ymax"].append(ymax)

                        width = xmax - xmin
                        height = ymax - ymin
                        dataset["defect_width"].append(width)
                        dataset["defect_height"].append(height)
                        dataset["defect_x_center"].append(
                            ((xmin + width) + xmin) / 2 / image_width
                        )
                        dataset["defect_y_center"].append(
                            ((ymin + height) + ymin) / 2 / image_height
                        )
                        dataset["width_ratio"].append(width / image_width)
                        dataset["height_ratio"].append(height / image_height)

                image_path = tree.find("path").text
                dataset["path"].append(_standardize_path(image_path))

    dataframe = pd.DataFrame(dataset)
    anno_summary_file = _standardize_path(ANNO_SUMMARY_FILE)
    dataframe.to_csv(anno_summary_file, sep=";")

    return dataframe


def get_dataframe():
    """
    Returns the dataframe containing the summary of annotations of the Tiny
    Defect dataset.

    Returns:
        - dataframe (pandas.DataFrame): The summary of annotations as a
            pandas DataFrame.
    """
    anno_summary_file = _standardize_path(ANNO_SUMMARY_FILE)
    if not os.path.exists(anno_summary_file):
        return _create_annotation_summary()

    return pd.read_csv(anno_summary_file, sep=";")


def _get_no_defects_paths():
    """
    Returns the paths of images with no defects.

    Returns:
        - paths (list): The paths of images with no defects.
    """
    paths = []
    for name in os.listdir(PCB_USED_DIR):
        if name.endswith(".JPG"):
            path = os.path.join(PCB_USED_DIR, name)
            path = _standardize_path(path)
            paths.append(path)
    return paths


def get_paths_by_defect_name(defect_name):
    """
    Retrieves a list of file paths associated with a specific defect name.

    Parameters:
        - defect_name (str): The name of the defect defined in
            CATEGORIES_NAMES or can be also 'no_defect'.

    Returns:
        - list: A list of file paths associated with the specified defect
            name.
    """
    if defect_name == "no_defect":
        return _get_no_defects_paths()
    df = get_dataframe()
    missing_hole_df = df[df["category_code"] == defect_name]
    paths = missing_hole_df["path"].tolist()
    return list(set(paths))
