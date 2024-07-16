import tensorflow as tf


def calc_accuracy(y_true, y_pred):
    """
    Calculates the accuracy of the predicted labels.

    Args:
        - y_true (array-like): The true labels.
        - y_pred (array-like): The predicted labels.

    Returns:
        - float: The accuracy score.
    """
    accuracy = tf.keras.metrics.Accuracy()(y_true, y_pred)
    accuracy = float(accuracy.numpy())
    return accuracy


def calc_precision(y_true, y_pred):
    """
    Calculates the precision metric for binary classification.

    Args:
        - y_true (array-like): The true labels.
        - y_pred (array-like): The predicted labels.

    Returns:
        - float: The precision score.
    """
    precision = tf.keras.metrics.Precision()(y_true, y_pred)
    precision = float(precision.numpy())
    return precision


def calc_recall(y_true, y_pred):
    """
    Calculates the recall metric.

    Args:
        - y_true (array-like): The true labels.
        - y_pred (array-like): The predicted labels.

    Returns:
        - float: The recall score.
    """
    recall = tf.keras.metrics.Recall()(y_true, y_pred)
    recall = float(recall.numpy())
    return recall


def calc_f1_score(y_true, y_pred):
    """
    Calculates the F1 score given the true labels and predicted labels.

    Args:
        - y_true (array-like): The true labels.
        - y_pred (array-like): The predicted labels.

    Returns:
        - float: The F1 score.
    """
    precision = calc_precision(y_true, y_pred)
    recall = calc_recall(y_true, y_pred)
    f1_score = (
        2 * (precision * recall) / (precision + recall + tf.keras.backend.epsilon())
    )
    return float(f1_score)
