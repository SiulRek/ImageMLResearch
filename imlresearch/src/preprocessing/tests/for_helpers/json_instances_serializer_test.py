import os
import unittest

from imlresearch.src.preprocessing.helpers.randomly_select_sequential_keys import (    # noqa: E501
    randomly_select_sequential_keys,
    is_sequential,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestRandomlySelectSequentialKeys(BaseTestCase):
    """
    Unit tests for `randomly_select_sequential_keys`.

    This suite tests the accuracy of the function in identifying and handling
    sequential key patterns in dictionaries. It covers various cases,
    including invalid patterns, sequential integrity, and frequency-based key
    selection. Each test ensures the function's robustness and error handling.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_data_directory = os.path.join(
            cls.output_dir, "randomly_select_sequential_keys_tests"
        )
        os.makedirs(cls.test_data_directory, exist_ok=True)

    def get_stripped_dict_keys(self, input_dict, separator="__"):
        """
        Get the keys of a dictionary with the separator and part after the
        separator removed.

        Args:
            - input_dict (dict): The input dictionary.
            - separator (str, optional): The separator used in the key
              pattern. Defaults to '__'.

        Returns:
            - list: A list of keys in the input dictionary.
        """
        return [key.split(separator)[0] for key in input_dict.keys()]

    def test_some_keys_not_matching(self):
        """Test that an error is raised when only some keys do not match."""
        input_dict = {"a_key__I0": "value1", "b_key": "value2"}
        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)

    def test_non_sequential_indices(self):
        """Test that an error is raised when indices are not sequential."""
        input_dict = {"a_key_i1__I1": "value1", "b_key_i3__I3": "value2"}
        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)

    def test_all_keys_matching(self):
        """Test that all keys are selected when matching the pattern."""
        input_dict = {
            "a_key_i0__I0": "value0",
            "b_key_i1__I1": "value1",
            "c_key_i2__I2": "value2",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = self.get_stripped_dict_keys(input_dict)
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 3)
        self.assertTrue(
            is_sequential([int(key.split("i")[1]) for key in output_dict])
        )

    def test_normal_operation(self):
        """Test the normal operation of the function."""
        input_dict = {
            "a_key_i0__I0": "value0",
            "b_key_i0__I0": "alt0",
            "a_key_i1__I1": "value1",
            "b_key_i1__I1": "alt1",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = self.get_stripped_dict_keys(input_dict)
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 2)
        self.assertTrue(
            is_sequential([int(key.split("i")[1]) for key in output_dict])
        )

    def _generate_test_data(self, num_sequences):
        """
        Generate test data with sequential keys for testing.

        Args:
            - num_sequences (int): Number of sequential pairs to generate.

        Returns:
            - dict: A dictionary with generated test data.
        """
        return {
            f"{i % 2}_key_i{i // 2}__I{i // 2}": f"value{i}"
            for i in range(num_sequences * 2)
        }

    def test_normal_operation_with_long_sequence(self):
        """Test normal operation with a longer sequence."""
        num_sequences = 111
        input_dict = self._generate_test_data(num_sequences)
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = self.get_stripped_dict_keys(input_dict)
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), num_sequences)
        self.assertTrue(
            is_sequential([int(key.split("i")[1]) for key in output_dict])
        )

    def test_resilient_operation_1(self):
        """Test resilience to unique identifiers specified in keys."""
        input_dict = {
            "key_i1__1__I1": "value1",
            "key_i1__2__I1": "alt1",
            "key_i0__3__I0": "value0",
            "key_i0__4__I0": "alt0",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = [
            "key_i1__1",
            "key_i1__2",
            "key_i0__3",
            "key_i0__4",
        ]
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 2)
        self.assertTrue(
            is_sequential([int(key.split("i")[1][0]) for key in output_dict])
        )

    def test_resilient_operation_2(self):
        """Test resilience to order of keys."""
        input_dict = {
            "a_key_i1__I1": "value1",
            "b_key_i0__I0": "value0",
            "c_key_i1__I1": "alt1",
            "d_key_i0__I0": "alt0",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = self.get_stripped_dict_keys(input_dict)
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 2)
        self.assertTrue(
            is_sequential([int(key.split("i")[1]) for key in output_dict])
        )

    def test_keys_with_frequency_simple(self):
        """Test processing of keys with frequency specification."""
        input_dict = {
            "a_key__I0": "value0",
            "b_key__I0F10": "alt0",
            "c_key__I1": "value1",
            "d_key__I1F10": "alt1",
            "e_key__I2F10": "alt2",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = self.get_stripped_dict_keys(input_dict)
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 3)


if __name__ == "__main__":
    unittest.main()
