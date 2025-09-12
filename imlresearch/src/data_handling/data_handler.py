import tensorflow as tf

from imlresearch.src.data_handling.io.create_dataset import create_dataset
from imlresearch.src.data_handling.io.save_images import save_images
from imlresearch.src.data_handling.labelling.label_utils import reverse_one_hot
from imlresearch.src.data_handling.manipulation.prepare_dataset import (
    prepare_dataset,
)
from imlresearch.src.data_handling.manipulation.split_dataset import (
    split_dataset,
)
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)


class DataHandler(ResearchAttributes):
    """
    A class for handling dataset operations including creation, enhancement,
    splitting, and saving images.
    """

    def __init__(self):
        """
        Initializes the DataHandler.
        """
        # Not initializing ResearchAttributes here, prefer call
        # synchronize_research_attributes explicitly. super().__init__()

        # Initialize research attributes used in the DataHandler
        self._label_manager = None  # Read
        self._datasets_container = {
            # Dataset Name: Dataset
        }  # Read/write

        self._backuped_datasets_container = {}

    def _assert_dataset_format(self, dataset):
        """
        Checks if the dataset has the format (image, label) and if the image
        shape is (height, width, 1|3).

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset to check.

        Raises
        ------
        ValueError
            If the dataset is not in the required format.
        """
        for sample in dataset.take(1):
            if not isinstance(sample, tuple) and len(sample) != 2:
                msg = "Dataset must be of form (image, label)."
                raise ValueError(msg)
            img, _ = sample
            if img.shape.ndims != 3:
                msg = "Image must have 3 dimensions."
                raise ValueError(msg)
            if img.shape[2] not in [1, 3]:
                msg = "Image must have 1 or 3 channels."
                raise ValueError(msg)

    def load_dataset(self, data):
        """
        Loads a dataset from the given data and stores it in the
        'datasets_container' under 'complete_dataset'.

        Parameters
        ----------
        data : tf.data.Dataset or dict or pandas.DataFrame
            The data to load. It can be:
            1. A TensorFlow dataset of tuples (image, label), where image
               shape is (height, width, 1|3).
            2. A dictionary or pandas DataFrame with 'path' and 'label'
               columns.

        Notes 
        -----
        When passing a `tf.data.Dataset`, it is recommended to
        provide a dataset without Keras operations like shuffling or batching.
        These operations should be applied in the `prepare_datasets` method.
        """
        if isinstance(data, tf.data.Dataset):
            self._assert_dataset_format(data)
            self._datasets_container.update({"complete_dataset": data})
            return
        try:
            dataset = create_dataset(
                data,
                self._label_manager.label_type,
                self._label_manager.class_names,
            )
            self._assert_dataset_format(dataset)
            self._datasets_container.update({"complete_dataset": dataset})
            return
        except ValueError as exc:
            msg = f"Not possible to load dataset from {data}."
            raise ValueError(msg) from exc

    def _assert_dataset_exists(self, dataset_name):
        """
        Checks if a dataset name exists in the dataset container.

        Parameters
        ----------
        dataset_name : str
            The name of the dataset to check.

        Raises
        ------
        ValueError
            If the dataset does not exist in the dataset container.
        """
        if dataset_name not in self._datasets_container:
            msg = f"Dataset {dataset_name} not found in the dataset container."
            raise ValueError(msg)

    def prepare_datasets(
        self,
        dataset_names=None,
        batch_size=None,
        shuffle_seed=None,
        prefetch_buffer_size=tf.data.experimental.AUTOTUNE,
        repeat_num=None,
    ):
        """
        Prepares datasets by applying transformations and updates them in the
        'datasets_container'.

        Parameters
        ----------
        dataset_names : list, optional
            The names of the datasets to enhance. Can be 'complete_dataset' or
            any split datasets ('train_dataset', 'val_dataset',
            'test_dataset'). If None (default), all datasets in the container
            are processed.
        batch_size : int, optional
            The batch size for the dataset. If None (default), no batching is
            applied.
        shuffle_seed : int, optional
            The seed for shuffling. If None (default), no shuffling is applied.
        prefetch_buffer_size : int, optional
            The prefetch buffer size. Defaults to
            tf.data.experimental.AUTOTUNE.
        repeat_num : int, optional
            The number of times to repeat the dataset. If None (default), no
            repeating is applied.
        """
        dataset_names = dataset_names or list(self._datasets_container.keys())
        for dataset_name in dataset_names:
            self._assert_dataset_exists(dataset_name)
            dataset = self._datasets_container[dataset_name]
            enhanced_dataset = prepare_dataset(
                dataset,
                batch_size=batch_size,
                shuffle_seed=shuffle_seed,
                prefetch_buffer_size=prefetch_buffer_size,
                repeat_num=repeat_num,
            )
            self._datasets_container.update({dataset_name: enhanced_dataset})

    def split_dataset(
        self, train_split=0.8, val_split=0.1, test_split=0.1, dataset_size=None
    ):
        """
        Splits 'complete_dataset' into 'train_dataset', 'val_dataset', and
        'test_dataset'. Removes the 'complete_dataset' after splitting.

        Parameters
        ----------
        train_split : float
            Proportion of the dataset for training.
        val_split : float
            Proportion of the dataset for validation.
        test_split : float
            Proportion of the dataset for testing.
        dataset_size : int, optional
            The dataset size. If None, the size is determined using the
            'cardinality' method.
        """
        self._assert_dataset_exists("complete_dataset")
        dataset = self._datasets_container["complete_dataset"]
        train_dataset, val_dataset, test_dataset = split_dataset(
            dataset, train_split, val_split, test_split, dataset_size
        )
        self._datasets_container.update(
            {
                "train_dataset": train_dataset,
                "val_dataset": val_dataset,
                "test_dataset": test_dataset,
            }
        )
        self._datasets_container.pop("complete_dataset")

    def save_images(self, output_dir, prefix=None, num_images=None):
        """
        Saves images from the dataset to a specified directory.

        Parameters
        ----------
        output_dir : str
            The directory to save the images.
        prefix : str or callable, optional
            The prefix for the image files. If callable, it should take the
            label as input and return a string. If None, a default prefix is
            used.
        num_images : int, optional
            The number of images to save. If None, the complete dataset is
            taken.
        """
        image_format = "jpg"
        if prefix is None:

            def prefix(label):
                prefix = "image"
                try:
                    label = reverse_one_hot(label)
                    prefix += f"_{self._label_manager.get_class(label)}"
                except ValueError:
                    pass
                return prefix

        start_number = 0

        concatenated_dataset = None
        for dataset in self._datasets_container.values():
            if concatenated_dataset is None:
                concatenated_dataset = dataset
            else:
                concatenated_dataset = concatenated_dataset.concatenate(
                    dataset
                )

        save_images(
            concatenated_dataset,
            output_dir,
            image_format=image_format,
            prefix=prefix,
            start_number=start_number,
            num_images=num_images,
        )

    def backup_datasets(self):
        """
        Creates a backup of the current dataset container.
        """
        for key, dataset in self._datasets_container.items():
            for sample in dataset.take(1):
                if isinstance(sample, tuple):
                    self._backuped_datasets_container.update(
                        {key: dataset.map(lambda x, y: (x, y))}
                    )
                else:
                    self._backuped_datasets_container.update(
                        {key: dataset.map(lambda x: x)}
                    )

    def restore_datasets(self):
        """
        Restores the dataset container from the backup.

        Raises
        ------
        ValueError
            If no backup dataset container is found.
        """
        if not self._backuped_datasets_container:
            msg = "No backuped dataset container found."
            raise ValueError(msg)
        self._datasets_container.update(self._backuped_datasets_container)
        self._backuped_datasets_container.clear()
