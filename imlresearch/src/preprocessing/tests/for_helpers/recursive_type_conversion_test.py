import json
import os
import unittest

from imlresearch.src.preprocessing.helpers.json_instances_serializer import (
    JSONInstancesSerializer,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class MockClass1:
    arguments_datatype = {
        "param1": str,
        "param2": int,
        "param3": {"key1": int, "key2": (float, bool)},
    }

    def __init__(self, param1, param3, param2=20):
        self.parameters = {
            "param1": param1,
            "param2": param2,
            "param3": param3,
        }

    def __eq__(self, obj):
        return self.parameters == obj.parameters


class MockClass2:
    arguments_datatype = {"param1": str, "param2": int}

    def __init__(self, param1, param2=20):
        self.parameters = {"param1": param1, "param2": param2}
        self.name = "MockClass2"

    def __eq__(self, obj):
        return self.parameters == obj.parameters


class MockClassWithoutArgsSpec:
    def __init__(self, param1=3):
        self.parameters = {"param1": param1}

    def __eq__(self, obj):
        return self.parameters == obj.parameters


class MockClassWithoutparametersAttr:
    pass


class MockClassInvalidparametersAttr:
    def __init__(self, param1=3):
        self.parameters = param1


class TestJSONInstancesSerializer(BaseTestCase):
    """
    Test suite for the JSONInstancesSerializer class.

    This suite contains a set of unit tests that are designed to ensure the
    proper functionality of the ClassInstancesSerializer's methods. It tests
    the ability to serialize and deserialize instance configurations, handle
    different types of inputs, and manage errors and edge cases appropriately.
    """

    def setUp(self):
        super().setUp()
        self.json_path = os.path.join(self.temp_dir, "test_config.json")
        with open(self.json_path, "w", encoding="utf-8"):
            pass
        self.instance_mapping = {
            "MockClass1": MockClass1,
            "MockClass2": MockClass2,
        }
        self.serializer = JSONInstancesSerializer(self.instance_mapping)
        self.instance_list = [
            MockClass1(
                param1="hallo",
                param2=20,
                param3={"key1": 30, "key2": (3.2, True)},
            ),
            MockClass1(
                param1="tschuess",
                param3={"key1": 40, "key2": (55.3, False)},
            ),
            MockClass2(param1="win"),
        ]

    def test_serialize_success_1(self):
        """Test the serialization to JSON value of various data types."""
        self.assertEqual(
            self.serializer._serialize_to_json_value([1, 2, 3]), [1, 2, 3]
        )
        self.assertEqual(
            self.serializer._serialize_to_json_value((1, 2, 3)), [1, 2, 3]
        )
        self.assertEqual(
            self.serializer._serialize_to_json_value({"a": 1, "b": 2}),
            {"a": 1, "b": 2},
        )
        self.assertEqual(self.serializer._serialize_to_json_value(1), 1)
        self.assertEqual(self.serializer._serialize_to_json_value(1.0), 1.0)
        self.assertEqual(
            self.serializer._serialize_to_json_value("test"), "test"
        )
        self.assertEqual(self.serializer._serialize_to_json_value(True), True)

    def test_serialize_success_2(self):
        """Test the serialization of a nested structure."""
        nested_structure = {
            "list": [1, 2, 3],
            "tuple": (1, 2, 3),
            "dict": {"nested_list": (4, 5, "30")},
        }
        expected = {
            "list": [1, 2, 3],
            "tuple": [1, 2, 3],
            "dict": {"nested_list": [4, 5, "30"]},
        }
        self.assertEqual(
            self.serializer._serialize_to_json_value(nested_structure),
            expected,
        )

    def test_serialize_failed(self):
        """Test serialization failure with unsupported data types."""
        with self.assertRaises(TypeError):
            self.serializer._serialize_to_json_value(set([1, 2, 3]))

        class CustomObject:
            pass

        with self.assertRaises(TypeError):
            self.serializer._serialize_to_json_value(CustomObject())

    def test_deserialize_json_parameters(self):
        """Test the deserialization of JSON parameters."""
        source = {
            "number_str": "123",
            "list_of_int": [1, 2, 3],
            "nested_dict": {"bool_str": True},
            "tuple_of_mixed": ("30", "", ["30", 10]),
        }
        expected = {
            "number_str": "123",
            "list_of_int": [1, 2, 3],
            "nested_dict": {"bool_str": True},
            "tuple_of_mixed": ("30", "", ["30", 10]),
        }

        output = self.serializer._deserialize_json_parameters(
            source, randomized=False
        )
        self.assertEqual(output, expected)

    def test_creation_of_json(self):
        """Test the creation of a JSON file."""
        json_file = os.path.join(self.output_dir, "serializer_test_file.json")
        self.serializer.save_instances_to_json([], json_file)
        os.remove(json_file)

    def test_load_from_json(self):
        """Test loading instances from a JSON file."""
        mock_class_parameters_1 = {"param1": "hallo", "param2": 20}
        mock_class_parameters_2 = {"param1": "servus", "param2": 3}
        temp_key = (
            "MockClass2" + JSONInstancesSerializer.KEY_SEPARATOR + "2"
        )
        json_data = {
            "MockClass2": mock_class_parameters_1,
            temp_key: mock_class_parameters_2,
        }

        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file)
        loaded_instance_list = self.serializer.get_instances_from_json(
            self.json_path
        )

        self.assertEqual(
            loaded_instance_list[0].parameters["param1"],
            mock_class_parameters_1["param1"],
        )
        self.assertEqual(
            loaded_instance_list[0].parameters["param2"],
            mock_class_parameters_1["param2"],
        )
        self.assertEqual(
            loaded_instance_list[1].parameters["param1"],
            mock_class_parameters_2["param1"],
        )
        self.assertTrue(
            isinstance(loaded_instance_list[0].parameters["param2"], int)
        )
        self.assertTrue(
            isinstance(loaded_instance_list[1].parameters["param2"], int)
        )

    def test_invalid_json_path(self):
        """Test handling of invalid JSON paths."""
        invalid_paths = [
            ("directory/does/not/exist/test_config.json", ValueError),
            ("imlresearch/src/utils/test_config.txt", ValueError),
        ]

        for path, expected_exception in invalid_paths:
            with self.subTest(path=path):
                with self.assertRaises(expected_exception):
                    self.serializer._verify_json_path(path)
                with self.assertRaises(expected_exception):
                    self.serializer.get_instances_from_json(path)
                with self.assertRaises(expected_exception):
                    self.serializer.get_randomized_instances_from_json(path)
                with self.assertRaises(expected_exception):
                    self.serializer.save_instances_to_json([], path)

    def test_missing_mapping_in_save(self):
        """Test saving instances with missing mapping."""
        with self.assertRaises(KeyError):
            self.serializer.instance_mapping = {"MockClass1": MockClass1}
            self.serializer.save_instances_to_json(
                self.instance_list, self.json_path
            )

    def test_missing_mapping_in_load(self):
        """Test loading instances with missing mapping."""
        mock_class_parameters = {
            "param1": ["tschuess", "hallo"],
            "param2": [20, 30, 40],
        }
        json_data = {"MockClass2": mock_class_parameters}

        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file)

        self.serializer.instance_mapping = {"MockClass1": MockClass1}
        with self.assertRaises(KeyError):
            self.serializer.get_instances_from_json(self.json_path)
        with self.assertRaises(KeyError):
            self.serializer.get_randomized_instances_from_json(self.json_path)


if __name__ == "__main__":
    unittest.main()
