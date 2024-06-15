import matplotlib.pyplot as plt


def plot_text(text, title=None):
    """
    Plots the given text on a matplotlib figure.

    Parameters:
        - text: The text to be plotted.
        - title: Optional title for the plot.
    """
    # Determine the size based on text length
    lines = text.split("\n")
    max_line_length = max(len(line) for line in lines)
    fig_width = max(1, max_line_length * 0.1)
    fig_height = max(1, len(lines) * 0.5)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    if title:
        fig.suptitle(title, fontsize=14, fontweight="bold")
    ax.text(0.5, 0.5, text, fontsize=12, ha="center", va="center", wrap=True)

    ax.axis("off")
    return fig
