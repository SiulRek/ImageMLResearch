import os
import tensorflow as tf


def _bytes_feature(value):
    """
    Convert a value to a bytes_list for TensorFlow features.

    Parameters
    ----------
    value : bytes or tf.Tensor
        The value to be converted into a TensorFlow Feature.

    Returns
    -------
    tf.train.Feature
        The bytes_list feature containing the value.
    """
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy()  # Convert EagerTensor to numpy
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def serialize_image(image_path):
    """
    Read an image, decode it, and serialize it into a tf.train.Example.

    Parameters
    ----------
    image_path : str
        Path to the image file.

    Returns
    -------
    bytes
        Serialized Example proto containing the image.
    """
    image_string = tf.io.read_file(image_path)
    image_decoded = tf.image.decode_png(image_string)
    image_bytes = tf.io.encode_png(tf.cast(image_decoded, tf.uint8))
    feature = {"image_raw": _bytes_feature(image_bytes)}
    example_proto = tf.train.Example(
        features=tf.train.Features(feature=feature)
    )
    return example_proto.SerializeToString()


def create_tfrecord_from_images(image_directory, output_filepath):
    """
    Create a TFRecord file from images in a specified directory.

    Parameters
    ----------
    image_directory : str
        Directory where image files are located.
    output_filepath : str
        Path to store the TFRecord file.
    """
    with tf.io.TFRecordWriter(output_filepath) as writer:
        for filename in os.listdir(image_directory):
            if filename.lower().endswith(".png"):
                image_path = os.path.join(image_directory, filename)
                example = serialize_image(image_path)
                writer.write(example)

    print(f"TFRecord file has been created at {output_filepath}")


if __name__ == "__main__":
    image_directory = "imlresearch/src/testing/image_data/geometrical_forms"
    output_filepath = (
        "imlresearch/src/testing/image_data/tf_records/"
        "geometrical_forms.tfrecord"
    )
    create_tfrecord_from_images(image_directory, output_filepath)
