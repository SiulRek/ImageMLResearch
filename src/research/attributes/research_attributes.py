from src.data_handling.labelling.label_manager import LabelManager
from src.research.attributes.attributes_utils import copy_public_properties


class ResearchAttributes:
    """
    A class to store attributes shared between modules in the research package.

    Attributes:
        - datasets_container (dict): Dictionary containing datasets. When
            creating new 'complete_dataset' is added, when split
            'train_dataset', 'val_dataset', and 'test_dataset' are added.
        - label_manager (LabelManager): LabelManager instance for handling
            labels.
        - outputs_container (dict): Dictionary containing outputs in form of
            Tuple -> (y_true, y_pred). When fitting, outputs are added. The name
            corresponds to the dataset name replacing 'dataset' with 'outputs',
            e.g. 'train_dataset' -> 'train_outputs'.
        - model (tf.keras.Model): The Keras model instance.
        - training_history (dict): The tracked training history of the model
            after fitting (Attribute 'history' of the return value).
        - evaluation_metrics (dict): The tracked evaluation metrics dicts of
            the model after evaluating. Can be set from outside.
        - Format {Set_Name: Metrics ({Metric: Value})}
        - figures (dict): Dictionary containing the tracked figures. Format
        - {figure_name: figure}. Can be set from outside.
    """

    def __init__(self, label_type=None, class_names=None):
        """
        Initializes the ResearchAttributes with optional label type and class
        names.

        Args:
            - label_type (str, None): The type of labels used: 'binary',
                'multi_class', 'multi_label', 'multi_label_multi_class',
                'object_detection'. If None, the label_manager is initialized to
                None.
            - class_names (list, optional): The list of class names.
        """
        self._datasets_container = {}
        self._label_manager = (
            LabelManager(label_type, class_names) if label_type else None
        )
        self._outputs_container = {}
        self._model = None
        self._training_history = None
        self._evaluation_metrics = {}
        self._figures = {}

    @property
    def datasets_container(self):
        """ Dictionary containing datasets of type tf.data.Dataset, where each
        sample is a tuple (image, label). """
        return self._datasets_container

    @property
    def label_manager(self):
        """ LabelManager instance for handling labels. """
        return self._label_manager

    @property
    def outputs_container(self):
        """ Dictionary containing outputs in form of Tuple -> (y_true, y_pred). """
        return self._outputs_container

    @property
    def model(self):
        """ The Keras model instance. """
        return self._model

    @property
    def training_history(self):
        """ The training history of the model after fitting. """
        return self._training_history

    @property
    def evaluation_metrics(self):
        """ The evaluation metrics dicts of the model after evaluating. """
        return self._evaluation_metrics

    @property
    def figures(self):
        """ Dictionary containing figures. {figure_name: figure} """
        return self._figures

    def synchronize_research_attributes(self, research_attributes):
        """
        Synchronizes the attributes of the instance with the attributes of the
        ResearchAttributes instance named `research_attributes`.

        Args:
            - instance: The class instance to insert attributes into.
        """
        if not isinstance(research_attributes, ResearchAttributes):
            msg = "The input instance must be of type ResearchAttributes."
            raise ValueError(msg)
        copy_public_properties(research_attributes, self)

    def reset_research_attributes(self, except_datasets=False):
        """
        Resets the research attributes. Note 'label_manager' is unchanged, as it
        should not be changed after initialization.

        Args:
            - except_datasets (bool, optional): If True, the datasets are
                not reset.
        """
        if not except_datasets:
            self._datasets_container.clear()
        self._outputs_container.clear()
        self._model = None
        self._training_history = None
        self._evaluation_metrics.clear()
        self._figures.clear()
