import matplotlib.pyplot as plt
import tensorflow as tf

def plot_images(dataset, grid_size=(2, 2), label_to_title_func=None):
    """
    Plots a grid of images from a TensorFlow dataset.

    Parameters:
        - dataset: TensorFlow dataset containing the images and optionally
            labels.
        - grid_size: Tuple containing the grid size (rows, columns).
            Defaults to (2, 2).
        - label_to_title_func: Function to convert the label to a string.
            Defaults to None.
    """
    fig_size = (grid_size[1] * 4, grid_size[0] * 4)
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

        axes[i].axis("off")
        if label_to_title_func is not None:
            try:
                label = label_to_title_func(label)
            except Exception as e:
                msg = "Converting Label to Title failed with error"
                raise ValueError(msg) from e
            axes[i].set_title(label)
    return fig