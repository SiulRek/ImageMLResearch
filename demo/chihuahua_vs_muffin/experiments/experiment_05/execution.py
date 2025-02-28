import os

import tensorflow as tf

from demo.chihuahua_vs_muffin.helpers.check_experiment_dir import check_experiment_dir
from demo.chihuahua_vs_muffin.helpers.load_data_dict import (
    load_chihuahua_vs_muffin_dict,
)
from imlresearch import load_experiment_definition
from imlresearch import MultiClassResearcher
from imlresearch.preprocessing_steps import ReverseScaler, TypeCaster, ShapeResizer


def create_preprocessing_pipeline():
    pipeline = [
        ShapeResizer(desired_shape=(128, 128)),
        ReverseScaler(255),
        TypeCaster(output_dtype="float32"),
    ]
    return pipeline


def make_model(hyperparameters):
    """
    Creates and compiles a model using a pretrained MobileNetV2 base with custom
    dense layers on top.

    Args:
        - hyperparameters (dict): A dictionary containing model
            hyperparameters.

    Returns:
        - model: A compiled tf.keras model.
    """
    # Load the pretrained MobileNetV2 model without the top layer
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(128, 128, 3), include_top=False, weights="imagenet"
    )

    # Freeze the base model to prevent its weights from being updated during
    # training
    base_model.trainable = False

    # Build the new model on top of the pretrained base
    model = tf.keras.models.Sequential(
        [
            base_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(hyperparameters["dense_units"], activation="relu"),
            tf.keras.layers.Dropout(hyperparameters["dropout_rate"]),
            tf.keras.layers.Dense(2, activation="softmax"),
        ]
    )

    # Compile the model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=hyperparameters["learning_rate"]
        ),
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
    epochs = 25
    batch_size = 128
    train_size = 0.7
    val_size = 0.15
    test_size = 0.15

    # Early stopping configuration early_stopping =
    # tf.keras.callbacks.EarlyStopping( monitor="val_loss", patience=4,
    # restore_best_weights=True )

    # Experiment Setup
    researcher = MultiClassResearcher(class_names=["chihuahua", "muffin"])
    data = load_chihuahua_vs_muffin_dict()
    researcher.load_dataset(data)
    preprocessing_pipe = create_preprocessing_pipeline()
    researcher.apply_preprocessing_pipeline(preprocessing_pipe)
    researcher.prepare_datasets(batch_size=batch_size, shuffle_seed=42)
    researcher.split_dataset(
        train_split=train_size, val_split=val_size, test_split=test_size
    )

    # Experiment Execution
    with researcher.run_experiment(**experimant_metadata) as experiment:
        for trial_definitions in trial_definitions:
            with experiment.run_trial(**trial_definitions) as trial:
                if trial.already_runned:
                    continue
                model = make_model(trial_definitions["hyperparameters"])
                researcher.set_compiled_model(model)
                researcher.fit_predict_evaluate(
                    epochs=epochs,
                    batch_size=batch_size,
                    # callbacks=[early_stopping],  # Add early stopping callback
                )

                researcher.plot_model_summary()
                researcher.plot_confusion_matrix()
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
