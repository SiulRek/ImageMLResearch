import json
import os

import tensorflow as tf

from src.research.researchers import BinaryResearcher


def load_fashion_mnist_binary():
    """
    Loads the Fashion MNIST dataset from keras.datasets, filters it to include
    only sneakers and ankle boots, and returns the complete dataset.

    Returns:
        - tf.data.Dataset: The filtered Fashion MNIST dataset.
    """
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.fashion_mnist.load_data()

    X = tf.concat([X_train, X_test], axis=0)
    Y = tf.concat([Y_train, Y_test], axis=0)

    # Filter for sneakers (label 7) and ankle boots (label 9)
    filter_mask = (Y == 7) | (Y == 9)
    X, Y = tf.boolean_mask(X, filter_mask), tf.boolean_mask(Y, filter_mask)

    # Map labels 7 -> 0 and 9 -> 1
    Y = tf.where(Y == 9, 1, 0)

    X = tf.cast(X, tf.float32) / 255.0

    # Add a channel dimension
    X = X[..., tf.newaxis]

    dataset = tf.data.Dataset.from_tensor_slices((X, Y))

    return dataset


def make_model(hyperparameters):
    """
    Creates and compiles a binary classification model with the given
    hyperparameters.

    Args:
        - hyperparameters (dict): A dictionary containing model
            hyperparameters.

    Returns:
        - model: A compiled tf.keras model.
    """
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
            tf.keras.layers.Dense(hyperparameters["units1"], activation="relu"),
            tf.keras.layers.Dropout(hyperparameters["dropout1"]),
            tf.keras.layers.Dense(hyperparameters["units2"], activation="relu"),
            tf.keras.layers.Dropout(hyperparameters["dropout2"]),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=hyperparameters["learning_rate"]
        ),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    return model


def make_experiment(experiment_definition, trial_definitions):
    """
    Runs the binary classification experiment with the given trial definitions
    using the BinaryResearcher class.

    Args:
        - experiment_definition (dict): A dictionary containing experiment
            details.
        - trial_definitions (list): A list of trial definitions.
    """
    researcher = BinaryResearcher(class_names=["Sneaker", "Ankle Boot"])
    dataset = load_fashion_mnist_binary()

    researcher.load_dataset(dataset)
    researcher.prepare_datasets(batch_size=32, shuffle_seed=42)
    researcher.split_dataset(train_split=0.8, val_split=0.1, test_split=0.1)

    with researcher.run_experiment(**experiment_definition) as experiment:
        for trial_definition in trial_definitions:
            with experiment.run_trial(**trial_definition) as trial:
                if trial.already_runned:
                    continue
                model = make_model(trial_definition["hyperparameters"])
                researcher.set_compiled_model(model)
                researcher.fit_predict_evaluate(
                    epochs=10, steps_per_epoch=32, validation_steps=32
                )

                researcher.plot_model_summary()
                researcher.plot_training_history(title="Training History")
                researcher.plot_confusion_matrix(title="Confusion Matrix")
                researcher.plot_roc_curve(title="ROC Curve")
                researcher.plot_pr_curve(title="PR Curve")
                researcher.plot_results(grid_size=(3, 3))


if __name__ == "__main__":
    json_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "definition.json"
    )
    with open(json_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    experiment_definition = config["experiment_definition"]
    trial_definitions = config["trial_definitions"]

    make_experiment(experiment_definition, trial_definitions)
