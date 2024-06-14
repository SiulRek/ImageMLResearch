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
        "categorical": tf.float32,
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
                Supported types are 'binary', 'categorical', 'multi_label',
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
        if not category_names and self._label_type == "categorical":
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
                Supported types are 'binary', 'categorical', 'multi_label',
                'multi_class_multi_label', and 'object_detection'.
        """

        def raise_exception_when_called(exception, msg):
            def wrapper(_):
                raise exception(msg)

            return wrapper

        label_encoders = {
            "binary": self.encode_binary_label,
            "categorical": self.encode_categorical_label,
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

        label_to_digit_converters = {
            "binary": self.convert_label_to_digit,
            "categorical": self.convert_categorical_label_to_digit,
            "multi_label": raise_exception_when_called(
                ValueError, "Cannot convert multi-label to digit."
            ),
            "multi_class_multi_label": raise_exception_when_called(
                ValueError, "Cannot convert multi-class multi-label to digit."
            ),
            "object_detection": raise_exception_when_called(
                ValueError, "Cannot convert object detection label to digit."
            ),
        }

        if label_type not in label_encoders:
            msg = f"The label type '{label_type}' is not supported."
            raise ValueError(msg)

        self._encode_label_func = label_encoders[label_type]
        self._convert_label_to_digit_func = label_to_digit_converters[label_type]

    def convert_to_numeric(self, label):
        """
        Converts a label to a numeric format in the case of string labels. If it
        is not a string, it returns the label as is (assuming it is already in
        numeric format).

        Args:
            - label (str or int): The label to convert.

        Returns:
            - int: The label in numeric format.
        """
        if not isinstance(label, str):
            return label
        try:
            return int(label)
        except ValueError:
            pass
        try:
            return self.category_names.index(label)
        except ValueError as e:
            msg = "The label is not in the list of category names."
            raise ValueError(msg) from e

    def encode_label(self, label):
        """
        Encodes a label based on the label type and category names specified
        during initialization to a tensor format.

        Args:
            - label (int): The label to encode.

        Returns:
            - tf.Tensor: A TensorFlow constant of the encoded label.
        """
        return self._encode_label_func(label)

    def encode_binary_label(self, label):
        """
        Encodes a binary label into a format suitable for binary classification.

        Args:
            - label (int): The label to encode.

        Returns:
            - tf.Tensor: A TensorFlow constant of the label in binary
                format.
        """
        try:
            label = self.convert_to_numeric(label)
            if label not in [0, 1]:
                msg = "The label is invalid for binary classification."
                raise ValueError(msg)
            label = tf.constant(label, dtype=self._label_dtype)
            return label
        except ValueError as e:
            msg = "The label should be convertible to an integer."
            raise ValueError(msg) from e

    def encode_categorical_label(self, label):
        """
        Encodes a categorical label into one-hot encoded format.

        Args:
            - label (int): The label to encode.

        Returns:
            - tf.Tensor: A one-hot encoded TensorFlow constant of the label.
        """
        try:
            label = self.convert_to_numeric(label)
            label = tf.constant(label, dtype=tf.int8)
            label = tf.one_hot(label, self.num_categories)
            label = tf.cast(label, self._label_dtype)
            return label
        except ValueError as e:
            msg = "The label should be convertible to an integer."
            raise ValueError(msg) from e
        except tf.errors.OpError as e:
            msg = "The number of categories is probably invalid."
            raise ValueError(msg) from e

    def numeric_to_category(self, numeric):
        """
        Converts a numeric label to a category name.

        Args:
            - numeric (numeric): The numeric label to convert.

        Returns:
            - str: The category name corresponding to the numeric label.
        """
        if not self.category_names:
            msg = "No category names are provided for label decoding."
            raise ValueError(msg)
        try:
            numeric = numeric.numpy()
        except AttributeError:
            pass
        try:
            numeric = int(numeric)
            return self.category_names[numeric]
        except IndexError as e:
            msg = "The label is out of bounds for the category names."
            raise ValueError(msg) from e
        except ValueError as e:
            msg = "The label should be convertible to an integer."
            raise ValueError(msg) from e

    def convert_label_to_digit(self, label):
        """
        Converts a label to a digit.

        Args:
            - label: The label to convert.

        Returns:
            - int: The digit corresponding to the label.
        """
        return self._convert_label_to_digit_func(label)

    def convert_categorical_label_to_digit(self, label):
        """ Converts a categorical label to a digit. """
        return tf.argmax(label).numpy()
