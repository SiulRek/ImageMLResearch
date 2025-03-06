"""
Disclaimer: The classes in this module were used for visualization purposes
during the development of the Image Preprocessing Framework. They are not
used for plotting purposes in model development.
"""

from abc import ABC
import matplotlib.pyplot as plt
import tensorflow as tf


class ImagePlotterBase(ABC):
    """
    Base class for the ImagePlotter child classes.

    Attributes
    ----------
    last_fig : matplotlib.figure.Figure or None
        Stores the last generated figure.
    show_plot : bool
        Determines whether to display plots.
    """

    def __init__(self, show_plot=True):
        """
        Initialize the ImagePlotterBase.

        Parameters
        ----------
        show_plot : bool, optional
            Whether to display the plot after generation, by default True.
        """
        self.last_fig = None
        self.show_plot = show_plot

    def save_plot_to_file(self, filename):
        """
        Save the last generated plot to a file.

        Parameters
        ----------
        filename : str
            The path to save the figure.
        """
        if self.last_fig:
            self.last_fig.savefig(filename)
        else:
            print("No plot to save!")
        plt.close()

    def _generate_plot(
        self, fig, title, y_title=0.95, wspace=0.01, hspace=0.01
    ):
        """
        Generate and display a plot.

        Parameters
        ----------
        fig : matplotlib.figure.Figure
            The figure object.
        title : str
            The plot title.
        y_title : float, optional
            Vertical title position, by default 0.95.
        wspace : float, optional
            Width spacing between subplots, by default 0.01.
        hspace : float, optional
            Height spacing between subplots, by default 0.01.
        """
        fig.suptitle(title, fontsize=20, fontweight="bold", y=y_title)
        plt.subplots_adjust(wspace=wspace, hspace=hspace)
        self.last_fig = fig
        if self.show_plot:
            plt.show()


class ImagePlotter(ImagePlotterBase):
    """
    ImagePlotter class for visualizing image processing.

    Attributes
    ----------
    last_fig : matplotlib.figure.Figure or None
        Stores the last generated figure.
    show_plot : bool
        Determines whether to display plots.
    """

    def plot_images(self, image_tf_dataset, title="Images"):
        """
        Plot 4 images from the given TensorFlow dataset.

        Parameters
        ----------
        image_tf_dataset : tf.data.Dataset
            A TensorFlow dataset containing images.
        title : str, optional
            The plot title, by default "Images".
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
        Plot a side-by-side comparison of an original and a processed image.

        Parameters
        ----------
        original_tf_dataset : tf.data.Dataset
            A TensorFlow dataset with original images.
        processed_tf_dataset : tf.data.Dataset
            A TensorFlow dataset with processed images.
        index : int
            The index number of the images to compare.
        title : str, optional
            The plot title, by default an empty string.
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
