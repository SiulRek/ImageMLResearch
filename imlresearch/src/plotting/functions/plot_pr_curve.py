# NOTE: plot_pr_curve is only allowed for binary
# classification labels.


import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc


def plot_pr_curve(y_true, y_pred):
    """
    Plots a Precision-Recall curve using Matplotlib.

    Args:
        - y_true (array-like): True labels.
        - y_pred (array-like): Predicted probabilities for the positive
            class.
        - class_names (List): List of class names.

    Returns:
        - fig: The Matplotlib figure containing the Precision-Recall curve
            plot.
    """
    # Configuration
    figsize = (8, 8)
    fontsize = 12

    # Compute Precision-Recall curve and area under the curve
    precision, recall, _ = precision_recall_curve(y_true, y_pred)
    pr_auc = auc(recall, precision)

    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(
        recall,
        precision,
        color="blue",
        lw=2,
        label=f"Precision-Recall curve (area = {pr_auc:.2f})",
    )
    ax.plot([0, 1], [0.5, 0.5], color="gray", lw=2, linestyle="--")

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("Recall", fontsize=int(fontsize * 1.3))
    ax.set_ylabel("Precision", fontsize=int(fontsize * 1.3))
    ax.legend(loc="lower left", fontsize=fontsize)
    ax.tick_params(axis="both", which="major", labelsize=fontsize)
    ax.grid(True)
    
    plt.tight_layout()
    return fig
