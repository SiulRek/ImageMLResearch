import numpy as np


def get_sample_from_distribution(distribution_data):
    """
    Generate a single random sample from a specified probability distribution.

    This function dynamically selects a distribution function based on the
    input dictionary `distribution_data`, which should contain the key
    'distribution' specifying the type of distribution and additional
    parameters required by the selected distribution.

    Parameters
    ----------
    distribution_data : dict
        A dictionary containing the distribution type and its corresponding
        parameters.

    Returns
    -------
    float
        A single sample from the specified distribution.
    """
    distribution_map = {
        "gaussian": np.random.normal,  # mean ('loc'), std deviation ('scale')
        "uniform": np.random.uniform,  # lower ('low'), upper ('high')
        "exponential": np.random.exponential,  # scale ('scale' or 1/lambda)
        "poisson": np.random.poisson,  # rate ('lam' or expected occurrences)
        "binomial": np.random.binomial,  # trials ('n'), success prob ('p')
        "gamma": np.random.gamma,  # shape ('shape'), scale ('scale')
        "beta": np.random.beta,  # alpha ('a'), beta ('b')
        "lognormal": np.random.lognormal,  # mean ('mean'), std ('sigma')
        "laplace": np.random.laplace,  # location ('loc'), scale ('scale')
    }

    if "distribution" not in distribution_data:
        msg = "Missing 'distribution' key in 'distribution_data'."
        raise KeyError(msg)

    dist_name = distribution_data["distribution"].lower()
    dist_function = distribution_map.get(dist_name)
    if not dist_function:
        msg = f"Distribution {dist_name} is not supported."
        raise ValueError(msg)

    args = {k: v for k, v in distribution_data.items() if k != "distribution"}
    args["size"] = 1

    try:
        sample = float(dist_function(**args)[0])
    except TypeError as e:
        msg = (
            "Invalid parameters provided for the specified distribution "
            "function in 'distribution_data'."
        )
        raise ValueError(msg) from e

    return sample
