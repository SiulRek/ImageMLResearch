from imlresearch.src.data_handling.labelling.label_manager import LabelManager
from imlresearch.src.research.attributes.attributes_utils import (
    copy_public_properties,
)


class ResearchAttributes:
    """
    Store attributes shared between modules in the research package.

    Attributes
    ----------
    datasets_container : dict
        Dictionary containing datasets. When creating new datasets,
        'complete_dataset' is added; when split, 'train_dataset',
        'val_dataset', and 'test_dataset' are added.
    label_manager : LabelManager
        LabelManager instance for handling labels.
    outputs_container : dict
        Dictionary containing outputs in the form of tuples
        (y_true, y_pred). When fitting, outputs are added. The name
        corresponds to the dataset name replacing 'dataset' with
        'outputs', e.g., 'train_dataset' -> 'train_outputs'.
    model : tf.keras.Model
        The Keras model instance.
    training_history : dict
        The tracked training history of the model after fitting
        (Attribute 'history' of the return value).
    evaluation_metrics : dict
        The tracked evaluation metrics of the model after evaluating.
        Can be set from outside. Format: {Set_Name: {Metric: Value}}.
    figures : dict
        Dictionary containing the tracked figures.
        Format: {figure_name: figure}. Can be set from outside.
    """

    def __init__(self, label_type=None, class_names=None):
        """
        Initialize ResearchAttributes with optional label type and class names.

        Parameters
        ----------
        label_type : str or None, optional
            The type of labels used: 'binary', 'multi_class', 'multi_label',
            'multi_label_multi_class', 'object_detection'. If None,
            label_manager is set to None.
        class_names : list, optional
            The list of class names.
        """
        self._datasets_container = {}
        self._label_manager = (
            LabelManager(label_type, class_names) if label_type else None
        )
        self._outputs_container = {}
        self._model = None
        self._training_history = {}
        self._evaluation_metrics = {}
        self._figures = {}

    @property
    def datasets_container(self):
        """
        Get the dictionary containing datasets.

        Returns
        -------
        dict
            A dictionary of type tf.data.Dataset, where each sample
            is a tuple (image, label).
        """
        return self._datasets_container

    @property
    def label_manager(self):
        """
        Get the LabelManager instance.

        Returns
        -------
        LabelManager
            Instance for handling labels.
        """
        return self._label_manager

    @property
    def outputs_container(self):
        """
        Get the dictionary containing outputs.

        Returns
        -------
        dict
            Dictionary in the form of tuples (y_true, y_pred).
        """
        return self._outputs_container

    @property
    def model(self):
        """
        Get the Keras model instance.

        Returns
        -------
        tf.keras.Model
            The Keras model instance.
        """
        return self._model

    @property
    def training_history(self):
        """
        Get the training history of the model after fitting.

        Returns
        -------
        dict
            Dictionary tracking the model's training history.
        """
        return self._training_history

    @property
    def evaluation_metrics(self):
        """
        Get the evaluation metrics dictionary of the model after evaluating.

        Returns
        -------
        dict
            Tracked evaluation metrics with format {Set_Name: {Metric: Value}}.
        """
        return self._evaluation_metrics

    @property
    def figures(self):
        """
        Get the dictionary containing figures.

        Returns
        -------
        dict
            Dictionary containing figures in the format {figure_name: figure}.
        """
        return self._figures

    def synchronize_research_attributes(self, research_attributes):
        """
        Synchronize research attributes with another ResearchAttributes
        instance.

        Parameters
        ----------
        research_attributes : ResearchAttributes
            The instance to synchronize with.
        """
        if not isinstance(research_attributes, ResearchAttributes):
            raise ValueError(
                "The input instance must be of type ResearchAttributes."
            )
        copy_public_properties(research_attributes, self)

    def reset_research_attributes(self, except_datasets=False):
        """
        Reset research attributes while preserving the label manager.

        Parameters
        ----------
        except_datasets : bool, optional
            If True, datasets are not reset, by default False.
        """
        if not except_datasets:
            self._datasets_container.clear()
        self._outputs_container.clear()
        self._model = None
        self._training_history.clear()
        self._evaluation_metrics.clear()
        self._figures.clear()
