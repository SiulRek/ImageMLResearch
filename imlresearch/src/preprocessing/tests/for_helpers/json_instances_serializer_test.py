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
        json_fil
