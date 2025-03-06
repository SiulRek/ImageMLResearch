import matplotlib.pyplot as plt
import tensorflow as tf

from imlresearch.src.utils import unbatch_dataset_if_batched


def plot_images(dataset, grid_size=(2, 2), label_to_title_func=None):
    """
    Plots a grid of images from a TensorFlow dataset.

    The function determines a random skip value to avoid plotting the same
    images every time.

    Parameters
    ----------
    dataset : tf.data.Dataset
        TensorFlow dataset containing the images and optionally labels.
    grid_size : tuple, optional
        Tuple specifying the grid size as (rows, columns). Defaults to (2, 2).
    label_to_title_func : callable, optional
        Function to convert the label to a string. Defaults to None.

    Returns
    -------
    matplotlib.figure.Figure
        The Matplotlib figure containing the plotted images.
    """
    # Configuration
    fig_size = (grid_size[1] * 4, grid_size[0] * 4)
    sample_num = grid_size[0] * grid_size[1]
    font_size = 12
    dataset_length = len(list(dataset))

    dataset = unbatch_dataset_if_batched(dataset)

    if dataset_length > sample_num:
        skip = tf.random.uniform(
            [], 0, dataset_length - sample_num, dtype=tf.int64
        )
        dataset = dataset.skip(skip) if skip > 0 else dataset

    fig, axes = plt.subplots(grid_size[0], grid_size[1], figsize=fig_size)
    axes = axes.ravel()

    for i, data in enumerate(dataset.take(grid_size[0] * grid_size[1])):
        if isinstance(data, tuple):
            image, label = data
        else:
            image = data
            label = None

        if len(image.shape) == 3 and image.shape[2] == 1:
            axes[i].imshow(tf.squeeze(image).numpy(), cmap="gray")
        else:
            axes[i].imshow(image.numpy())

        if label_to_title_func is not None:
            try:
                label = label_to_title_func(label)
            except Exception as e:
                msg = "Converting Label to Title failed with error"
                raise ValueError(msg) from e
            axes[i].set_title(label, fontsize=font_size)

    return fig
