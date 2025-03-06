import unittest

import matplotlib.pyplot as plt

from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class BaseTestCaseDemo(BaseTestCase):
    """
    Demonstration class showcasing the functionality of BaseTestCase.

    This class utilizes the setup and teardown mechanisms of BaseTestCase
    to demonstrate their effectiveness and practical usage in testing.
    """

    @classmethod
    def _compute_output_dir(cls):
        """
        Override method to specify a custom output directory.

        Returns
        -------
        str
            The computed output directory.
        """
        return super()._compute_output_dir("testing")

    @classmethod
    def setUpClass(cls):
        """
        Set up the class-level test environment.

        This method initializes output directories and logging mechanisms.
        """
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
        """
        Clean up class-level resources after tests.

        This method ensures proper cleanup of temporary directories.
        """
        super().tearDownClass()
        print(
            f"TearDownClass: Temp directory at {cls.temp_dir} cleaned up."
        )

    def test_example_functionality(self):
        """
        Example test demonstrating logging and test assertion.

        This test case simply asserts `True` to showcase logging.
        """
        self.assertTrue(True)

    def test_load_image_dataset(self):
        """
        Example test demonstrating dataset loading functionality.

        This test case verifies that an image dataset can be loaded
        and saved as an output image.
        """
        dataset = self.load_geometrical_forms_dataset()
        for image in dataset.take(1):
            self.assertIsNotNone(image)
            plt.imshow(image)
            plt.savefig(f"{self.output_dir}/loaded_image.png")

    def tearDown(self):
        """
        Log the outcome after each test method.

        This method ensures that test results are properly logged.
        """
        super().tearDown()
        print("Logging the outcome of the test method.")


if __name__ == "__main__":
    unittest.main()
