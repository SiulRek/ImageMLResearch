import json
import os
import random
import re
import warnings

from imlresearch.src.preprocessing.helpers.parse_and_repeat import (
    parse_and_repeat,
)
from imlresearch.src.preprocessing.helpers.randomly_select_sequential_keys import (
    randomly_select_sequential_keys,
)
from imlresearch.src.preprocessing.helpers.recursive_type_conversion import (
    recursive_type_conversion,
)
from imlresearch.src.utils import get_sample_from_distribution


class JSONInstancesSerializer:
    """
    Manages serialization and deserialization of class instances to and from
    JSON format. Supports saving class instances with parameters to JSON and
    reconstructing them with optional parameter randomization. Useful for
    hyperparameter tuning and experimentation.

    Attributes:
        - KEY_SEPARATOR (str): Separator for constructing unique keys in
          JSON files.
        - instance_mapping (dict): Maps class names to actual class objects.
    """

    KEY_SEPARATOR = "__"

    def __init__(self, instance_mapping):
        """
        Initializes a new instance of the JSONInstancesSerializer class.

        This handler manages serialization and deserialization of class
        instance configurations to and from JSON files. It ensures that class
        instances are appropriately instantiated with their corresponding
        parameters stored in a JSON format.

        Args:
            - instance_mapping (dict): A dictionary mapping class names as
              strings to the actual class objects. This enables the handler to
              instantiate objects of the mapped classes from stored
              configurations.
        """
        self.instance_mapping = instance_mapping

    @property
    def instance_mapping(self):
        return self._instance_mapping

    @instance_mapping.setter
    def instance_mapping(self, value):
        if not isinstance(value, dict):
            raise ValueError(
                f"The specified instance mapping is not of type dict: {value}."
            )
        self._instance_mapping = value

    def _verify_json_path(self, json_path):
        """
        Verifies that the provided path is a JSON file and the base directory
        of the file exists.

        Args:
            - json_path (str): The file path to verify.
        """
        if not os.path.exists(os.path.dirname(json_path)):
            raise ValueError(
                f"The Base Directory of JSON path {json_path} does not exist."
            )
        if not json_path.endswith(".json"):
            raise ValueError(f"Specified JSON path '{json_path}' is not JSON.")

    def _serialize_to_json_value(self, obj):
        """
        Recursively converts Python objects to JSON serializable types.

        Args:
            - obj (object): The Python object to serialize.

        Returns:
            - object: The JSON-serializable representation of `obj`.
        """
        if isinstance(obj, (tuple, list)):
            return [self._serialize_to_json_value(item) for item in obj]
        if isinstance(obj, dict):
            return {
                key: self._serialize_to_json_value(value)
                for key, value in obj.items()
            }
        if isinstance(obj, (int, float, str, bool)):
            return obj
        raise TypeError(
            f"Object with value '{obj}' cannot be serialized to JSON format."
        )

    def _generate_unique_key_name(self, current_key, dictionary):
        """
        Generates a unique key name by appending incrementing numbers if a
        conflict exists.

        Args:
            - current_key (str): The base name for the key.
            - dictionary (dict): The dictionary which should not have
              conflicting keys.

        Returns:
            - str: A unique key name for the dictionary.
        """
        key = current_key
        i = 2  # Starts from 2 as 1 is the case of key name without identification.
        while key in dictionary.keys():
            sep = JSONInstancesSerializer.KEY_SEPARATOR
            key = key.split(sep)[0] + sep + str(i)
            i += 1
        return key

    def _remove_newlines(self, match):
        """
        Removes newlines and spaces within square brackets in JSON strings.

        Args:
            - match (re.Match): The regex match object containing the matched
              string.

        Returns:
            - str: The matched string with newlines and spaces removed.
        """
        return match.group().replace("\n", "").replace(" ", "")

    def _save_configurations_to_json(self, configurations, json_path):
        """
        Saves configurations of the class instances to a JSON file after
        serializing and formatting.

        Args:
            - configurations (dict): Dictionary containing the class
              instance configuration.
            - json_path (str): The file path where the JSON will be saved.
        """
        self._verify_json_path(json_path)
        json_data = {}
        for class_name in configurations.keys():
            converted_parameters = {
                key: self._serialize_to_json_value(value)
                for key, value in configurations[class_name].items()
            }
            unique_name = self._generate_unique_key_name(class_name, json_data)
            json_data[unique_name] = converted_parameters

        json_string = json.dumps(json_data, indent=4).replace("},", "},\n")
        pattern = r"\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]"
        result = re.sub(pattern, self._remove_newlines, json_string)
        with open(json_path, "w", encoding="utf-8") as file:
            file.write(result)

    def save_instances_to_json(self, instance_list, json_path):
        """
        Serializes a list of class instances to a JSON file.

        Args:
            - instance_list (list): A list of class instances to serialize.
            - json_path (str): The file path where the JSON will be saved.
        """
        configurations = {}
        for instance in instance_list:
            configurations = self._add_instance_to_configurations(
                instance, configurations
            )
        self._save_configurations_to_json(configurations, json_path)

    def get_instances_from_json(self, json_path):
        """
        Deserializes class instances from a JSON file with specific parameters.

        Args:
            - json_path (str): The file path of the JSON to deserialize.

        Returns:
            - list: A list of class instances created from the JSON file
              with specific parameters.
        """
        return self._build_instances_from_json(json_path, randomized=False)

    def get_randomized_instances_from_json(self, json_path):
        """
        Deserializes class instances from a JSON file with randomly selected
        parameters.

        Args:
            - json_path (str): The file path of the JSON to deserialize.

        Returns:
            - list: A list of class instances created from the JSON file
              with random parameters.
        """
        return self._build_instances_from_json(json_path, randomized=True)
