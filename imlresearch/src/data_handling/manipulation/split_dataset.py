def split_dataset(
    dataset, train_split=0.8, val_split=0.1, test_split=0.1, dataset_size=None
):
    """
    Splits a TensorFlow dataset into training, validation, and test sets
    based on the specified proportions.

    Parameters
    ----------
    dataset : tf.data.Dataset
        The TensorFlow dataset to split.
    train_split : float, optional
        Proportion of the dataset to include in the training set.
        Default is 0.8.
    val_split : float, optional
        Proportion of the dataset to include in the validation set.
        Default is 0.1.
    test_split : float, optional
        Proportion of the dataset to include in the test set. Default is 0.1.
    dataset_size : int, optional
        The size of the dataset. If None, the size is determined using the
        `cardinality` method.

    Returns
    -------
    tuple of (tf.data.Dataset or None)
        - The training dataset, or None if its size is 0.
        - The validation dataset, or None if its size is 0.
        - The test dataset, or None if its size is 0.
    """
    if train_split + val_split + test_split != 1.0:
        msg = "The sum of train_split, val_split, and test_split should be 1.0."
        raise ValueError(msg)
    if dataset_size is None:
        dataset_size = dataset.cardinality().numpy()
        if dataset_size < 0:
            msg = "Failed to determine the dataset size."
            raise ValueError(msg)

    train_size = int(train_split * dataset_size)
    val_size = int(val_split * dataset_size)
    test_size = dataset_size - train_size - val_size

    train_dataset = dataset.take(train_size) if train_size > 0 else None
    val_dataset = (
        dataset.skip(train_size).take(val_size) if val_size > 0 else None
    )
    test_dataset = (
        dataset.skip(train_size + val_size) if test_size > 0 else None
    )

    return train_dataset, val_dataset, test_dataset
