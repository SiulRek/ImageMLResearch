import os

import tensorflow as tf

from imlresearch.src.data_handling.data_handler import DataHandler
from imlresearch.src.experimenting.experiment import Experiment
from imlresearch.src.experimenting.helpers.load_experiment_definition import (
    load_experiment_definition,
)
from imlresearch.src.plotting.plotters.multi_class_plotter import (
    MultiClassPlotter,
)
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.training.trainer import Trainer


def load_dataset():
    """
    Loads the MNIST digits dataset from keras.datasets and creates a
    tf.data.Dataset object.

    Returns:
        - tf.data.Dataset: The MNIST digits dataset.
    """
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()

    X_train = X_train / 255
    X_test = X_test / 255

    X = tf.concat([X_train, X_test], axis=0)
    X = tf.stack([X] * 3, axis=-1)
    Y = tf.concat([Y_train, Y_test], axis=0)
    Y = tf.one_hot(Y, 10)

    dataset = tf.data.Dataset.from_tensor_slices((X, Y))
    return dataset


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
            tf.keras.layers.Dense(
                hyperparameters["units1"], activation="relu"
            ),
            tf.keras.layers.Dense(
                hyperparameters["units2"], activation="relu"
            ),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=hyperparameters["learning_rate"]
        ),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def make_experiment(experiment_metadata, trial_definitions):
    """
    Runs the experiment with the given trial definitions using the researcher
    class.

    Args:
        - experiment_metadata (dict): A dictionary containing experiment
            details.
        - trial_definitions (list): A list of trial definitions.
    """
    # Experiment Setup
    research_attributes = ResearchAttributes(
        label_type="multi_class",
        class_names=[f"Digit {i}" for i in range(10)],
    )
    data_handler = DataHandler()
    trainer = Trainer()
    plotter = MultiClassPlotter()

    data_handler.synchronize_research_attributes(research_attributes)
    dataset = load_dataset()
    data_handler.load_dataset(dataset)
    data_handler.prepare_datasets(batch_size=32, shuffle_seed=42)
    data_handler.split_dataset(train_split=0.8, val_split=0.1, test_split=0.1)

    # Experiment Execution
    with Experiment(data_handler, **experiment_metadata) as experiment:
        for trial_definition in trial_definitions:
            with experiment.run_trial(**trial_definition) as trial:
                if trial.already_runned:
                    continue
                model = make_model(trial_definition["hyperparameters"])
                trainer.synchronize_research_attributes(experiment)
                trainer.set_compiled_model(model)
                trainer.fit_predict_evaluate(
                    epochs=10, steps_per_epoch=32, validation_steps=32
                )

                plotter.synchronize_research_attributes(trainer)
                plotter.plot_model_summary()
                plotter.plot_training_history(title="Training History")
                plotter.plot_results(grid_size=(4, 3), prediction_bar=True)

                experiment.synchronize_research_attributes(plotter)


if __name__ == "__main__":
    json_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "definition.json"
    )
    experiment_metadata, trial_definitions = load_experiment_definition(
        json_path
    )
    make_experiment(experiment_metadata, trial_definitions)
