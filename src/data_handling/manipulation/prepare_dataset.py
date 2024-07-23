import tensorflow as tf

from src.data_handling.manipulation.shuffle_dataset import shuffle_dataset


def prepare_dataset(
    dataset,
    batch_size=None,
    shuffle_seed=None,
    prefetch_buffer_size=tf.data.experimental.AUTOTUNE,
    repeat_num=None,
):
    """
    Prepares a TensorFlow dataset by applying shuffling, batching, prefetching,
    and repeating a number of times. If a parameter is None, the corresponding
    operation is not applied.

    Args:
        - dataset (tf.data.Dataset): The initial TensorFlow dataset to
            enhance.
        - batch_size (int, optional): Size of batches of data.
        - shuffle_seed (int, optional): Seed for random shuffling.
        - prefetch_buffer_size (int, optional): Number of batches to
            prefetch (default is tf.data.experimental.AUTOTUNE).
        - repeat_num (int, optional): Number of times to repeat the dataset.

    Returns:
        - tf.data.Dataset: The prepared TensorFlow dataset.
    """
    if shuffle_seed is not None:
        dataset = shuffle_dataset(dataset, random_seed=shuffle_seed)

    if batch_size is not None:
        dataset = dataset.batch(batch_size)

    if prefetch_buffer_size is not None:
        dataset = dataset.prefetch(buffer_size=prefetch_buffer_size)

    if repeat_num is not None:
        dataset = dataset.repeat(repeat_num)

    return dataset
