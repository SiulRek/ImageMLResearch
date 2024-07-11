import tensorflow as tf

from src.research.attributes.research_attributes import ResearchAttributes
from src.training.evaluating.compute_classification_metrics import (
    compute_classification_metrics,
)
from src.utils import unbatch_dataset_if_batched


class Trainer(ResearchAttributes):
    """ A class to train a Keras model using datasets from research_attributes. """

    def __init__(self):
        """ Initializes the Trainer. """
        super().__init__()

        # Initialize research attributes used in the Trainer
        self._datasets_container = {
            # Dataset name: Dataset
        }  # Read
        self._model = None  # Read and write
        self._outputs_container = {
            # Output name: Tuple -> (y_true, y_pred)    
        }  # Read and write
        self._training_history = None  # Write
        self._evaluation_metrics = None  # Write

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

    def _evaluate(self):
        """
        Evaluates the model using the predictions and true labels from the
        outputs and datasets containers. Uses 'test_dataset' if available, else
        'complete_dataset'.
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
            not "complete_output" in self._outputs_container
            and not "test_output" in self._outputs_container
        ):
            msg = "Neither 'complete_output' nor 'test_output' found"
            msg += "in outputs container to evaluate."
            raise ValueError(msg)

        outputs = self._outputs_container.get("test_output")
        if outputs is None:
            outputs = self._outputs_container.get("complete_output")
        y_true, y_pred = outputs
        class_names = self.label_manager.class_names
        self._evaluation_metrics = compute_classification_metrics(
            y_true, y_pred, class_names
        )

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
        dataset = unbatch_dataset_if_batched(dataset)

        labels_list = []
        for _, labels in dataset:
            labels_list.append(tf.expand_dims(labels, axis=0))
        labels_tensor = tf.concat(labels_list, axis=0)
        return labels_tensor

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
            msg = "Neither 'train_dataset' nor 'complete_dataset' found in"
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

        outputs_mapping = {
            "train_output": train_dataset,
            "val_output": val_dataset,
            "test_output": test_dataset,
            "complete_output": complete_dataset,
        }

        for output_name, dataset in outputs_mapping.items():
            if dataset:
                dataset_name = output_name.replace("output", "dataset")
                y_pred = self.model.predict(dataset)
                y_true = self._get_labels_tensor(dataset_name)
                outputs = (y_true, y_pred)
                self._outputs_container[output_name] = outputs
        self._evaluate()
