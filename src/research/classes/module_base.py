from src.data_handling.labelling.label_manager import LabelManager


class ModuleBase:
    """ A base class for all modules in the research package. """

    def __init__(self, label_type, category_names=None):
        """
        Initializes the ModuleBase with optional label type and category names.

        Args:
            - label_type (str): The type of labels used: 'binary',
                'categorical', 'multi_label', 'multi_label_multi_class',
                'object_detection'.
            - category_names (list, optional): The list of category names.
        """
        self._dataset_container = {}
        self._label_manager = LabelManager(label_type, category_names)
        self._label_type = label_type
        self._category_names = category_names
        self._training_history = None

    @property
    def dataset_container(self):
        """
        Dictionary containing datasets. When creating new 'complete_dataset' is
        added, when splitted 'train_dataset', 'val_dataset', and 'test_dataset'
        are added.
        """
        return self._dataset_container

    @property
    def label_manager(self):
        """ LabelManager instance for handling labels. """
        return self._label_manager

    @property
    def label_type(self):
        """ The type of labels used: 'binary', 'categorical', 'multi_label',
        'multi_label_multi_class', 'object_detection'. """
        return self._label_type

    @property
    def category_names(self):
        """ The list of category names. """
        return self._category_names

    @property
    def training_history(self):
        """ The training history of the model after fitting. """
        return self._training_history
