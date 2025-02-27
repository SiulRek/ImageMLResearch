import tensorflow as tf


def is_batched(dataset):
    """
    Checks if the dataset is batched. Expects a dataset of type tf.data.Dataset
    and assumes that each sample in the dataset is either an image or a tuple
    containing an image and its corresponding label. The images are expected to
    have 3 dimensions.

    Args:
        - dataset (tf.data.Dataset): Dataset to check.

    Returns:
        - bool: Whether the dataset is batched.
    """
    if not isinstance(dataset, tf.data.Dataset):
        msg = "The input dataset must be a tf.data.Dataset object."
        raise ValueError(msg)
    for sample in dataset.take(1):
        if isinstance(sample, tuple):
            image, _ = sample
        else:
            image = sample
    return image.shape.ndims == 4


def unbatch_dataset_if_batched(dataset):
    """
    Unbatches the dataset if it is batched. Expects a dataset of type
    tf.data.Dataset and assumes that each sample in the dataset is either an
    image or a tuple containing an image and its corresponding label. The images
    are expected to have 3 dimensions.

    Args:
        - dataset (tf.data.Dataset): Dataset to unbatch.

    Returns:
        - tf.data.Dataset: Unbatched dataset.
    """
    batched = is_batched(dataset)
    if not batched:
        return dataset
    return dataset.unbatch()
