import tensorflow as tf


def calc_accuracy(y_true, y_pred):
    """
    Calculate the accuracy of the predicted labels.

    Parameters
    ----------
    y_true : array-like
        The true labels.
    y_pred : array-like
        The predicted labels.

    Returns
    -------
    float
        The accuracy score.
    """
    accuracy = tf.keras.metrics.Accuracy()(y_true, y_pred)
    return float(accuracy.numpy())


def calc_precision(y_true, y_pred):
    """
    Calculate the precision metric for binary classification.

    Parameters
    ----------
    y_true : array-like
        The true labels.
    y_pred : array-like
        The predicted labels.

    Returns
    -------
    float
        The precision score.
    """
    precision = tf.keras.metrics.Precision()(y_true, y_pred)
    return float(precision.numpy())


def calc_recall(y_true, y_pred):
    """
    Calculate the recall metric.

    Parameters
    ----------
    y_true : array-like
        The true labels.
    y_pred : array-like
        The predicted labels.

    Returns
    -------
    float
        The recall score.
    """
    recall = tf.keras.metrics.Recall()(y_true, y_pred)
    return float(recall.numpy())


def calc_f1_score(y_true, y_pred):
    """
    Calculate the F1 score given the true labels and predicted labels.

    Parameters
    ----------
    y_true : array-like
        The true labels.
    y_pred : array-like
        The predicted labels.

    Returns
    -------
    float
        The F1 score.
    """
    precision = calc_precision(y_true, y_pred)
    recall = calc_recall(y_true, y_pred)
    epsilon = tf.keras.backend.epsilon()
    f1_score = 2 * (precision * recall) / (precision + recall + epsilon)
    return float(f1_score)
