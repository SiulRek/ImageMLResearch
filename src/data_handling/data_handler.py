import tensorflow as tf

from src.data_handling.io.create_dataset import create_dataset
from src.data_handling.io.save_images import save_images
from src.data_handling.labelling.label_manager import LabelManager
from src.data_handling.labelling.temp import reverse_one_hot
from src.data_handling.manipulation.enhance_dataset import enhance_dataset
from src.data_handling.manipulation.split_dataset import split_dataset


class DataHandler:
    """ A class to handle various dataset operations including creation,
    enhancement, splitting, and saving images. """

    def __init__(self, label_type=None, category_names=None):
        """
        Initializes the DataHandler with optional label type and category names.

        Args:
            - label_type (str, optional): The type of labels used.
            - category_names (list, optional): The list of category names.
        """
        self.dataset_container = {}
        self.backuped_dataset_container = {}
        self.label_manager = LabelManager(label_type, category_names)
        self.label_type = label_type
        self.category_names = category_names

    def create_dataset(self, data):
        """
        Creates a dataset from the given data and stores it in the
        'dataset_container' under 'complete_dataset'.

        Args:
            - data (any): The data used to create the dataset.
        """
        self.dataset_container["complete_dataset"] = create_dataset(
            data, self.label_type, self.category_names
        )

    def _check_dataset_exists(self, dataset_name):
        """
        Checks if a dataset name exists in the dataset container.

        Args:
            - dataset_name (str): The name of the dataset to check.

        Raises:
            - ValueError: If the dataset does not exist in the dataset
                container.
        """
        if dataset_name not in self.dataset_container:
            msg = f"Dataset {dataset_name} not found in the dataset container."
            raise ValueError(msg)

    def enhance_dataset(
        self,
        dataset_names=["complete_dataset"],
        batch_size=None,
        shuffle=False,
        random_seed=None,
        prefetch_buffer_size=tf.data.experimental.AUTOTUNE,
        cache=False,
        repeat_num=None,
    ):
        """
        Enhances the dataset by applying transformations and stores the enhanced
        dataset back in the 'dataset_container'.

        Args:
            - dataset_names (list): The names of the dataset to enhance. Can
                be 'complete_dataset' or 'train_dataset', 'val_dataset', or
                'test_dataset' if split already.
            - batch_size (int, optional): The batch size for the dataset.
            - shuffle (bool, optional): Whether to shuffle the dataset.
            - random_seed (int, optional): The random seed for shuffling.
            - prefetch_buffer_size (int, optional): The prefetch buffer
                size.
            - cache (bool, optional): Whether to cache the dataset.
            - repeat_num (int, optional): The number of times to repeat the
                dataset.
        """
        for dataset_name in dataset_names:
            self._check_dataset_exists(dataset_name)
            dataset = self.dataset_container[dataset_name]
            enhanced_dataset = enhance_dataset(
                dataset,
                batch_size,
                shuffle,
                random_seed,
                prefetch_buffer_size,
                cache,
                repeat_num,
            )
            self.dataset_container[dataset_name] = enhanced_dataset

    def split_dataset(self, train_size, val_size, test_size):
        """
        Splits the 'complete_dataset' into 'train_dataset', 'val_dataset' and
        'test_dataset' and stores them in the 'dataset_container'. Note that the
        complete dataset is removed.

        Args:
            - train_size (float): The proportion of the dataset for
                training.
            - val_size (float): The proportion of the dataset for
                validation.
            - test_size (float): The proportion of the dataset for testing.
        """
        self._check_dataset_exists("complete_dataset")
        dataset = self.dataset_container["complete_dataset"]
        train_dataset, val_dataset, test_dataset = split_dataset(
            dataset, train_size, val_size, test_size
        )
        self.dataset_container["train_dataset"] = train_dataset
        self.dataset_container["val_dataset"] = val_dataset
        self.dataset_container["test_dataset"] = test_dataset

        self.dataset_container.pop("complete_dataset")

    def save_images(self, output_dir, prefix=None):
        """
        Saves the images from the dataset to a specified directory.

        Args:
            - output_dir (str): The directory to save the images. Defaults
                to "jpg".
            - prefix (str|callable, optional): The prefix for the image
                file. Can be a string or a callable that takes the label as
                input and returns a string. If None, the default prefix is used.
        """
        image_format = "jpg"
        if prefix is None:

            def prefix(label):
                prefix = "image"
                try:
                    label = reverse_one_hot(label)
                    prefix += f"_{self.label_manager.get_category(label)}"
                except ValueError:
                    pass
                return prefix

        start_number = 0

        # concatenate all datasets in container
        dataset_iterator = self.dataset_container.values()
        concatenated_dataset = None
        for dataset in dataset_iterator:
            if dataset is None:
                concatenated_dataset = dataset
            else:
                concatenated_dataset = concatenated_dataset.concatenate(dataset)

        save_images(dataset, output_dir, image_format, prefix, start_number)

    def backup_datasets(self):
        """ Backups the current dataset container. """
        for key, dataset in self.dataset_container.items():
            # Create a copy of the dataset
            for sample in dataset.take(1):
                if isinstance(sample, tuple):
                    self.backuped_dataset_container[key] = dataset.map(
                        lambda x, y: (x, y)
                    )
                else:
                    self.backuped_dataset_container[key] = dataset.map(lambda x: x)

    def restore_datasets(self):
        """
        Restores the backuped dataset container.

        Raises:
            - ValueError: If no backuped dataset container is found.
        """
        if not self.backuped_dataset_container:
            msg = "No backuped dataset container found."
            raise ValueError(msg)
        self.dataset_container = self.backuped_dataset_container
        self.backuped_dataset_container = {}
