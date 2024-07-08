import matplotlib.pyplot as plt
import numpy as np


def plot_multi_class_classification_results(
    x, y_true, y_pred, class_names, grid_size=(2, 2), prediction_bar=False
):
    """
    Plots a grid of images with their true and predicted labels. If the
    prediction_bar parameter is set to True, it also shows a bar plot with the
    predicted probabilities.

    Parameters:
        - x (np.ndarray): Input data (images, can be grayscale or RGB).
        - y_true (np.ndarray): True labels, one-hot encoded.
        - y_pred (np.ndarray): Predicted labels, one-hot encoded.
        - class_names (List): List of class names.
        - grid_size (Tuple): Tuple containing the grid size (rows, columns).
            Defaults to (2, 2).
        - prediction_bar (bool): Whether to show the predicted probabilities
            as a bar plot. Defaults to False.
    """
    # Configuration
    n_rows, n_cols = grid_size
    fig_size = (n_cols * (6 if prediction_bar else 3), n_rows * 4)
    font_size = 12
    sample_num = n_rows * n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols * (2 if prediction_bar else 1), figsize=fig_size
    )
    axes = axes.ravel()

    for i in range(sample_num):
        img_ax = axes[i * (2 if prediction_bar else 1)]

        image = x[i]
        true_label = y_true[i]
        predicted_probs = y_pred[i]

        true_label_index = np.argmax(true_label)
        predicted_label_index = np.argmax(predicted_probs)
        cmap = {"cmap": "gray"} if image.shape[-1] == 1 else {}
        img_ax.imshow(image.squeeze(), **cmap)
        img_ax.axis("off")

        title_color = "green" if predicted_label_index == true_label_index else "red"
        true_label_name = class_names[true_label_index]
        predicted_label_name = class_names[predicted_label_index]
        img_ax.set_title(
            f"Predicted: {predicted_label_name}\nTrue: {true_label_name}",
            fontsize=font_size,
            color=title_color,
        )

        if prediction_bar:
            bar_ax = axes[i * 2 + 1]
            bar_colors = [
                "green" if j == true_label_index else "blue"
                for j in range(len(class_names))
            ]
            if predicted_label_index != true_label_index:
                bar_colors[predicted_label_index] = "red"
            bar_ax.bar(range(len(predicted_probs)), predicted_probs, color=bar_colors)
            bar_ax.set_xticks(range(len(class_names)))
            bar_ax.set_xticklabels(class_names, rotation=90)
            bar_ax.set_ylim(0, 1)

    plt.tight_layout()
    return fig
