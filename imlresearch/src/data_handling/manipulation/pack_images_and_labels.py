import tensorflow as tf


def pack_images_and_labels(image_dataset, label_dataset):
    """
    Combines two `tf.data.Dataset` objects—one for images and one for labels—
    into a single `tf.data.Dataset`.

    Parameters
    ----------
    image_dataset : tf.data.Dataset
        A dataset containing image tensors.
    label_dataset : tf.data.Dataset
        A dataset containing label tensors.

    Returns
    -------
    tf.data.Dataset
        A dataset containing tuples of (image, label).
    """
    return tf.data.Dataset.zip((image_dataset, label_dataset))
