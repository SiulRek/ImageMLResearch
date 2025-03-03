import warnings

import tensorflow as tf

from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.training.evaluating.evaluate import (
    get_evaluation_function,
)


class Trainer(ResearchAttributes):
    """
    A class to train a Keras model using datasets from research_attributes.
    """

    def __init__(self):
        """Initializes the Trainer."""
        # Not initializing ResearchAttributes here, prefer calling
        # synchronize_research_attributes explicitly.
        # super().__init__()

        # Initialize research attributes used in the Trainer
        self._datasets_container = {}  # Read
        self._label_manager = None  # Read
        self._model = None  # Read and write
        self._outputs_container = {}  # Read and write
        self._training_history = {}  # Write
        self._evaluation_metrics = {}  # Write

    def set_compiled_model(self, model):
        """
        Sets the compiled Keras model for training.

        Args:
            - model (tf.keras.Model): Compiled Keras model.
        """
        self._model = model

    def _assert_datasets_batched(self):
        """Ensures that datasets are batched correctly."""
        for name, dataset in self.datasets_container.items():
            dataset = self.datasets_container[name]
            if dataset and dataset.element_spec[0].shape.ndims != 4:
                msg = f"Dataset '{name}' must be batched and have 4 dimensions."
                raise ValueError(msg)

    def _evaluate_outputs(self):
        """
        Evaluates the outputs of the model using the appropriate evaluation
        function based on the label type.
        """
        if "test_output" not in self._outputs_container:
            warnings.warn("No test output found for evaluation.")

        label_type = self._label_manager.label_type
        class_names = self._label_manager.class_names
        eval_func = get_evaluation_function(label_type)
        evaluation_metrics = {}
        self._evaluation_metrics.clear()

        for output_name, outputs in self._outputs_container.items():
            if outputs:
                name = output_name.replace("_output", "")
                y_true, y_pred = outputs
                cn_kwarg = {"class_names": class_names} if class_names else {}
                evaluation_metrics[name] = eval_func(
                    y_true, y_pred, **cn_kwarg
                )

        self._evaluation_metrics.update(evaluation_metrics)

    def _get_labels_tensor(self, dataset_name):
        """
        Gets the labels from the dataset.

        Args:
            - dataset_name (str): Name of the dataset in the container.

        Returns:
            - tf.Tensor: Labels from the dataset.
        """
        dataset = self._datasets_container[dataset_name]
        labels = dataset.map(lambda x, y: y)
        labels_tensor = tf.concat(list(labels), axis=0)
        return labels_tensor

    def fit_predict_evaluate(self, **kwargs):
        """
        Fits the model, saves training history, predicts outputs, and evaluates.

        Requires a 'train_dataset' for training. Optionally, a 'val_dataset'
        can be provided for validation, and a 'test_dataset' for evaluation.

        Args:
            - **kwargs: Keyword arguments for the Keras model's fit method.
        """
        if self._model is None:
            raise ValueError("A compiled model must be set before calling fit.")

        self._assert_datasets_batched()

        train_dataset = self._datasets_container.get("train_dataset", None)
        val_dataset = self._datasets_container.get("val_dataset", None)
        complete_dataset = self._datasets_container.get(
            "complete_dataset", None
        )
        test_dataset = self._datasets_container.get("test_dataset", None)

        if train_dataset is None and complete_dataset:
            raise ValueError(
                "No train dataset provided. Probably no split done."
            )  # Fixed line length
        if train_dataset is None:
            raise ValueError(
                "No train dataset provided. Consider loading a dataset."
            )  # Fixed line length

        if val_dataset:
            kwargs["validation_data"] = val_dataset

        fit_dataset = train_dataset if train_dataset else complete_dataset
        history = self._model.fit(fit_dataset, **kwargs)
        self._training_history.update(history.history)

        outputs_mapping = {
            "train_output": train_dataset,
            "val_output": val_dataset,
            "test_output": test_dataset,
        }

        for output_name, dataset in outputs_mapping.items():
            if dataset:
                dataset_name = output_name.replace("output", "dataset")
                y_pred = self._model.predict(dataset)
                y_true = self._get_labels_tensor(dataset_name)
                self._outputs_container[output_name] = (y_true, y_pred)

        self._evaluate_outputs()
