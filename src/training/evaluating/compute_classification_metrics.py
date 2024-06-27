import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)


def compute_classification_metrics(y_true, y_pred, class_names):
    """
    Computes classification metrics from true and predicted labels for
    evaluation. Calculates metrics for binary, multi-class, and multi-label
    classification.

    Args:
        - y_true (np.ndarray|tf.Tensor): True labels.
        - y_pred (np.ndarray|tf.Tensor): Predicted labels.
        - class_names (list): List of class names.

    Returns:
        - dict: Evaluation metrics. Dictionary with the following keys:
        - 'accuracy'
        - 'precision'
        - 'recall'
        - 'f1'
        - 'classification_report'
    """
    y_pred = np.round(y_pred)
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="weighted")
    recall = recall_score(y_true, y_pred, average="weighted")
    f1 = f1_score(y_true, y_pred, average="weighted")
    classification_rep = classification_report(y_true, y_pred, target_names=class_names)
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "classification_report": classification_rep,
    }

