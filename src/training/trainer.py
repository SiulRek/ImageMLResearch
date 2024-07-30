import warnings

import tensorflow as tf

from src.research.attributes.research_attributes import ResearchAttributes
from src.training.evaluating.evaluate import get_evaluation_function


class Trainer(ResearchAttributes):
    """ A class to train a Keras model using datasets from research_attributes. """

    def __init__(self):
        """ Initializes the Trainer. """
        # Not initializing ResearchAttributes here,
        # prefer call synchronize_research_attributes explicitly.
        # super().__init__()

        # Initialize research attributes used in the Trainer
        self._datasets_container = {
            # Dataset name: Dataset
        }  # Read
        self._label_manager = None  # Read
        self._model = None  # Read and write
        self._outputs_container = {
            # Output name: Tuple -> (y_true, y_pred)
        }  # Read and write
        self._training_history = {
            # Metric: List of values
        }  # Write
        self._evaluation_metrics = {
            # Set Name: Metrics -> {Metric: Value}
        }  # Write

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

    def _evaluate_outputs(self):
        """ Evaluates the outputs of the model using the appropriate evaluation
        function based on the label type. """
        if not "test_output" in self._outputs_container:
            msg = "No test output found for evaluation."
            warnings.warn(msg)

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
                evaluation_metrics[name] = eval_func(y_true, y_pred, **cn_kwarg)
        self._evaluation_metrics.update(evaluation_metrics)

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

        labels = dataset.map(lambda x, y: y)
        labels_tensor = tf.concat(list(labels), axis=0)
        return labels_tensor

    def fit_predict_evaluate(self, **kwargs):
        """
        Fits the model to the training dataset, saves the training history,
        calculates predictions, and evaluates the model.

        The method requires a 'train_dataset' for training. Optionally, a
        'val_dataset' can be provided for validation during training, and a
        'test_dataset' can be provided for evaluation.

        Args:
            - **kwargs: Keyword arguments for the Keras model's fit method.
        """
        if self._model is None:
            msg = "A compiled model must be set before calling fit."
            raise ValueError(msg)

        self._assert_datasets_batched()

        train_dataset = self._datasets_container.get("train_dataset", None)
        val_dataset = self._datasets_container.get("val_dataset", None)
        complete_dataset = self._datasets_container.get("complete_dataset", None)
        test_dataset = self._datasets_container.get("test_dataset", None)

        if train_dataset is None and complete_dataset:
            msg = "No train dataset provided. Probably no split done."
            raise ValueError(msg)
        if train_dataset is None:
            msg = "No train dataset provided. Consider loading a dataset,"
            msg += "before fitting."
            raise ValueError(msg)
        if val_dataset:
            kwargs["validation_data"] = val_dataset  # Add to fit kwargs.

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
                outputs = (y_true, y_pred)
                self._outputs_container[output_name] = outputs

        self._evaluate_outputs()
