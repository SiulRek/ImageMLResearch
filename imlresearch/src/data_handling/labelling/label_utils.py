import numpy as np
import tensorflow as tf


def reverse_one_hot(label):
    """
    Converts a one-hot encoded label to its corresponding class index.

    Parameters
    ----------
    label : tf.Tensor or array-like
        The one-hot encoded label to convert.

    Returns
    -------
    int
        The index corresponding to the highest value in the label.
    """
    if isinstance(label, tf.Tensor):
        label = label.numpy()
    else:
        label = np.array(label)
    if isinstance(label, np.ndarray):
        label = np.argmax(label)
    return label
