import tensorflow as tf

from imlresearch.src.data_handling.manipulation.shuffle_dataset import (
    shuffle_dataset,
)


def _shapes_are_known(dataset):
    """
    Checks if all shapes in a dataset are known.

    Parameters
    ----------
    dataset : tf.data.Dataset
        The dataset to check.

    Returns
    -------
    bool
        True if all shapes are known, False otherwise.
    """
    if isinstance(dataset.element_spec, tuple):
        shapes_known = all(
            element.shape is not None for element in dataset.element_spec
        )
    else:
        shapes_known = dataset.element_spec.shape is not None
    return shapes_known


def _restore_dataset_shape(dataset):
    """
    Restores the static shape of a dataset with 'unknown' shape by iterating
    over its elements and rebuilding it with the correct static shape.

    Parameters
    ----------
    dataset : tf.data.Dataset
        The dataset to restore shape for.

    Returns
    -------
    tf.data.Dataset
        A dataset with restored static shapes.
    """
    elements = list(dataset.as_numpy_iterator())

    if isinstance(elements[0], tuple) and len(elements[0]) == 2:
        features, labels = zip(*elements)
        restored_dataset = tf.data.Dataset.from_tensor_slices(
            (list(features), list(labels))
        )
    else:
        restored_dataset = tf.data.Dataset.from_tensor_slices(elements)

    return restored_dataset


def prepare_dataset(
    dataset,
    batch_size=None,
    shuffle_seed=None,
    prefetch_buffer_size=tf.data.experimental.AUTOTUNE,
    repeat_num=None,
):
    """
    Prepares a TensorFlow dataset by applying shuffling, batching, prefetching,
    and repeating a number of times.

    Parameters
    ----------
    dataset : tf.data.Dataset
        The initial TensorFlow dataset to enhance.
    batch_size : int, optional
        Size of batches of data. If None (default), no batching is applied.
    shuffle_seed : int, optional
        Seed for random shuffling. If None (defualt), no shuffling is applied.
    prefetch_buffer_size : int, optional
        Number of batches to prefetch.
        (default is tf.data.experimental.AUTOTUNE).
    repeat_num : int, optional
        Number of times to repeat the dataset. If None (default), no repeating
        is applied.

    Returns
    -------
    tf.data.Dataset
        The prepared TensorFlow dataset.
    """
    if shuffle_seed:
        try:
            # Shuffling automatically restores the dataset shape as well
            dataset = shuffle_dataset(dataset, random_seed=shuffle_seed)
        except ValueError as e:
            msg = "Shuffling requires a dataset with a rectangular shape."
            raise ValueError(msg) from e
    # TODO: Make a test method for this
    elif not _shapes_are_known(dataset):
        try:
            dataset = _restore_dataset_shape(dataset)
        except ValueError:  # dataset might be not a rectangular sequence
            pass

    if batch_size is not None:
        dataset = dataset.batch(batch_size)

    if prefetch_buffer_size is not None:
        dataset = dataset.prefetch(buffer_size=prefetch_buffer_size)

    if repeat_num is not None:
        dataset = dataset.repeat(repeat_num)

    return dataset
