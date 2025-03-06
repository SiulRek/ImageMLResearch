import os
import numpy as np
import tensorflow as tf

ROOT_DIR = os.path.join(os.path.abspath(__file__), "..", "..", "..", "..")
NP_DATASET_DIR = os.path.join(
    ROOT_DIR, "testing", "image_data", "numpy_datasets"
)


def load_sign_digits_dataset(sample_num=None, labeled=True):
    """
    Load the sign language digits dataset used for testing.

    Parameters
    ----------
    sample_num : int, optional
        Number of samples to load, by default None.
    labeled : bool, optional
        Whether to return the dataset with labels, by default True.

    Returns
    -------
    tf.data.Dataset
        The sign language digits dataset for testing.
    """
    X = np.load(os.path.join(NP_DATASET_DIR, "sign_language_digits_X.npy"))
    Y = np.load(os.path.join(NP_DATASET_DIR, "sign_language_digits_Y.npy"))

    if sample_num:
        X, Y = X[:sample_num], Y[:sample_num]

    return tf.data.Dataset.from_tensor_slices((X, Y)) if labeled else \
        tf.data.Dataset.from_tensor_slices(X)
