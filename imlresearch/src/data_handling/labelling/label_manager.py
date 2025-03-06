import tensorflow as tf


class LabelManager:
    """
    Manages different types of label encoding for machine learning models.

    Attributes
    ----------
    class_names : list
        The existing class names for label encoding.
    num_classes : int
        The number of classes used for multi_class and multi_class_multi_label
        label encoding.

    Methods
    -------
    encode_label(label)
        Encodes a label based on the specified label type.
    decode_label(index)
        Decodes a label from a numeric format to a string format.
    """

    default_label_dtype = {
        "binary": tf.float32,
        "multi_class": tf.float32,
        "multi_label": tf.float32,
        "multi_class_multi_label": tf.float32,
        "object_detection": tf.float32,
    }

    def __init__(self, label_type, class_names=None, dtype=None):
        """
        Initializes the LabelManager with a specific label encoding type
        and, optionally, the number of classes.

        Parameters
        ----------
        label_type : str
            The type of label encoding to manage. Supported types are
            'binary', 'multi_class', 'multi_label',
            'multi_class_multi_label', and 'object_detection'.
        class_names : list, optional
            The existing class names for label encoding.
        dtype : tf.DType, optional
            The data type of the label.
        """
        self._label_type = label_type
        self.num_classes = None
        self.class_names = None
        self._set_class_params(class_names)
        self._set_label_type_functions(label_type)
        self._label_dtype = dtype or self.default_label_dtype[label_type]

    @property
    def label_type(self):
        """Returns the label type of the manager."""
        return self._label_type

    @property
    def label_dtype(self):
        """Returns the data type of the label."""
        return self._label_dtype

    def _set_class_params(self, class_names):
        """
        Sets the number of classes based on the class names provided.

        Parameters
        ----------
        class_names : list
            The list of class names.
        """
        if not class_names and self._label_type == "multi_class":
            msg = (
                "The class names are required at least to derive the number "
                "of classes."
            )
            raise ValueError(msg)
        if not class_names and self._label_type == "binary":
            self.class_names = ["0", "1"]
            self.num_classes = 2
        elif class_names:
            self.class_names = class_names
            self.num_classes = len(class_names)

    def _set_label_type_functions(self, label_type):
        """
        Sets the label encoder and label-to-digit converter methods based on
        the label type.

        Parameters
        ----------
        label_type : str
            The type of label encoding to manage. Supported types are
            'binary', 'multi_class', 'multi_label',
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
                NotImplementedError,
                "Multi-label encoding is not yet implemented.",
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

    def get_index(self, class_name):
        """
        Returns the index of a class based on its name.

        Parameters
        ----------
        class_name : str
            The name of the class.

        Returns
        -------
        int
            The index of the class.
        """
        class_name = self.class_names.index(class_name)
        if class_name is not None:
            return class_name
        msg = "The class name is not in the class names."
        raise ValueError(msg)

    def _encode_binary_label(self, label):
        """
        Encodes a binary label into a format suitable for binary classification.

        Parameters
        ----------
        label : int or str
            The label to encode. If string, it should be a class name.

        Returns
        -------
        tf.Tensor
            A TensorFlow constant of the label in binary format.
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
        Encodes a multi-class label into one-hot encoded format.

        Parameters
        ----------
        label : int or str
            The label to encode. If string, it should be a class name.

        Returns
        -------
        tf.Tensor
            A one-hot encoded TensorFlow constant of the label.
        """
        label = self.get_index(label) if isinstance(label, str) else label
        try:
            label = tf.constant(label, dtype=tf.int8)
            label = tf.one_hot(label, self.num_classes)
            label = tf.cast(label, self._label_dtype)
            return label
        except tf.errors.OpError as e:
            msg = "Failed to encode the label to a tensor."
            raise ValueError(msg) from e

    def encode_label(self, label):
        """
        Encodes a label based on the label type and class names specified
        during initialization to a tensor format.

        Parameters
        ----------
        label : int or str
            The label to encode. Can be an integer or a string if
            class names are specified.

        Returns
        -------
        tf.Tensor
            A TensorFlow constant of the encoded label.
        """
        return self._encode_label_func(label)

    def get_class(self, index):
        """
        Converts a numeric label to a class name.

        Parameters
        ----------
        index : str or int
            The class index.

        Returns
        -------
        str
            The class name corresponding to the numeric label.
        """
        if not self.class_names:
            msg = "No class names are provided for label decoding."
            raise ValueError(msg)
        try:
            index = index.numpy()
        except AttributeError:
            pass
        try:
            index = int(index)
            return self.class_names[index]
        except IndexError as e:
            msg = "The label is out of bounds for the class names."
            raise ValueError(msg) from e
        except ValueError as e:
            msg = "The label should be convertible to an integer."
            raise ValueError(msg) from e
