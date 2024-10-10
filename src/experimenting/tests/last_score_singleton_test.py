import unittest

from src.experimenting.helpers.last_score_singleton import LastScoreSingleton
from src.testing.bases.base_test_case import BaseTestCase


class TestLastScoreSingleton(BaseTestCase):

    def tearDown(self):
        super().tearDown()
        if LastScoreSingleton._instance:
            LastScoreSingleton._instance = None

    def test_set_score_none(self):
        """ Test if set() method works correctly with None values. """
        score_instance = LastScoreSingleton()
        score_instance.set(None)

    def test_set_score_numeric(self):
        """ Test if set() method works correctly with numeric values. """
        numeric_values = [-2, 0.85, 0, -0.85, 2]
        score_instance = LastScoreSingleton()
        for value in numeric_values:
            score_instance.set(value)

    def test_set_score_non_numeric(self):
        """ Test if set() method raises an AssertionError when non-numeric values
        are provided. """
        non_numeric_values = ["string", True, False, [], {}]
        score_instance = LastScoreSingleton()
        for value in non_numeric_values:
            with self.assertRaises(AssertionError, msg=f"Value: {value}"):
                score_instance.set(value)

    def test_singleton_behavior(self):
        """ Test if the LastScoreSingleton class exhibits singleton behavior. """
        instance1 = LastScoreSingleton()
        instance2 = LastScoreSingleton()
        self.assertIs(instance1, instance2, "LastScoreSingleton is not a singleton!")

    def test_set_and_take_score_same_instances(self):
        """ Test if set() and take() methods work correctly. """
        score_instance = LastScoreSingleton()

        score_instance.set(0.85)
        self.assertEqual(
            score_instance.take(), 0.85, "Score did not match after setting!"
        )

        score_instance.set(0.90)
        self.assertEqual(score_instance.take(), 0.90, "Score did not update correctly!")

    def test_set_and_take_score_different_instances(self):
        """ Test if set() and take() methods work correctly with different
        instances. """
        score_instance_1 = LastScoreSingleton()
        score_instance_2 = LastScoreSingleton()
        score_instance_1.set(0.85)
        self.assertEqual(
            score_instance_1.take(), 0.85, "Score did not match after setting!"
        )

        score_instance_2.set(0.90)
        self.assertEqual(
            score_instance_2.take(), 0.90, "Score did not update correctly!"
        )

    def test_take_without_previous_set(self):
        """ Test if take() method raises a ValueError when no score has been set. """
        score_instance = LastScoreSingleton()
        with self.assertRaises(ValueError):
            score_instance.take()

    def test_clear(self):
        """ Test if clear() method works correctly. """
        score_instance = LastScoreSingleton()
        score_instance.set(0.85)
        score_instance.clear()
        with self.assertRaises(ValueError):
            score_instance.take()


if __name__ == "__main__":
    unittest.main()
