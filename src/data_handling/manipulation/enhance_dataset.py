import tensorflow as tf

from src.data_handling.manipulation.shuffle_dataset import shuffle_dataset


def enhance_dataset(
    dataset,
    batch_size=None,
    shuffle=False,
    random_seed=None,
    prefetch_buffer_size=tf.data.experimental.AUTOTUNE,
    repeat_num=None,
):
    """
    Enhances a TensorFlow dataset by applying shuffling, batching, prefetching,
    and optionally repeating a specified number of times or indefinitely if
    repeat_num is None and the repeat parameter is set to True.

    Args:
        - dataset (tf.data.Dataset): The initial TensorFlow dataset to
            enhance.
        - batch_size (int, optional): Size of batches of data.
        - shuffle (bool, optional): Whether to shuffle the dataset. Default
            is False.
        - random_seed (int, optional): Seed for random shuffling if shuffle
            is True.
        - prefetch_buffer_size (int, optional): Number of batches to
            prefetch (default is tf.data.experimental.AUTOTUNE).
        - repeat_num (int, optional): Number of times to repeat the dataset.
            None for indefinite repeat.

    Returns:
        - tf.data.Dataset: The enhanced TensorFlow dataset.
    """
    if shuffle:
        dataset = shuffle_dataset(dataset, random_seed=random_seed)

    if batch_size:
        dataset = dataset.batch(batch_size)

    dataset = dataset.prefetch(buffer_size=prefetch_buffer_size)

    if repeat_num is not None:
        dataset = dataset.repeat(repeat_num)

    return dataset
