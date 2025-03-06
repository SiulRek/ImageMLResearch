"""
Unit tests for `randomly_select_sequential_keys`.

This module tests the accuracy and robustness of the function in identifying
and handling sequential key patterns in dictionaries. It verifies behavior
across various scenarios, including invalid patterns, sequential integrity,
and frequency-based key selection.

Attributes
----------
ENABLE_VISUAL_INSPECTION : bool
    Flag to enable or disable tests requiring visual inspection.
"""

import os
import unittest

from imlresearch.src.preprocessing.helpers.randomly_select_sequential_keys import (    # noqa: E501
    randomly_select_sequential_keys,
    is_sequential,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestRandomlySelectSequentialKeys(BaseTestCase):
    """
    Test suite for `randomly_select_sequential_keys`.

    This suite verifies that the function correctly identifies, processes,
    and selects sequential keys in dictionaries with different patterns
    and constraints.

    Notes
    -----
    - The default separator used in keys is '__'.
    - The dictionary key follows this pattern:
      `{key identifier}_{key}_i{index}__I{index}F{frequency}__extra`
    - Only the `{key}` part is required; other elements vary by test case.
    - `__I{index}F{frequency}` is the pattern detected by the function.
    - `i{index}` is used for verification since `__I{index}F{frequency}`
      is removed in the output.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the test directory for generated test data."""
        super().setUpClass()
        cls.test_data_directory = os.path.join(
            cls.output_dir, "randomly_select_sequential_keys_tests"
        )
        os.makedirs(cls.test_data_directory, exist_ok=True)

    def get_stripped_dict_keys(self, input_dict, separator="__"):
        """
        Remove the separator and its suffix from dictionary keys.

        Parameters
        ----------
        input_dict : dict
            The input dictionary with formatted keys.
        separator : str, optional
            The separator pattern in the keys (default is '__').

        Returns
        -------
        list
            List of cleaned keys from the input dictionary.
        """
        return [key.split(separator)[0] for key in input_dict.keys()]

    def test_some_keys_not_matching(self):
        """Test that a KeyError is raised when only some keys match."""
        input_dict = {"a_key__I0": "value1", "b_key": "value2"}
        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)

    def test_non_sequential_indices(self):
        """Test that a KeyError is raised when indices are not sequential."""
        input_dict = {"a_key_i1__I1": "value1", "b_key_i3__I3": "value2"}
        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)

    def test_all_keys_matching(self):
        """
        Test that all keys are selected when they match the pattern
        with different indices.
        """
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
        """Test normal execution with expected sequential keys."""
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
        Generate test data with sequential keys.

        Parameters
        ----------
        num_sequences : int
            Number of sequential key-value pairs to generate.

        Returns
        -------
        dict
            Dictionary containing generated sequential keys.
        """
        return {
            f"{i % 2}_key_i{i // 2}__I{i // 2}": f"value{i}"
            for i in range(num_sequences * 2)
        }

    def test_normal_operation_with_long_sequence(self):
        """Test normal execution with a long sequence of keys."""
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
        """
        Test the function's resilience to unique identifiers in keys.

        Ensures that keys containing additional unique identifiers are
        processed correctly without affecting sequential selection.
        """
        input_dict = {
            "key_i1__1__I1": "value1",
            "key_i1__2__I1": "alt1",
            "key_i0__3__I0": "value0",
            "key_i0__4__I0": "alt0",
        }
        output_dict = randomly_select_sequential_keys(input_dict)
        stripped_input_keys = [
            "key_i1__1", "key_i1__2", "key_i0__3", "key_i0__4"
        ]
        self.assertTrue(all(key in stripped_input_keys for key in output_dict))
        self.assertEqual(len(output_dict), 2)
        self.assertTrue(
            is_sequential([int(key.split("i")[1][0]) for key in output_dict])
        )

    def test_resilient_operation_2(self):
        """
        Test the function's resilience to the order of the keys.

        Ensures that the function correctly processes keys regardless of
        their ordering in the dictionary.
        """
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

    def test_key_already_selected(self):
        """
        Test that a KeyError is raised when keys are already selected.

        Ensures that the function correctly identifies keys that should
        not be selected multiple times.
        """
        input_dict = {"a_key__I0": "value0", "a_key__I1": "value1"}

        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)

    def test_keys_with_frequency_simple(self):
        """
        Test processing of keys with frequency specification.

        Ensures that the function correctly handles keys that include
        a frequency component in their naming pattern.
        """
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

    def test_keys_with_frequency_with_probability(self):
        """
        Test selection probability of keys with frequency specification.

        Ensures that keys with frequency indicators are selected with the
        correct probability distribution.
        """
        input_dict = {
            "a_key__I0": "value0",
            "b_key__I0F10": "alt0",
            "c_key__I1": "value1",
            "d_key__I1F10": "alt1",
        }
        keys = ["a_key", "b_key", "c_key", "d_key"]
        output_dicts = []
        for _ in range(1000):
            output_dicts.append(randomly_select_sequential_keys(input_dict))

        key_counts = {}
        for key in keys:
            key_counts[key] = sum(
                [1 if key in output_dict else 0 for output_dict in output_dicts]
            )

        self.assertAlmostEqual(key_counts["a_key"], 91, delta=25)
        self.assertAlmostEqual(key_counts["c_key"], 91, delta=25)

    def test_pattern_ending_allowed(self):
        """
        Test handling of keys with allowed characters after the pattern.

        Ensures that keys containing additional allowed characters beyond
        the expected pattern are correctly identified.
        """
        separator = "__"
        input_dict = {
            f"a_key{separator}extra{separator}I0": "value0",
            f"b_key{separator}I1": "value1",
            f"c_key{separator}I2{separator}extra": "value2",
            f"d_key{separator}I3F10": "value3",
            f"e_key{separator}I4F10{separator}extra": "value4",
        }

        expected_dict = {
            f"a_key{separator}extra": "value0",
            "b_key": "value1",
            f"c_key{separator}extra": "value2",
            "d_key": "value3",
            f"e_key{separator}extra": "value4",
        }

        output_dict = randomly_select_sequential_keys(input_dict)
        self.assertEqual(output_dict, expected_dict)

    def test_pattern_ending_not_allowed(self):
        """
        Test that extra disallowed characters after the pattern raise an error.

        Ensures that keys with unexpected characters following the pattern
        are correctly rejected.
        """
        separator = "__"
        input_dict = {
            f"a_key{separator}I0": "value0",
            f"b_key{separator}I1": "value1",
            f"c_key{separator}I2_extra": "value2",
            f"d_key{separator}I3F10": "value3",
            f"e_key{separator}I4F10_extra": "value4",
        }

        with self.assertRaises(KeyError):
            randomly_select_sequential_keys(input_dict)



if __name__ == "__main__":
    unittest.main()
