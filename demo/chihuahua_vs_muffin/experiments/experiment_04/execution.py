import os

import tensorflow as tf

from demo.chihuahua_vs_muffin.helpers.check_experiment_dir import check_experiment_dir
from demo.chihuahua_vs_muffin.helpers.load_data_dict import (
    load_chihuahua_vs_muffin_dataset,
)
from src.experimenting.helpers.load_experiment_definition import (
    load_experiment_definition,
)
import src.preprocessing.steps as pp_steps
from src.research.researchers import MultiClassResearcher

# tf.config.set_visible_devices([], 'GPU')


def create_resizing_pipeline(shape):
    return [pp_steps.ShapeResizer(desired_shape=shape)]


def create_data_augmenting_pipeline(crop_size):
    pipeline = [
        pp_steps.RandomCropper(crop_size=crop_size),
        pp_steps.RandomFlipper(flip_direction="horizontal"),
        pp_steps.RandomRotator(angle_range=[-10, 10]),
        pp_steps.RandomPerspectiveTransformer(warp_scale=0.1),
    ]
    return pipeline


def create_normalizing_pipeline(hyperparameters):
    normalization_mapping = {
        "min_max": pp_steps.MinMaxNormalizer(),
        "standard": pp_steps.StandardNormalizer(),
        "mean": pp_steps.MeanNormalizer(),
    }
    pipeline = [
        normalization_mapping[hyperparameters["normalization"]],
        pp_steps.TypeCaster(output_dtype="float32"),
    ]
    return pipeline


def make_model(hyperparameters):
    """
    Creates and compiles a model with hardcoded hyperparameters.

    Returns:
        - model: A compiled tf.keras model.
    """
    # Hardcoded kernel sizes and other hyperparameters
    shape = (128, 128, 3)
    kernel_size1 = (5, 5)
    kernel_size2 = (7, 7)
    units1 = 128
    units2 = 64
    dense_units = 128
    dropout_rate = 0.15073888319621384
    learning_rate = hyperparameters["learning_rate"]

    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Input(shape=shape),
            tf.keras.layers.Conv2D(units1, kernel_size=kernel_size1, activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Conv2D(units2, kernel_size=kernel_size2, activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Conv2D(units2, kernel_size=kernel_size2, activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(dense_units, activation="relu"),
            tf.keras.layers.Dropout(dropout_rate),
            tf.keras.layers.Dense(dense_units, activation="relu"),
            tf.keras.layers.Dropout(dropout_rate),
            tf.keras.layers.Dense(2, activation="softmax"),
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model


def make_experiment(experimant_metadata, trial_definitions):
    """
    Runs the experiment with the given trial definitions using the researcher
    class.

    Args:
        - experiment_metadata (dict): A dictionary containing experiment
            details.
        - trial_definitions (list): A list of trial definitions.
    """
    # Configurations
    data_len = 4733
    epochs = 15
    train_split = 0.7
    val_split = 0.15
    test_split = 0.15
    resolution = (128, 128)
    pre_crop_resolution = (160, 160)

    # Experiment Setup
    researcher = MultiClassResearcher(class_names=["chihuahua", "muffin"])
    dataset = load_chihuahua_vs_muffin_dataset()
    researcher.load_dataset(dataset)
    researcher.split_dataset(
        train_split=train_split,
        val_split=val_split,
        test_split=test_split,
        dataset_size=data_len,
    )

    # Resize shapes
    shape_resizing_pipe = create_resizing_pipeline(resolution)
    researcher.apply_preprocessing_pipeline(
        shape_resizing_pipe, dataset_names=["val_dataset", "test_dataset"]
    )

    # Data Augmentation
    researcher.prepare_datasets(
        repeat_num=2, dataset_names=["train_dataset"], prefetch_buffer_size=None
    )
    data_augmenting_pipe = create_resizing_pipeline(
        pre_crop_resolution
    ) + create_data_augmenting_pipeline(resolution)
    researcher.apply_preprocessing_pipeline(
        data_augmenting_pipe, dataset_names=["train_dataset"]
    )

    # Experiment Execution
    with researcher.run_experiment(**experimant_metadata) as experiment:
        for trial_definitions in trial_definitions:
            with experiment.run_trial(**trial_definitions) as trial:
                if trial.already_runned:
                    continue
                hyperparameters = trial_definitions["hyperparameters"]
                print(f"Running trial with hyperparameters: {hyperparameters}")
                batch_size = hyperparameters["batch_size"]

                try:
                    researcher.restore_datasets()
                except ValueError:
                    pass

                normalizing_pipe = create_normalizing_pipeline(hyperparameters)
                researcher.apply_preprocessing_pipeline(normalizing_pipe, backup=True)
                researcher.prepare_datasets(
                    batch_size=batch_size, prefetch_buffer_size=None
                )

                model = make_model(hyperparameters)
                researcher.set_compiled_model(model)
                researcher.fit_predict_evaluate(
                    epochs=epochs,
                    batch_size=batch_size,
                )

                researcher.plot_training_history(title="Training History")

            del model
            tf.keras.backend.clear_session()


if __name__ == "__main__":
    json_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "definition.json"
    )
    experiment_metadata, trial_definitions = load_experiment_definition(json_path)
    check_experiment_dir(experiment_metadata)
    make_experiment(experiment_metadata, trial_definitions)
