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
        """
        Initialize the Trainer.

        Attributes
        ----------
        _datasets_container : dict
            Dictionary containing datasets.
        _label_manager : LabelManager or None
            Label manager instance for handling labels.
        _model : tf.keras.Model or None
            The compiled Keras model.
        _outputs_container : dict
            Dictionary to store outputs after model predictions.
        _training_history : dict
            Dictionary storing model training history.
        _evaluation_metrics : dict
            Dictionary containing model evaluation metrics.
        """
        # Not initializing ResearchAttributes here, prefer calling
        # synchronize_research_attributes explicitly.

        # Initialize research attributes used in the Trainer
        self._datasets_container = {}  # Read
        self._label_manager = None  # Read
        self._model = None  # Read and write
        self._outputs_container = {}  # Read and write
        self._training_history = {}  # Write
        self._evaluation_metrics = {}  # Write

    def set_compiled_model(self, model):
        """
        Set the compiled Keras model for training.

        Parameters
        ----------
        model : tf.keras.Model
            The compiled Keras model.
        """
        self._model = model

    def _assert_datasets_batched(self):
        """
        Ensure that datasets are batched correctly.

        Raises
        ------
        ValueError
            If a dataset is not batched properly.
        """
        for name, dataset in self.datasets_container.items():
            dataset = self.datasets_container[name]
            if dataset and dataset.element_spec[0].shape.ndims != 4:
                msg = f"Dataset '{name}' must be batched and have 4 dimensions."
                raise ValueError(msg)

    def _evaluate_outputs(self):
        """
        Evaluate model outputs using the appropriate evaluation function
        based on the label type.
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
        Retrieve labels from a dataset.

        Parameters
        ----------
        dataset_name : str
            Name of the dataset in the container.

        Returns
        -------
        tf.Tensor
            Tensor containing labels from the dataset.
        """
        dataset = self._datasets_container[dataset_name]
        labels = dataset.map(lambda x, y: y)
        labels_tensor = tf.concat(list(labels), axis=0)
        return labels_tensor

    def fit_predict_evaluate(self, **kwargs):
        """
        Fit the model, save training history, predict outputs, and evaluate.

        Requires a 'train_dataset' for training. Optionally, a 'val_dataset'
        can be provided for validation, and a 'test_dataset' for evaluation.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments for the Keras model's `fit` method.
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
