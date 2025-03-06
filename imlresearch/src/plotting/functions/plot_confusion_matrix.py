import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# NOTE: plot_confusion_matrix is only allowed for binary and multiclass
# classification labels.


def plot_confusion_matrix(y_true, y_pred, class_names):
    """
    Plots a confusion matrix using Matplotlib and Seaborn.

    Parameters
    ----------
    y_true : array-like
        True labels of the dataset.
    y_pred : array-like
        Predicted labels from the model.
    class_names : list
        List of class names corresponding to label indices.

    Returns
    -------
    matplotlib.figure.Figure
        The Matplotlib figure containing the confusion matrix plot.
    """
    # Configuration
    figsize = (len(class_names) + 2, len(class_names) + 2)
    fontsize = 12
    cmap = "Blues"
    normalize = True
    fmt = ".2" if normalize else "d"

    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        cm,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        xticklabels=class_names,
        yticklabels=class_names,
        ax=ax,
        annot_kws={"fontsize": fontsize},
    )

    ax.set_xlabel("Predicted Labels", fontsize=int(fontsize * 1.3))
    ax.set_ylabel("True Labels", fontsize=int(fontsize * 1.3))
    ax.tick_params(axis="both", which="major", labelsize=fontsize)

    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=fontsize)

    plt.tight_layout()
    return fig
