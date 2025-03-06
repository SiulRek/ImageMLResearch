import numpy as np
import tensorflow as tf


def shuffle_dataset(dataset, random_seed=42):
    """
    Shuffles the given dataset using the specified random seed.

    Parameters
    ----------
    dataset : tf.data.Dataset
        The dataset to be shuffled.
    random_seed : int, optional
        The random seed for shuffling. Default is 42.

    Returns
    -------
    tf.data.Dataset
        The shuffled dataset.
    """
    elements = list(dataset.as_numpy_iterator())
    indices = np.arange(len(elements))

    np.random.seed(random_seed)
    np.random.shuffle(indices)

    shuffled_elements = [elements[i] for i in indices]

    if isinstance(elements[0], tuple) and len(elements[0]) == 2:
        features, labels = zip(*shuffled_elements)
        dataset = tf.data.Dataset.from_tensor_slices(
            (list(features), list(labels))
        )
    else:
        dataset = tf.data.Dataset.from_tensor_slices(shuffled_elements)

    return dataset
