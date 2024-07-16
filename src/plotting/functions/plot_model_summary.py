import io

import matplotlib.pyplot as plt


def plot_model_summary(model):
    """
    Plot the summary of the passed model.

    Args:
        - model (Keras.Model): Keras model to plot the summary.
    
    Returns:
        - fig: Matplotlib figure for the model configuration.
    """
    # Configuration
    font_size = 10
    line_height = 0.25
    char_width = 0.15

    summary_str = io.StringIO()
    model.summary(print_fn=lambda x: summary_str.write(x + "\n"))
    summary_text = summary_str.getvalue()
    summary_str.close()

    max_line_length = max(len(line) for line in summary_text.split("\n"))
    fig_width = max_line_length * char_width
    fig_height = len(summary_text.split("\n")) * line_height

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.axis("off")
    ax.text(
        0.01,
        0.99,
        summary_text,
        fontsize=font_size,
        verticalalignment="top",
        horizontalalignment="left",
        transform=ax.transAxes,
    )

    plt.subplots_adjust(top=0.85)
    return fig
