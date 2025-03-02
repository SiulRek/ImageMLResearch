"""
Disclaimer: The classes in this module were used for visualization purposes
during the development of the Image Preprocessing Framework. They are not 
used for plotting purposes in model development.
"""

from abc import ABC

import matplotlib.pyplot as plt
import tensorflow as tf


class ImagePlotterBase(ABC):
    """Base class for the ImagePlotter child classes."""

    def __init__(self, show_plot=True):
        self.last_fig = None
        self.show_plot = show_plot

    def save_plot_to_file(self, filename):
        """Saves the last generated plot to a file."""
        if self.last_fig:
            self.last_fig.savefig(filename)
        else:
            print("No plot to save!")
        plt.close()

    def _generate_plot(
        self, fig, title, y_title=0.95, wspace=0.01, hspace=0.01
    ):
        """
        Generates and displays a plot.

        Args:
            - fig: The figure object.
            - title (str): Plot title.
            - y_title (float, optional): Vertical title position. Defaults to 0.95.
            - wspace (float, optional): Width spacing. Defaults to 0.01.
            - hspace (float, optional): Height spacing. Defaults to 0.01.
        """
        fig.suptitle(title, fontsize=20, fontweight="bold", y=y_title)
        plt.subplots_adjust(wspace=wspace, hspace=hspace)
        self.last_fig = fig
        if self.show_plot:
            plt.show()


class ImagePlotter(ImagePlotterBase):
    """
    ImagePlotter class for visualizing image processing.

    Pass a slice from a TensorFlow dataset as an input parameter.
    """

    def plot_images(self, image_tf_dataset, title="Images"):
        """
        Plots 4 images from the given TensorFlow dataset.

        Args:
            - image_tf_dataset: TensorFlow dataset containing images.
            - title (str, optional): Plot title. Defaults to 'Images'.
        """
        fig, axes = plt.subplots(2, 2, figsize=(8, 8))
        axes = axes.ravel()

        for i, image in enumerate(image_tf_dataset.take(4)):
            img_data = image.numpy()
            if len(image.shape) == 3 and image.shape[2] == 1:
                axes[i].imshow(tf.squeeze(image).numpy(), cmap="gray")
            else:
                axes[i].imshow(img_data)
            axes[i].axis("off")

        self._generate_plot(fig, title)

    def plot_image_comparison(
        self, original_tf_dataset, processed_tf_dataset, index, title=""
    ):
        """
        Plots a side-by-side comparison of an original and a processed image.

        Args:
            - original_tf_dataset: TensorFlow dataset with original images.
            - processed_tf_dataset: TensorFlow dataset with processed images.
            - index (int): Index number of the images to compare.
            - title (str, optional): Plot title. Defaults to 'Compare Images'.
        """
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        axes = axes.ravel()

        image_data_org = original_tf_dataset.skip(index).take(1)
        image_data_prc = processed_tf_dataset.skip(index).take(1)

        for i, take_object in enumerate([image_data_org, image_data_prc]):
            for image in take_object:
                img_data = image.numpy()
                if len(image.shape) == 3 and image.shape[2] == 1:
                    axes[i].imshow(tf.squeeze(image).numpy(), cmap="gray")
                else:
                    axes[i].imshow(img_data)
                axes[i].axis("off")

        title = title if title else "Compare Images"
        self._generate_plot(fig, title)
