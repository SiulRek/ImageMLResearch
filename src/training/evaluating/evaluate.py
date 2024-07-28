import numpy as np
from sklearn.metrics import classification_report

from src.training.evaluating.calculate_metrics import (
    calc_accuracy,
    calc_precision,
    calc_recall,
    calc_f1_score,
)


def evaluate_multi_class_classification(y_true, y_pred, class_names=None):
    """
    Computes classification metrics from true and predicted labels for
    evaluation. Calculates metrics for multi-class classification.

    Args:
        - y_true (arrayLike): True labels.
        - y_pred (arrayLike): Predicted labels.
        - class_names (list, optional): List of class names. If provided,
            the classification report will be returned with the class names.

    Returns:
        - dict: Evaluation metrics. Dictionary with the following keys:
        - 'accuracy' -> float
        - 'precision' -> float
        - 'recall' -> float
        - 'f1' -> float
        - 'classification_report' -> dict
    """
    y_pred_one_hot = np.zeros_like(y_pred)
    y_pred_one_hot[np.arange(len(y_pred)), np.argmax(y_pred, axis=-1)] = 1

    accuracy = calc_accuracy(y_true, y_pred_one_hot)
    precision = calc_precision(y_true, y_pred)
    recall = calc_recall(y_true, y_pred)
    f1_score = calc_f1_score(y_true, y_pred)
    cn_kwarg = {"target_names": class_names} if class_names else {}
    report = classification_report(
        y_true, y_pred_one_hot, output_dict=True, zero_division=0, **cn_kwarg
    )
    eval_metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1_score,
        "classification_report": report,
    }
    return eval_metrics


def evaluate_binary_classification(y_true, y_pred, class_names=None):
    """
    Computes classification metrics from true and predicted labels for
    evaluation. Calculates metrics for binary classification.

    Args:
        - y_true (arrayLike): True labels.
        - y_pred (arrayLike): Predicted labels.
        - class_names (list, optional): List with len=2 of class names. If
            provided, the classification report will be returned with the class
            names.

    Returns:
        - dict: Evaluation metrics. Dictionary with the following keys:
        - 'accuracy' -> float
        - 'precision' -> float
        - 'recall' -> float
        - 'f1' -> float
        - 'classification_report' -> dict
    """
    accuracy = calc_accuracy(y_true, y_pred)
    precision = calc_precision(y_true, y_pred)
    recall = calc_recall(y_true, y_pred)
    f1_score = calc_f1_score(y_true, y_pred)
    cn_kwarg = {"target_names": class_names} if class_names else {}
    y_pred_rounded = np.round(y_pred).astype(int)
    report = classification_report(
        y_true, y_pred_rounded, output_dict=True, zero_division=0, **cn_kwarg
    )
    report.pop("accuracy", None)
    eval_metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1_score,
        "classification_report": report,
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
    if label_type == "binary":
        return evaluate_binary_classification
    msg = f"Label type '{label_type}' is not supported for evaluation."
    raise ValueError(msg)
