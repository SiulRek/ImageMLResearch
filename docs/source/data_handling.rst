.. _Modules_Data_Handling:

Data Handling
-----------------------------------------------

Description
+++++++++++

The Data Handling module facilitates the preparation of raw data for machine learning experiments using the ``DataHandler`` class.

Main class
++++++++++

.. class:: DataHandler

    A class for handling dataset operations including creation, enhancement,
    splitting, and saving images.

    .. _DataHandler_init:
    .. method:: __init__()

        Initializes the DataHandler.

    .. _DataHandler_load_dataset:
    .. method:: load_dataset(data: Union[tf.data.Dataset, dict, pandas.DataFrame])
        
        Loads a dataset from the given data and stores it in the 'datasets_container' under 'complete_dataset'.

        :param data: The data to load. It can be:  

                        1. A TensorFlow dataset of tuples (image, label), where image
                           shape is (height, width, 1|3).
                        2. A dictionary or pandas DataFrame with 'path' and 'label'
                           columns.
                        
        :type data: Union[tf.data.Dataset, dict, pandas.DataFrame]

    .. _DataHandler_prepare_datasets:
    .. method:: prepare_datasets(dataset_names: Optional[List[str]] = None, batch_size: Optional[int] = None, shuffle_seed: Optional[int] = None, prefetch_buffer_size: int = tf.data.experimental.AUTOTUNE, repeat_num: Optional[int] = None)
        
        Prepares datasets by applying transformations and updates them in the
        'datasets_container'.

        :param dataset_names: The names of the datasets to enhance. Can be 'complete_dataset' or
                              any split datasets ('train_dataset', 'val_dataset', 'test_dataset').
                              If None, all datasets are processed.
        :type dataset_names: Optional[List[str]]
        :param batch_size: The batch size for the dataset. If None, no batching is applied.
        :type batch_size: Optional[int]
        :param shuffle_seed: The seed for shuffling. If None, no shuffling is applied.
        :type shuffle_seed: Optional[int]
        :param prefetch_buffer_size: The prefetch buffer size. Defaults to tf.data.experimental.AUTOTUNE.
        :type prefetch_buffer_size: int
        :param repeat_num: The number of times to repeat the dataset. If None, no repetition is applied.
        :type repeat_num: Optional[int]

    .. _DataHandler_split_dataset:
    .. method:: split_dataset(train_split: float = 0.8, val_split: float = 0.1, test_split: float = 0.1, dataset_size: Optional[int] = None)
        
        Splits 'complete_dataset' into 'train_dataset', 'val_dataset', and
        'test_dataset'. Removes the 'complete_dataset' after splitting.

        :param train_split: Proportion of the dataset for training. Defaults to 0.8.
        :type train_split: float
        :param val_split: Proportion of the dataset for validation. Defaults to 0.1.
        :type val_split: float
        :param test_split: Proportion of the dataset for testing. Defaults to 0.1.
        :type test_split: float
        :param dataset_size: The dataset size. If None, the size is determined using the
                             'cardinality' method.
        :type dataset_size: Optional[int]

    .. _DataHandler_save_images:
    .. method:: save_images(output_dir: str, prefix: Optional[Union[str, Callable[[Any], str]]] = None, num_images: Optional[int] = None)
        
        Saves images from the dataset to a specified directory.

        :param output_dir: The directory to save the images.
        :type output_dir: str
        :param prefix: The prefix for the image files. If callable, it should take the
                       label as input and return a string. If None, a default prefix is used.
        :type prefix: Optional[Union[str, Callable[[Any], str]]]
        :param num_images: The number of images to save. If None, the complete dataset is taken.
        :type num_images: Optional[int]

    .. _DataHandler_backup_datasets:
    .. method:: backup_datasets()
        
        Creates a backup of the current dataset container.

    .. _DataHandler_restore_datasets:
    .. method:: restore_datasets()
        
        Restores the dataset container from the backup.
