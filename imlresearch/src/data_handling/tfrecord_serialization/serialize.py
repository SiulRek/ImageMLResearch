import os

import tensorflow as tf

from imlresearch.src.utils import unbatch_dataset_if_batched


def _bytes_feature(value):
    """
    Converts a value to a TensorFlow `Feature` with a bytes_list.

    Parameters
    ----------
    value : bytes or tf.Tensor
        The value to convert to a bytes_list feature.

    Returns
    -------
    tf.train.Feature
        A TensorFlow `Feature` containing a bytes_list.
    """
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy()
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def serialize_sample_for_png(image, label=None):
    """
    Serializes an image and optionally a label pair into a `tf.train.Example`
    protocol buffer. The image is expected to be in PNG format.

    Parameters
    ----------
    image : tf.Tensor
        The image tensor to serialize.
    label : tf.Tensor, optional
        The corresponding label tensor to serialize.

    Returns
    -------
    bytes
        Serialized `tf.train.Example` representation of the sample.
    """
    feature = {"image": _bytes_feature(tf.io.encode_png(image).numpy())}
    if label is not None:
        feature["label"] = _bytes_feature(
            tf.io.serialize_tensor(label).numpy()
        )

    sample_proto = tf.train.Example(
        features=tf.train.Features(feature=feature)
    )
    return sample_proto.SerializeToString()


def serialize_sample_for_jpeg(image, label=None):
    """
    Serializes an image and optionally a label pair into a `tf.train.Example`
    protocol buffer. The image is expected to be in JPEG format.

    Parameters
    ----------
    image : tf.Tensor
        The image tensor to serialize.
    label : tf.Tensor, optional
        The corresponding label tensor to serialize.

    Returns
    -------
    bytes
        Serialized `tf.train.Example` representation of the sample.
    """
    feature = {"image": _bytes_feature(tf.io.encode_jpeg(image).numpy())}
    if label is not None:
        feature["label"] = _bytes_feature(
            tf.io.serialize_tensor(label).numpy()
        )

    sample_proto = tf.train.Example(
        features=tf.train.Features(feature=feature)
    )
    return sample_proto.SerializeToString()


def serialize_dataset_to_tf_record(dataset, filepath, image_format):
    """
    Saves a dataset to a TFRecord file. If the dataset is batched, it will be
    unbatched before saving. Supports labeled datasets, storing image-label
    pairs.

    Parameters
    ----------
    dataset : tf.data.Dataset
        A dataset object containing image and optionally label pairs.
    filepath : str
        The path to the output TFRecord file.
    image_format : str
        The format of the images in the dataset. Supported values: 'png' or '
        jpeg'.

    Raises
    ------
    ValueError
        If the specified image format is not supported.
    """
    if image_format == "png":
        serialize_sample = serialize_sample_for_png
    elif image_format == "jpeg":
        serialize_sample = serialize_sample_for_jpeg
    else:
        msg = f"Image format '{image_format}' is not supported. Please use "
        msg += "either 'png' or 'jpeg'."
        raise ValueError(msg)

    dataset = unbatch_dataset_if_batched(dataset)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with tf.io.TFRecordWriter(filepath) as writer:
        for sample in dataset:
            if isinstance(sample, tuple):
                image, label = sample
            else:
                image, label = sample, None
            example = serialize_sample(image, label)
            writer.write(example)
