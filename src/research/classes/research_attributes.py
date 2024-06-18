from src.data_handling.labelling.label_manager import LabelManager


class ResearchAttributes:
    """
    A class to store attributes used by modules in the research package.

    Attributes:
        - dataset_container (dict): Dictionary containing datasets. When
            creating new 'complete_dataset' is added, when split
            'train_dataset', 'val_dataset', and 'test_dataset' are added.
        - label_manager (LabelManager): LabelManager instance for handling
            labels.
        - predictions_container (dict): Dictionary containing predictions.
            When fitting, predictions are added. The name corresponds to the
            dataset name replacing 'dataset' with 'predictions', e.g.
            'train_dataset' -> 'train_predictions'.
        - model (tf.keras.Model): The Keras model instance.
        - training_history (tf.keras.callbacks.History): The training
            history of the model after fitting.
        - evaluation_metrics (dict): The evaluation metrics dicts of the
            model after evaluating.
    """

    def __init__(self, label_type, category_names=None):
        """
        Initializes the ResearchAttributes with optional label type and category
        names.

        Args:
            - label_type (str): The type of labels used: 'binary',
                'categorical', 'multi_label', 'multi_label_multi_class',
                'object_detection'.
            - category_names (list, optional): The list of category names.
        """
        self._dataset_container = {}
        self._label_manager = LabelManager(label_type, category_names)
        self._predictions_container = {}
        self._model = None
        self._training_history = None
        self._evaluation_metrics = None

    @property
    def dataset_container(self):
        """ Dictionary containing datasets. """
        return self._dataset_container

    @property
    def label_manager(self):
        """ LabelManager instance for handling labels. """
        return self._label_manager

    @property
    def predictions_container(self):
        """ Dictionary containing predictions. """
        return self._predictions_container

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


def insert_research_attributes(instance, research_attributes):
    """
    Inserts the attributes from a ResearchAttributes instance into another class
    instance. Retrieves all public properties from research_attributes and sets
    them as attributes in the instance.

    Args:
        - instance: The class instance to insert attributes into.
        - research_attributes (ResearchAttributes): The ResearchAttributes
            instance.
    """

    def is_property(attr_name):
        cls = research_attributes.__class__
        attr = getattr(cls, attr_name)
        return isinstance(attr, property)

    if not isinstance(research_attributes, ResearchAttributes):
        msg = "research_attributes must be an instance of ResearchAttributes"
        msg += f"not {type(research_attributes)}."
        raise ValueError(msg)

    for attr_name in dir(research_attributes):
        attribute = getattr(research_attributes, attr_name)
        if (
            not attr_name.startswith("_")
            and not callable(attribute)
            and is_property(attr_name)
        ):
            setattr(instance, "_" + attr_name, getattr(research_attributes, attr_name))
