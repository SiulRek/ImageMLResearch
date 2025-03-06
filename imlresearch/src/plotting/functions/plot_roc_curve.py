import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# NOTE: plot_roc_curve is only allowed for binary classification labels.


def plot_roc_curve(y_true, y_pred):
    """
    Plots the Receiver Operating Characteristic (ROC) curve.

    Parameters
    ----------
    y_true : array-like
        True labels of the dataset.
    y_pred : array-like
        Predicted probabilities for the positive class.

    Returns
    -------
    matplotlib.figure.Figure
        The Matplotlib figure containing the ROC curve plot.
    """
    # Configuration
    figsize = (8, 8)
    fontsize = 12

    # Compute ROC curve and ROC area for the positive class
    fpr, tpr, _ = roc_curve(y_true, y_pred)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(
        fpr, tpr, color="blue", lw=2,
        label=f"ROC curve (area = {roc_auc:.2f})"
    )
    ax.plot([0, 1], [0, 1], color="gray", lw=2, linestyle="--")

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("False Positive Rate", fontsize=int(fontsize * 1.3))
    ax.set_ylabel("True Positive Rate", fontsize=int(fontsize * 1.3))
    ax.legend(loc="lower right", fontsize=fontsize)
    ax.tick_params(axis="both", which="major", labelsize=fontsize)
    ax.grid(True)

    plt.tight_layout()
    return fig
