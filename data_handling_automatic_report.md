# Data Handling Automatic Report

This report presents an overview of the `data_handling` module in the `ImageMLResearch` software project. The structure of the folder is shown below, as well as the descriptions of the main functionalities.


```py
data_handling/
├── helpers/
│   ├── ...
├── io/
│   ├── create_dataset.py
│   ├── decode_image.py
│   └── save_images.py
├── manipulation/
│   ├── enhance_dataset.py
│   ├── pack_images_and_labels.py
│   ├── split_dataset.py
│   └── unpack_dataset.py
├── tests/
│   ├── ...
└── tfrecord_serialization/
    ├── deserialize.py
    └── serialize.py
```

## IO Folder

The `io` folder is responsible for the input/output operations related to the project.

### create_dataset.py

This script creates a TensorFlow Dataset object from the given data containing file paths and labels using LabelManager for label encoding.

```python
def create_dataset(data, label_type, category_names):
    """Creates a TensorFlow Dataset object from the given data containing file paths and labels using LabelManager for label encoding.
    LabelManager is a class that handles label encoding and decoding for various label types.
    
    Args:
        - data (dicts, list of dicts or pandas.DataFrame): Data containing 'path' and labels. 'path' should contain the relative file paths and labels should contain the corresponding labels for the specified 'label_type'.
        - label_type (str, optional): Specifies the label encoding strategy ('binary', 'category_codes', 'sparse_category_codes', or 'object_detection'). Default is None.
        - category_names (list, optional): The existing category names for label encoding if 'label_type' is not None. Default is None.
    
    Returns:
        - tf.data.Dataset: A TensorFlow Dataset containing tuples of (image, encoded label), where 'image' is the decoded image file and 'encoded label' is processed by LabelManager. If no labels are provided, returns a dataset of images only.
    """
```

### save_images.py

This script is responsible for saving images from a dataset to a specified directory. The unlabeled dataset is allowed.

```python
def save_images(dataset, output_dir, image_format, prefix, start_number):
    """Saves images from dataset to the specified directory. Unlabeled dataset is allowed.

    Args:
        - dataset (tf.data.Dataset): The dataset containing images and labels.
        - output_dir (str): The directory to save the encoded image files.
        - image_format (str, optional): The format for saving images ('jpg' or 'png').
        - prefix (str or function, optional): The prefix for naming the saved images. If a function is provided, it should take a label and return a string.
        - start_number (int, optional): The starting number for the sequential naming.
    """
```

## Manipulation Folder

This `manipulation` folder is responsible for handling the processing of image data.

### pack_images_and_labels.py

This script packs two `tf.data.Dataset` objects for images and labels into a single `tf.data.Dataset`.

```python
def pack_images_and_labels(image_dataset, label_dataset):
    """
    Packs two tf.data.Dataset objects for images and labels into a single
    tf.data.Dataset.
    
    Args:
        - image_dataset (tf.data.Dataset): A dataset of image tensors.
        - label_dataset (tf.data.Dataset): A dataset of label tensors.
    
    Returns:
        - tf_dataset (tf.data.Dataset): A tf.data.Dataset object containing
            tuples of (image, label).
    """
```

### split_dataset.py

This script splits a TensorFlow dataset into training, validation, and test sets based on the specified proportions.

```python
def split_dataset(dataset, train_size, val_size, test_size):
    """
    Splits a TensorFlow dataset into training, validation, and test sets based
    on the specified proportions.
    
    Args:
        - dataset (tf.data.Dataset): The TensorFlow dataset to split.
        - train_size (float, optional): Proportion of the dataset to include
            in the training set.
        - val_size (float, optional): Proportion of the dataset to include
            in the validation set.
        - test_size (float, optional): Proportion of the dataset to include
            in the test set.
    
    Returns:
        - tf.data.Dataset: The training dataset.
        - tf.data.Dataset: The validation dataset.
        - tf.data.Dataset: The test dataset.
    """
```

### enhance_dataset.py

The script is designed to enhance a TensorFlow dataset by applying shuffling, batching, prefetching, and optionally repeating a specified number of times or indefinitely.

```python
def enhance_dataset(dataset, batch_size, shuffle, random_seed, prefetch_buffer_size, cache, repeat_num):
    """
    Enhances a TensorFlow dataset by applying shuffling, batching, prefetching,
    and optionally repeating a specified number of times or indefinitely if
    repeat_num is None and the repeat parameter is set to True.
    
    Args:
        - dataset (tf.data.Dataset): The initial TensorFlow dataset to
            enhance.
        - batch_size (int, optional): Size of batches of data.
        - shuffle (bool, optional): Whether to shuffle the dataset. Default
            is False.
        - random_seed (int, optional): Seed for random shuffling if shuffle
            is True.
        - prefetch_buffer_size (int, optional): Number of batches to
            prefetch (default is tf.data.experimental.AUTOTUNE).
        - cache (bool, optional): Whether to cache the dataset. Default is
            False.
        - repeat_num (int, optional): Number of times to repeat the dataset.
            None for indefinite repeat.
    
    Returns:
        - tf.data.Dataset: The enhanced TensorFlow dataset.
    """
```

### unpack_dataset.py

The script unpacks a `tf.data.Dataset` into two `tf.data.Dataset` objects for images and labels.

```python
def unpack_dataset(tf_dataset):
    """
    Unpacks a tf.data.Dataset into two tf.data.Dataset objects for images and
    labels.
    
    Args:
        - tf_dataset (tf.data.Dataset): A tf.data.Dataset object containing
            tuples of (image, label). 'image' is the decoded image file and
            'label' is an integer label.
    
    Returns:
        - image_dataset (tf.data.Dataset): A dataset of image tensors.
        - label_dataset (tf.data.Dataset): A dataset of label tensors.
    """
```

## TFRecord Serialization Folder

The `tfrecord_serialization` folder contains scripts for handling the serialization process for TensorFlow.

### deserialize.py

These scripts together form the logic to load a TFRecord file into a `tf.data.Dataset` object.

```python

def deserialize_dataset_from_tfrecord(filepath, label_dtype):
    """
    Loads a TFRecord file into a tf.data.Dataset object.
    
    Args:
        - filepath (str): The path to the TFRecord file.
        - label_dtype (tf.DType, optional): The data type of the labels in
            the dataset. If None, assumes there are no labels.
    
    Returns:
        - tf.data.Dataset: A dataset object containing image and optionally
            label pairs.
    """
```

### serialize.py

Scripts in this file facilitate the process of saving a dataset to a TFRecord file.

```python

def serialize_dataset_to_tf_record(dataset, filepath, image_format):
    """
    Saves a dataset to a TFRecord file. If the dataset is batched, it will be
    unbatched before saving. Labeled dataset is allowed and will be serialized
    as image and label pairs.
    
    Args:
        - dataset (tf.data.Dataset): A dataset object containing image and
            optionally label pairs.
        - filepath (str): The path to the output TFRecord file.
        - image_format (str): The format of the images in the dataset. It
            can be either 'png' or 'jpeg'.
    """
```

## Tests Folder

This folder contains numerous test scripts, such as `test_runner.py`, `create_dataset_test.py`, `split_dataset_test.py`, `enhance_dataset_test.py`, `tfrecord_serialization_test.py`, `save_images_test.py`, and `label_manager_test.py` for evaluating the performance of the code. 

Due to their extensive nature, we're not attaching each test case here but it is crucial to note that they significantly contribute to ensuring the codebase’s robustness.

## Helpers Folder

This folder contains utility functions used throughout the dataset handling functionality.