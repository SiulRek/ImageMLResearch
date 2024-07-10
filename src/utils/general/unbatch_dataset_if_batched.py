import tensorflow as tf


def unbatch_dataset_if_batched(dataset):
    """
    Unbatches the dataset if it is batched. Expects a dataset of type tf.data.Dataset and assumes that each sample in the dataset is either an image or a tuple containing an image and its corresponding label. The images are expected to have 3 dimensions. 

    Args:
        - dataset (tf.data.Dataset): Dataset to unbatch.

    Returns:
        - tf.data.Dataset: Unbatched dataset.
    """
    if not isinstance(dataset, tf.data.Dataset):
        msg = "The input dataset must be a tf.data.Dataset object."
        raise ValueError(msg)
    for sample in dataset.take(1):
        if isinstance(sample, tuple):
            image, _ = sample
        else:
            image = sample
    if (
        image.shape.ndims == 4
    ):  # We expect 3 dimensions for images, so if it's 4, it's batched.
        dataset = dataset.unbatch()
    return dataset
