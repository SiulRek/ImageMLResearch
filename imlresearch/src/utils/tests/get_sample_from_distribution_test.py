import unittest

from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.utils import get_sample_from_distribution


class TestGetSampleFromDistribution(BaseTestCase):
    """
    Test suite for the get_sample_from_distribution function.
    """

    def test_gaussian_distribution(self):
        """
        Test sampling from a Gaussian distribution.
        """
        data = {"distribution": "gaussian", "loc": 0, "scale": 1}
        sample = get_sample_from_distribution(data)
        self.assertIsInstance(sample, float)

    def test_gaussian(self):
        """
        Test sampling from a Gaussian distribution.
        """
        data = {"distribution": "gaussian", "loc": 0, "scale": 1}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_uniform(self):
        """
        Test sampling from a uniform distribution.
        """
        data = {"distribution": "uniform", "low": 1, "high": 2}
        sample = get_sample_from_distribution(data)
        self.assertIsInstance(sample, float)
        self.assertTrue(1 <= sample <= 2)

    def test_exponential(self):
        """
        Test sampling from an exponential distribution.
        """
        data = {"distribution": "exponential", "scale": 1}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_poisson(self):
        """
        Test sampling from a Poisson distribution.
        """
        data = {"distribution": "poisson", "lam": 3}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_binomial(self):
        """
        Test sampling from a binomial distribution.
        """
        data = {"distribution": "binomial", "n": 10, "p": 0.5}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_gamma(self):
        """
        Test sampling from a gamma distribution.
        """
        data = {"distribution": "gamma", "shape": 2, "scale": 1}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_beta(self):
        """
        Test sampling from a beta distribution.
        """
        data = {"distribution": "beta", "a": 0.5, "b": 0.5}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_lognormal(self):
        """
        Test sampling from a log-normal distribution.
        """
        data = {"distribution": "lognormal", "mean": 0, "sigma": 1}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_laplace(self):
        """
        Test sampling from a Laplace distribution.
        """
        data = {"distribution": "laplace", "loc": 0, "scale": 1}
        self.assertIsInstance(get_sample_from_distribution(data), float)

    def test_invalid_distribution(self):
        """
        Test handling of an invalid distribution name.
        """
        data = {"distribution": "unknown", "param": 1}
        with self.assertRaises(ValueError):
            get_sample_from_distribution(data)

    def test_invalid_distribution_arguments(self):
        """
        Test handling of invalid arguments for a known distribution.
        """
        data = {"distribution": "gaussian", "invalid_argument": 1}
        with self.assertRaises(ValueError):
            get_sample_from_distribution(data)

    def test_missing_distribution_key(self):
        """
        Test handling of missing 'distribution' key in input data.
        """
        data = {"mean": 0, "std_dev": 1}
        with self.assertRaises(KeyError):
            get_sample_from_distribution(data)


if __name__ == "__main__":
    unittest.main()
