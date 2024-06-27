import tensorflow as tf

from src.research.attributes.research_attributes import ResearchAttributes
from src.training.evaluating.compute_classification_metrics import (
    compute_classification_metrics,
)


class Trainer(ResearchAttributes):
    """ A class to train a Keras model using datasets from research_attributes. """

    def __init__(self):
        """ Initializes the Trainer. """
        self._model = None  # Read and write
        self._predictions_container = {}  # Read and write
        self._training_history = None  # Write
        self._evaluation_metrics = None  # Write
        self._datasets_container = {}  # Read

    def set_compiled_model(self, model):
        """
        Sets the compiled Keras model for training.

        Args:
            - model (tf.keras.Model): Compiled Keras model.
        """
        self._model = model

    def _assert_datasets_batched(self):
        for name, dataset in self.datasets_container.items():
            dataset = self.datasets_container[name]
            if dataset and dataset.element_spec[0].shape.ndims != 4:
                msg = f"Dataset '{name}' must be batched and have 4 dimensions."
                raise ValueError(msg)

    def _get_labels_tensor(self, dataset_name):
        """
        Gets the labels from the dataset.

        Args:
            - dataset_name (str): Name of the dataset in the datasets
                container.

        Returns:
            - tf.Tensor: Labels from the dataset.
        """
        dataset = self._datasets_container[dataset_name]
        return tf.concat([y for x, y in dataset], axis=0)

    def _evaluate(self):
        """
        Evaluates the model using the predictions and true labels from the
        predictions and datasets containers. Uses 'test_dataset' if available,
        else 'complete_dataset'.
        """
        if self.label_manager.label_type not in [
            "binary",
            "multi_class",
            "multi_label",
        ]:
            msg = f"Label type '{self.label_manager.label_type}' is not"
            msg += "supported for evaluation."
            raise ValueError(msg)

        if (
            not "complete_predictions" in self._predictions_container
            and not "test_predictions" in self._predictions_container
        ):
            msg = "Neither 'complete_predictions' nor 'test_predictions' found"
            msg += "in predictions container to evaluate."
            raise ValueError(msg)

        dataset_name = (
            "test_dataset"
            if "test_dataset" in self._datasets_container
            else "complete_dataset"
        )
        y_true = self._get_labels_tensor(dataset_name)
        prediction_name = dataset_name.replace("dataset", "predictions")
        y_pred = self._predictions_container[prediction_name]
        class_names = self.label_manager.category_names
        self._evaluation_metrics = compute_classification_metrics(
            y_true, y_pred, class_names
        )

    def fit_predict_evaluate(self, **kwargs):
        """
        Fits the model to the dataset, saves the training history, calculates
        predictions, and evaluates the model.

        If a 'train_dataset' is provided, it is used for training. Otherwise, if
        a 'complete_dataset' is provided, it is used for training. If a
        'val_dataset' is provided, it is used for validation during training. If
        a 'test_dataset' is provided, it is used for evaluation. Otherwise, the
        'complete_dataset' is used for evaluation.

        Args:
            - **kwargs: Keyword arguments for the Keras model's fit method.
        """
        if self.model is None:
            msg = "A compiled model must be set before calling fit."
            raise ValueError(msg)

        self._assert_datasets_batched()

        train_dataset = self._datasets_container.get("train_dataset", None)
        val_dataset = self._datasets_container.get("val_dataset", None)
        complete_dataset = self._datasets_container.get("complete_dataset", None)
        test_dataset = self._datasets_container.get("test_dataset", None)

        if train_dataset is None and complete_dataset is None:
            msg = "Neither 'test_dataset' nor 'complete_dataset' found in"
            msg += "dataset container for training."
            raise ValueError(msg)
        if test_dataset is None and complete_dataset is None:
            msg = "Neither 'test_dataset' nor 'complete_dataset' found in"
            msg += "dataset container for evaluation."
            raise ValueError(msg)

        if val_dataset:
            kwargs["validation_data"] = val_dataset  # Add to fit kwargs.

        fit_dataset = train_dataset if train_dataset else complete_dataset
        self._training_history = self.model.fit(fit_dataset, **kwargs)

        predictions_mapping = {
            "train_predictions": train_dataset,
            "val_predictions": val_dataset,
            "test_predictions": test_dataset,
            "complete_predictions": complete_dataset,
        }

        for name, dataset in predictions_mapping.items():
            if dataset:
                self._predictions_container[name] = self.model.predict(dataset)

        self._evaluate()
