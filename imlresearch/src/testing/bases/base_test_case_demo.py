import unittest

import matplotlib.pyplot as plt

from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class BaseTestCaseDemo(BaseTestCase):
    """
    A demonstration class to showcase the functionality of BaseTestCase.

    It leverages the setup and teardown mechanisms of BaseTestCase to 
    demonstrate their effectiveness and usage in a practical testing scenario.
    """

    @classmethod
    def _compute_output_dir(cls):
        """Override method to avoid needing a 'tests' directory."""
        return super()._compute_output_dir("testing")

    @classmethod
    def setUpClass(cls):
        """Set up class-level test environment."""
        super().setUpClass()
        print(
            f"SetupClass: Output directory set up at {cls.output_dir}"
        )
        print(
            f"SetupClass: Temporary directory set up at {cls.temp_dir}"
        )
        print(f"SetupClass: Log file set up at {cls.log_file}")

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources after tests."""
        super().tearDownClass()
        print(
            f"TearDownClass: Temp directory at {cls.temp_dir} cleaned up."
        )

    def test_example_functionality(self):
        """
        An example test that logs its outcome and demonstrates 
        the logging functionality.
        """
        self.assertTrue(True)

    def test_load_image_dataset(self):
        """
        An example test that demonstrates the usage of a helper method.
        """
        dataset = self.load_geometrical_forms_dataset()
        for image in dataset.take(1):
            # Plot the image to outputs directory
            self.assertIsNotNone(image)
            plt.imshow(image)
            plt.savefig(f"{self.output_dir}/loaded_image.png")

    def tearDown(self):
        """Log test outcome after each test method."""
        super().tearDown()
        print("Logging the outcome of the test method.")


if __name__ == "__main__":
    unittest.main()
