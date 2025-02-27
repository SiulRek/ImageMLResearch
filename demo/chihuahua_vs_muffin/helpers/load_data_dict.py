import os

import numpy as np
import tensorflow as tf

from imlresearch.data_handling.io.create_dataset import create_dataset
from imlresearch.data_handling.tfrecord_serialization.deserialize import (
    deserialize_dataset_from_tfrecord,
)
from imlresearch.data_handling.tfrecord_serialization.serialize import (
    serialize_dataset_to_tf_record,
)

LABEL_TYPE = "multi_class"

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TFRECORD_PATH = os.path.join(DATA_DIR, "chihuahua_vs_muffin.tfrecord")


def load_chihuahua_vs_muffin_dict():
    data_dict = {"chihuahua": [], "muffin": []}

    for split in ["train", "validation"]:
        for class_name in ["chihuahua", "muffin"]:
            class_dir = os.path.join(DATA_DIR, split, class_name)
            if os.path.exists(class_dir):
                data_dict[class_name].extend(
                    [os.path.join(class_dir, img) for img in os.listdir(class_dir)]
                )

    # Make a dict with entry 'paths' and 'labels'
    new_data_dict = {
        "path": data_dict["chihuahua"] + data_dict["muffin"],
        "label": [0] * len(data_dict["chihuahua"]) + [1] * len(data_dict["muffin"]),
    }

    return new_data_dict


def load_chihuahua_vs_muffin_dataset():
    if not os.path.exists(TFRECORD_PATH):
        data_dict = load_chihuahua_vs_muffin_dict()
        
        # shuffle data_dict
        length = len(data_dict["path"])
        indices = np.arange(length)
        np.random.seed(42)
        np.random.shuffle(indices)
        data_dict["path"] = np.array(data_dict["path"])[indices].tolist()
        data_dict["label"] = np.array(data_dict["label"])[indices].tolist()

        dataset = create_dataset(
            data_dict, label_type=LABEL_TYPE, class_names=["chihuahua", "muffin"]
        )
        serialize_dataset_to_tf_record(dataset, TFRECORD_PATH, "jpeg")
    else:
        dataset = deserialize_dataset_from_tfrecord(
            TFRECORD_PATH, label_dtype=tf.float32
        )
    return dataset


if __name__ == "__main__":
    dataset = load_chihuahua_vs_muffin_dataset()
