import os

from PIL import Image
import numpy as np
import tensorflow as tf


def save_mnist_digits_images(output_dir, sample_num, start_num, extension):
    """
    Save MNIST digits images to a directory.

    Args:
        - output_dir (str): The directory to save the images.
        - sample_num (int): The number of images to save.
        - start_num (int): The starting number for the image filenames.
        - extension (str): The extension for the image files.
    """
    extension = extension if extension.startswith(".") else f".{extension}"
    mnist_digits_dataset = tf.keras.datasets.mnist.load_data()

    (X, Y), _ = mnist_digits_dataset

    if X.ndim == 3:
        X = np.stack([X] * 3, axis=-1)
    Y = tf.keras.utils.to_categorical(Y)

    random_indices = np.random.permutation(len(X))
    X = X[random_indices]
    Y = Y[random_indices]
    if sample_num:
        X = X[:sample_num]
        Y = Y[:sample_num]

    os.makedirs(output_dir, exist_ok=True)

    for i, (image, label) in enumerate(zip(X, Y)):
        image_pil = Image.fromarray(image)
        label = np.argmax(label)
        image_pil.save(
            os.path.join(output_dir, f"image_{i + start_num}_digit_{label}{extension}")
        )


if __name__ == "__main__":
    output_dir = "./imlresearch/testing/image_data/mnist_digits"
    sample_num = 5
    start_num = 1
    extension = "png"

    save_mnist_digits_images(output_dir, sample_num, start_num, extension)
