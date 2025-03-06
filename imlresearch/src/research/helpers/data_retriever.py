import numpy as np
import tensorflow as tf

from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.utils import unbatch_dataset_if_batched


class DataRetriever(ResearchAttributes):
    """
    Retrieve input and output data from `datasets_containers` and
    `outputs_containers` in ResearchAttributes.
    """

    def __init__(self):
        """
        Initialize the DataRetriever.

        Notes
        -----
        ResearchAttributes is not initialized here. Instead,
        `synchronize_research_attributes` should be explicitly called.

        This initializes research attributes used in DataRetriever.
        """
        self._datasets_container = {}
        self._outputs_container = {}

    def _to_numpy_array(self, array):
        """
        Convert an array to a NumPy array.

        The conversion follows these steps:
        1. If the array has a `numpy` method, it is called.
        2. If no `numpy` method exists, `np.array` is used for conversion.

        Parameters
        ----------
        array : array-like
            The array to convert.

        Returns
        -------
        np.ndarray
            The converted NumPy array.
        """
        if isinstance(array, np.ndarray):
            return array
        try:
            return array.numpy()
        except AttributeError:
            return np.array(array)

    def _retrieve_class_names(self):
        """
        Retrieve class names from the label manager.

        Returns
        -------
        list
            The class names.
        """
        try:
            return self.label_manager.class_names
        except AttributeError:
            raise AttributeError("No class names found in the label manager.")

    def _retrieve_test_output_data(self):
        """
        Retrieve the output of the test dataset.

        This function returns the true and predicted labels.

        Returns
        -------
        tuple
            (y_true, y_pred)
        """
        complete_output = self._outputs_container.get("complete_output")
        test_output = self._outputs_container.get("test_output")
        output = complete_output or test_output
        if output is None:
            raise ValueError(
                "Neither 'complete_output' nor 'test_output' found in outputs."
            )
        return output[0], output[1]

    def _retrieve_output_data_by_name(self, output_name):
        """
        Retrieve output data by its name.

        Parameters
        ----------
        output_name : str
            The name of the output data to retrieve from the container.

        Returns
        -------
        object
            The output data associated with the given name.
        """
        if output_name not in self._outputs_container:
            raise ValueError(
                f"No output data found with name '{output_name}' to plot."
            )
        return self._outputs_container[output_name]

    def _retrieve_input_data_by_name(self, dataset_name):
        """
        Retrieve input data from the dataset.

        Parameters
        ----------
        dataset_name : str
            The name of the dataset in the datasets container.

        Returns
        -------
        tf.Tensor
            The retrieved input data.
        """
        if dataset_name not in self._datasets_container:
            raise ValueError(f"No dataset found with name '{dataset_name}'.")

        dataset = self._datasets_container.get(dataset_name)
        dataset = unbatch_dataset_if_batched(dataset)

        inputs_list = []
        for inputs, _ in dataset:
            inputs_list.append(tf.expand_dims(inputs, axis=0))
        return tf.concat(inputs_list, axis=0)

    def _retrieve_test_input_output_data(self):
        """
        Retrieve input and output data from the test dataset.

        Returns
        -------
        tuple
            (x, y_true, y_pred)
        """
        for dataset_name in ["complete_dataset", "test_dataset"]:
            if (
                dataset_name in self._datasets_container
                and self._datasets_container[dataset_name]
            ):
                try:
                    x = self._retrieve_input_data_by_name(dataset_name)
                    output_name = dataset_name.replace("dataset", "output")
                    y_true, y_pred = self._retrieve_output_data_by_name(
                        output_name
                    )
                    return x, y_true, y_pred
                except ValueError:
                    pass

        raise ValueError(
            "No dataset synced with outputs found to plot.\n"
            "Possible reasons:\n"
            "1. Neither 'complete_dataset' nor 'test_dataset' found in "
            "datasets container.\n"
            "2. No output data synced with the dataset found in outputs "
            "container."
        )
