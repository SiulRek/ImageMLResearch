import tensorflow as tf


class LabelManager:
    """
    Manages different types of label encoding for machine learning models.

    Attributes:
        - category_names (list): The existing category names for label
            encoding.
        - num_categories (int): The number of categories used for
            categorical label encoding.

    Methods:
        - encode_label: Depending on the `label_type`, it delegates to the
            corresponding method to encode labels.
        - decode_label: Decodes a label from a numeric format to a string
            format.
    """

    default_label_dtype = {
        "binary": tf.float32,
        "multi_class": tf.float32,
        "multi_label": tf.float32,
        "multi_class_multi_label": tf.float32,
        "object_detection": tf.float32,
    }

    def __init__(self, label_type, category_names=None, dtype=None):
        """
        Initializes the LabelManager with a specific label encoding type and,
        optionally, the number of categories.

        Args:
            - label_type (str): The type of label encoding to manage.
                Supported types are 'binary', 'multi_class', 'multi_label',
                'multi_class_multi_label', and 'object_detection'.
            - category_names (list, optional): The existing category names
                for label encoding.
            - dtype (tf.DType, optional): The data type of the label.
        """
        self._label_type = label_type
        self.num_categories = None
        self.category_names = None
        self._set_category_params(category_names)
        self._set_label_type_functions(label_type)
        self._label_dtype = dtype or self.default_label_dtype[label_type]

    @property
    def label_type(self):
        """
        Returns the label type of the manager.

        Returns:
            - str: The label type of the manager.
        """
        return self._label_type

    @property
    def label_dtype(self):
        """
        Returns the data type of the label.

        Returns:
            - tf.DType: The data type of the label.
        """
        return self._label_dtype

    def _set_category_params(self, category_names):
        """
        Sets the number of categories based on the category names provided.

        Args:
            - category_names (list): The list of category names.
        """
        if not category_names and self._label_type == "multi_class":
            msg = "The category names are required at least to derive the number of categories."
            raise ValueError(msg)
        if not category_names and self._label_type == "binary":
            self.num_categories = 2
            self.category_names = ["0", "1"]
        elif category_names:
            self.category_names = category_names
            self.num_categories = len(category_names)

    def _set_label_type_functions(self, label_type):
        """
        Sets the label encoder and label to digit converter methods based on the
        label type.

        Args:
            - label_type (str): The type of label encoding to manage.
                Supported types are 'binary', 'multi_class', 'multi_label',
                'multi_class_multi_label', and 'object_detection'.
        """

        def raise_exception_when_called(exception, msg):
            def wrapper(_):
                raise exception(msg)

            return wrapper

        label_encoders = {
            "binary": self._encode_binary_label,
            "multi_class": self._encode_multi_class_label,
            "multi_label": raise_exception_when_called(
                NotImplementedError, "Multi-label encoding is not yet implemented."
            ),
            "multi_class_multi_label": raise_exception_when_called(
                NotImplementedError,
                "Multi-class multi-label encoding is not yet implemented.",
            ),
            "object_detection": raise_exception_when_called(
                NotImplementedError,
                "Object detection label encoding is not yet implemented.",
            ),
        }

        if label_type not in label_encoders:
            msg = f"The label type '{label_type}' is not supported."
            raise ValueError(msg)

        self._encode_label_func = label_encoders[label_type]

    def get_index(self, category_name):
        """
        Returns the index of a category based on its name.

        Args:
            - category_name (str): The name of the category.

        Returns:
            - int: The index of the category.
        """
        category_name = self.category_names.index(category_name)
        if category_name is not None:
            return category_name
        msg = "The category name is not in the category names."
        raise ValueError(msg)

    def _encode_binary_label(self, label):
        """
        Encodes a binary label into a format suitable for binary classification.

        Args:
            - label (int): The label to encode. If string it should be a
                category name.

        Returns: - tf.Tensor: A TensorFlow constant of the label in binary
        format.
        """
        label = self.get_index(label) if isinstance(label, str) else label
        try:
            if label not in [0, 1]:
                msg = "The label is invalid for binary classification."
                raise ValueError(msg)
            label = tf.constant(label, dtype=self._label_dtype)
            return label
        except tf.errors.OpError as e:
            msg = "Failed to convert the label to a tensor."
            raise ValueError(msg) from e

    def _encode_multi_class_label(self, label):
        """
        Encodes a multi_class label into one-hot encoded format.

        Args:
            - label (int|str): The label to encode. If string it should be a
                category name.

        Returns:
            - tf.Tensor: A one-hot encoded TensorFlow constant of the label.
        """
        label = self.get_index(label) if isinstance(label, str) else label
        try:
            label = tf.constant(label, dtype=tf.int8)
            label = tf.one_hot(label, self.num_categories)
            label = tf.cast(label, self._label_dtype)
            return label
        except tf.errors.OpError as e:
            msg = "Failed to encode the label to a tensor."
            raise ValueError(msg) from e

    def encode_label(self, label):
        """
        Encodes a label based on the label type and category_name names
        specified during initialization to a tensor format.

        Args:
            - label (int): The label to encode.

        Returns: - tf.Tensor: A TensorFlow constant of the encoded label.
        """
        return self._encode_label_func(label)

    def get_category(self, index):
        """
        Converts a numeric label to a category_name name.

        Args:
            - index (str|numeric): The category_name index.

        Returns:
            - str: The category_name name corresponding to the numeric
                label.
        """
        if not self.category_names:
            msg = "No category names are provided for label decoding."
            raise ValueError(msg)
        try:
            index = index.numpy()
        except AttributeError:
            pass
        try:
            index = int(index)
            return self.category_names[index]
        except IndexError as e:
            msg = "The label is out of bounds for the category names."
            raise ValueError(msg) from e
        except ValueError as e:
            msg = "The label should be convertible to an integer."
            raise ValueError(msg) from e
