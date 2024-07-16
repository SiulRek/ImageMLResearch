import numpy as np

from src.training.evaluating.calculate_metrics import (
    calc_accuracy,
    calc_precision,
    calc_recall,
    calc_f1_score,
)


def evaluate_multi_class_classification(y_true, y_pred):
    """
    Computes classification metrics from true and predicted labels for
    evaluation. Calculates metrics for multi-class classification.

    Args:
        - y_true (arrayLike): True labels.
        - y_pred (arrayLike): Predicted labels.

    Returns:
        - dict: Evaluation metrics. Dictionary with the following keys:
        - 'accuracy'
        - 'precision'
        - 'recall'
        - 'f1'
    """

    y_pred_one_hot = np.zeros_like(y_pred)
    y_pred_one_hot[np.arange(len(y_pred)), np.argmax(y_pred, axis=-1)] = 1

    accuracy = calc_accuracy(y_true, y_pred_one_hot)
    precision = calc_precision(y_true, y_pred)
    recall = calc_recall(y_true, y_pred)
    f1_score = calc_f1_score(y_true, y_pred)
    eval_metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1_score,
    }
    return eval_metrics

def get_evaluation_function(label_type):
    """
    Gets the evaluation function based on the label type.

    Args:
        - label_type (str): Type of labels.

    Returns:
        - function: Evaluation function.
    """
    if label_type == "multi_class":
        return evaluate_multi_class_classification
    else:
        msg = f"Label type '{label_type}' is not supported for evaluation."
        raise ValueError(msg)