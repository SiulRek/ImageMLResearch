import os

from PIL import Image
import numpy as np
import tensorflow as tf


def save_mnist_digits_images(output_dir, sample_num, start_num, extension):
    """
    Save MNIST digits images to a directory.

    Parameters
    ----------
    output_dir : str
        Directory to save the images.
    sample_num : int
        Number of images to save.
    start_num : int
        Starting number for filenames.
    extension : str
        Image file extension.
    """
    extension = extension if extension.startswith(".") else f".{extension}"
    mnist_digits_dataset = tf.keras.datasets.mnist.load_data()
    (X, Y), _ = mnist_digits_dataset

    if X.ndim == 3:
        X = np.stack([X] * 3, axis=-1)  # Convert grayscale to RGB format
    Y = tf.keras.utils.to_categorical(Y)

    random_indices = np.random.permutation(len(X))
    X, Y = X[random_indices], Y[random_indices]

    if sample_num:
        X, Y = X[:sample_num], Y[:sample_num]

    os.makedirs(output_dir, exist_ok=True)

    for i, (image, label) in enumerate(zip(X, Y)):
        image_pil = Image.fromarray(image)
        label = np.argmax(label)
        filename = f"image_{i + start_num}_digit_{label}{extension}"
        image_pil.save(os.path.join(output_dir, filename))


if __name__ == "__main__":
    output_dir = "./imlresearch/src/testing/image_data/mnist_digits"
    sample_num = 5
    start_num = 1
    extension = "png"

    save_mnist_digits_images(output_dir, sample_num, start_num, extension)
