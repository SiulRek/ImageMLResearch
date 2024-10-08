import os

import tensorflow as tf

from src.experimenting.helpers.load_experiment_definition import (
    load_experiment_definition,
)
from src.preprocessing.steps import ReverseScaler, TypeCaster
from src.research.researchers import MultiClassResearcher


def load_dataset():
    """
    Loads the MNIST digits dataset from keras.datasets and creates a
    tf.data.Dataset object.

    Returns:
        - tf.data.Dataset: The MNIST digits dataset.
    """
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()

    X = tf.concat([X_train, X_test], axis=0)
    X = tf.stack([X] * 3, axis=-1)
    Y = tf.concat([Y_train, Y_test], axis=0)
    Y = tf.one_hot(Y, 10)

    dataset = tf.data.Dataset.from_tensor_slices((X, Y))
    return dataset


def create_preprocessing_pipeline():
    return [ReverseScaler(255), TypeCaster(output_dtype="float32")]


def make_model(hyperparameters):
    """
    Creates and compiles a model with the given hyperparameters.

    Args:
        - hyperparameters (dict): A dictionary containing model
            hyperparameters.

    Returns:
        - model: A compiled tf.keras model.
    """
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28, 3)),
            tf.keras.layers.Dense(hyperparameters["units1"], activation="relu"),
            tf.keras.layers.Dense(hyperparameters["units2"], activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=hyperparameters["learning_rate"]
        ),
        loss="categorical_crossentropy",
        metrics="accuracy",
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
    # Experiment Setup
    researcher = MultiClassResearcher(
        class_names=["Digit " + str(i) for i in range(10)]
    )
    dataset = load_dataset()
    researcher.load_dataset(dataset)
    preprocessing_pipe = create_preprocessing_pipeline()
    researcher.apply_preprocessing_pipeline(preprocessing_pipe)
    researcher.prepare_datasets(batch_size=32, shuffle_seed=42)
    researcher.split_dataset(train_size=0.8, val_size=0.1, test_size=0.1)

    # Experiment Execution
    with researcher.run_experiment(**experimant_metadata) as experiment:
        for trial_definitions in trial_definitions:
            with experiment.run_trial(**trial_definitions) as trial:
                if trial.already_runned:
                    continue
                model = make_model(trial_definitions["hyperparameters"])
                researcher.set_compiled_model(model)
                researcher.fit_predict_evaluate(
                    epochs=10, steps_per_epoch=32, validation_steps=32
                )

                researcher.plot_model_summary()
                researcher.plot_training_history(title="Training History")
                researcher.plot_results(grid_size=(4, 3), prediction_bar=True)


if __name__ == "__main__":
    json_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "definition.json"
    )
    experiment_metadata, trial_definitions = load_experiment_definition(json_path)
    make_experiment(experiment_metadata, trial_definitions)
