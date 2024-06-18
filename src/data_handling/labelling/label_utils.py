import numpy as np
import tensorflow as tf


def reverse_one_hot(label):
    """
    Converts a label to a NumPy digit.

    Args:
        - label: The label to convert.

    Returns:
        - int: The digit corresponding to the label.
    """
    if isinstance(label, tf.Tensor):
        label = label.numpy()
    else:
        label = np.array(label)
    if isinstance(label, np.ndarray):
        label = np.argmax(label)
    return label
