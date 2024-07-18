import matplotlib.pyplot as plt


def plot_training_history(history):
    """
    Plots the training and validation history of a Keras model.

    Args:
        - history: History dictionary containing the training and validation

    Returns:
        - fig: The Matplotlib figure containing the training and validation
            history plot.
    """
    # Configuration
    axes_size = (10, 6)
    font_size = 12

    history_dict = history
    epochs = range(1, len(history_dict[next(iter(history_dict))]) + 1)

    # Calculate the number of metrics and adjust the figure size accordingly
    num_metrics = (
        len(history_dict) // 2
        if any(key.startswith("val_") for key in history_dict)
        else len(history_dict)
    )
    fig, axes = plt.subplots(
        num_metrics, 1, figsize=(axes_size[0], axes_size[1] * num_metrics)
    )

    if num_metrics == 1:
        axes = [axes]

    i = 0
    for metric in history_dict:
        if not metric.startswith("val_"):
            ax = axes[i]
            i += 1
            ax.plot(epochs, history_dict[metric], "b-", label=f"Training {metric}")
            if f"val_{metric}" in history_dict:
                ax.plot(
                    epochs,
                    history_dict[f"val_{metric}"],
                    "b--",
                    label=f"Validation {metric}",
                )
            ax.set_xlabel("Epochs", fontsize=font_size)
            ax.set_ylabel(metric.capitalize(), fontsize=font_size)
            ax.tick_params(axis="x", labelsize=font_size)
            ax.tick_params(axis="y", labelsize=font_size)
            ax.legend(loc="best", fontsize=font_size)

    plt.tight_layout()
    return fig
