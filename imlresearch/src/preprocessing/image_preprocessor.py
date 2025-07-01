from copy import deepcopy

import tensorflow as tf

from imlresearch.src.data_handling.manipulation.pack_images_and_labels import pack_images_and_labels    # noqa: E501
from imlresearch.src.data_handling.manipulation.unpack_dataset import unpack_dataset    # noqa: E501
from imlresearch.src.preprocessing.definitions.step_class_mapping import STEP_CLASS_MAPPING   # noqa: E501
from imlresearch.src.preprocessing.helpers.get_pipeline_code_representation import get_pipeline_code_representation   # noqa: E501
from imlresearch.src.preprocessing.helpers.json_instances_serializer import JSONInstancesSerializer  # noqa: E501
from imlresearch.src.preprocessing.steps.step_base import StepBase


class ImagePreprocessor:
    """
    Manages and processes a pipeline of image preprocessing steps.

    The ImagePreprocessor class encapsulates a sequence of preprocessing
    operations defined as steps. Each step is a discrete preprocessing action,
    such as noise reduction, normalization, etc., applied in sequence to an
    input dataset of images.

    Attributes
    ----------
    pipeline : list of StepBase
        List of preprocessing steps to be executed.
    serializer : JSONInstancesSerializer
        Handles serialization/deserialization of the pipeline.
    occurred_exception_message : str
        Stores exception messages encountered during processing.

    Methods
    -------
    set_default_datatype(datatype)
        Sets the default datatype for pipeline steps.
    set_pipe(pipeline)
        Sets the preprocessing pipeline with a deep copy of provided steps.
    pipe_append(step)
        Appends a new step to the pipeline, verifying it is a subclass of
        StepBase.
    pipe_pop()
        Removes and returns the last step from the pipeline.
    pipe_clear()
        Clears all steps from the pipeline.
    process(image_dataset)
        Applies each preprocessing step to the provided dataset.
    save_pipe_to_json(json_path)
        Serializes the preprocessing pipeline to a JSON file.
    load_pipe_from_json(json_path)
        Loads and reconstructs a preprocessing pipeline from a JSON file.
    load_randomized_pipe_from_json(json_path)
        Loads a pipeline from JSON with randomized parameters.
    get_pipe_code_representation()
        Generates a text representation of the pipeline.
    """

    def __init__(self, raise_step_process_exception=True):
        """
        Initializes the ImagePreprocessor with an empty pipeline.

        Parameters
        ----------
        raise_step_process_exception : bool, optional
            Determines whether exceptions during step processing are raised or
            logged.
        """
        self._pipeline = []
        self._serializer = None
        self._initialize_class_instance_serializer(STEP_CLASS_MAPPING)
        self._raise_step_process_exception = raise_step_process_exception
        self._occurred_exception_message = ""
        self.set_default_datatype(tf.uint8)

    def __eq__(self, other):
        """
        Checks equality between two ImagePreprocessor instances.

        Parameters
        ----------
        other : ImagePreprocessor
            The other ImagePreprocessor instance to compare.

        Returns
        -------
        bool
            True if the pipelines are identical, False otherwise.
        """
        if not isinstance(other, ImagePreprocessor):
            return False
        return self.pipeline == other.pipeline

    @property
    def pipeline(self):
        return self._pipeline

    @property
    def serializer(self):
        return self._serializer

    @property
    def occurred_exception_message(self):
        return self._occurred_exception_message

    def _initialize_class_instance_serializer(self, step_class_mapping):
        """
        Initializes the serializer for pipeline serialization and
        deserialization.

        Parameters
        ----------
        step_class_mapping : dict
            Dictionary mapping step names to StepBase subclasses.
        """
        if not isinstance(step_class_mapping, dict):
            raise TypeError(
                "'step_class_mapping' must be of type dict, not "
                f"{type(step_class_mapping)}."
            )

        for mapped_class in step_class_mapping.values():
            if not issubclass(mapped_class, StepBase):
                raise ValueError(
                    "At least one mapped class is not a subclass of StepBase."
                )

        self._serializer = JSONInstancesSerializer(step_class_mapping)

    def set_default_datatype(self, datatype):
        """
        Sets the default datatype for the pipeline steps.

        Parameters
        ----------
        datatype : tf.dtpyes.DType
            The default output datatype for the pipeline steps.
        """
        if not isinstance(datatype, tf.dtypes.DType):
            raise TypeError(
                f"Expecting a tf.dtypes.DType, got {type(datatype)} instead."
            )
        StepBase.default_output_datatype = datatype

    def set_pipe(self, pipeline):
        """
        Sets the preprocessing pipeline with a deep copy of the provided steps.

        Parameters
        ----------
        pipeline : list of StepBase
            List of preprocessing steps to be set in the pipeline.
        """
        for step in pipeline:
            if not isinstance(step, StepBase):
                raise ValueError(
                    f"Expecting a subclass of StepBase, got {type(step)} "
                    "instead."
                )
        self._pipeline = deepcopy(pipeline)

    def pipe_pop(self):
        """
        Removes and returns the last step from the pipeline.

        Returns
        -------
        StepBase
            The last step that was removed from the pipeline.
        """
        return self._pipeline.pop()

    def pipe_append(self, step):
        """
        Appends a new step to the pipeline.

        Parameters
        ----------
        step : StepBase
            The preprocessing step to be appended.
        """
        if not isinstance(step, StepBase):
            raise ValueError(
                f"Expecting a subclass of StepBase, got {type(step)} instead."
            )
        self._pipeline.append(deepcopy(step))

    def pipe_clear(self):
        """
        Clears all steps from the pipeline.
        """
        self._pipeline.clear()

    def save_pipe_to_json(self, json_path):
        """
        Serializes the preprocessing pipeline to the specified JSON file.

        Parameters
        ----------
        json_path : str
            File path where the pipeline configuration will be saved.
        """
        self.serializer.save_instances_to_json(self.pipeline, json_path)

    def load_pipe_from_json(self, json_path):
        """
        Loads and reconstructs a preprocessing pipeline from a JSON file.

        Parameters
        ----------
        json_path : str
            File path from which the pipeline configuration will be loaded.
        """
        self._pipeline = self.serializer.get_instances_from_json(json_path)

    def load_randomized_pipe_from_json(self, json_path):
        """
        Loads and reconstructs a preprocessing pipeline from a JSON file with
        randomized parameters.

        Parameters
        ----------
        json_path : str
            File path from which the pipeline configuration will be loaded.
        """
        self._pipeline = self.serializer.get_randomized_instances_from_json(
            json_path
        )

    def get_pipe_code_representation(self):
        """
        Generates a text representation of the pipeline's configuration.

        Returns
        -------
        str
            A string representation of the pipeline in a code-like format.
        """
        return get_pipeline_code_representation(self.pipeline)

    def _consume_tf_dataset(self, tf_dataset):
        """
        Forces execution of the TensorFlow dataset computation graph.

        Parameters
        ----------
        tf_dataset : tf.data.Dataset
            The dataset to be consumed.
        """
        for _ in tf_dataset.take(1):
            pass

    def _unpack_dataset(self, dataset):
        """
        Unpacks a dataset into images and labels if applicable.

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset to unpack.

        Returns
        -------
        tuple
            A tuple containing the unpacked dataset and labels.
        """
        for element in dataset.take(1):
            if isinstance(element, tuple) and len(element) == 2:
                return unpack_dataset(dataset)
            return dataset, None

    def process(self, image_dataset):
        """
        Applies each preprocessing step to the provided dataset.

        If `_raise_step_process_exception` is True, exceptions in processing a
        step will be caught and logged, and the process will return None.
        Otherwise, it will proceed without exception handling.

        Parameters
        ----------
        image_dataset : tf.data.Dataset
            The TensorFlow dataset to be processed.

        Returns
        -------
        tf.data.Dataset
            The processed dataset after applying all the steps in the pipeline.
        """
        image_dataset, label_dataset = self._unpack_dataset(image_dataset)
        processed_dataset = image_dataset
        for step in self.pipeline:
            if self._raise_step_process_exception:
                processed_dataset = step(processed_dataset)
            else:
                try:
                    processed_dataset = step(processed_dataset)
                    self._consume_tf_dataset(processed_dataset)
                except Exception as e:
                    msg = f"An error occurred in step {step.name}: {str(e)}"
                    print(msg)
                    self._occurred_exception_message = msg
                    return None
    
        if not self._raise_step_process_exception:
            self._consume_tf_dataset(processed_dataset)

        if label_dataset is not None:
            processed_dataset = pack_images_and_labels(
                processed_dataset, label_dataset
            )

        return processed_dataset