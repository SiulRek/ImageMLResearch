def unpack_dataset(tf_dataset):
    """
    Unpacks a `tf.data.Dataset` into two separate datasets: one for images
    and another for labels.

    Parameters
    ----------
    tf_dataset : tf.data.Dataset
        A `tf.data.Dataset` object containing tuples of (image, label), where
        'image' is the decoded image tensor and 'label' is an integer label.

    Returns
    -------
    image_dataset : tf.data.Dataset
        A dataset containing only image tensors.
    label_dataset : tf.data.Dataset
        A dataset containing only label tensors.
    """
    image_dataset = tf_dataset.map(lambda image, label: image)
    label_dataset = tf_dataset.map(lambda image, label: label)
    return image_dataset, label_dataset
