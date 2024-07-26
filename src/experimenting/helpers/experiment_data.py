from copy import deepcopy
import json
import os
import warnings

_DEFAULT_EXPERIMENT_DATA = {
    "name": None,  # Name of the experiment
    "description": None,  # Description of the experiment
    "directory": None,  # Directory where experiment data is stored
    "sort_metric": "accuracy",  # Metric used for sorting results
    # (default is 'accuracy')
    "start_time": None,  # Time when the experiment started
    # (set at the end of __enter__)
    "resume_time": None,  # Time when the experiment was resumed
    "duration": None,  # Total duration of the experiment
    # (calculated at the beginning of __exit__)
    "figures": {},  # Dictionary to store figures generated during the experiment
    "trials": [],  # List to store individual trial data
}

_TRIAL_KEYS = {
    "name",  # Name of the trial
    "start_time",  # Time when the trial started
    # (set at the end of __enter__)
    "duration",  # Duration of the trial
    # (calculated at the beginning of __exit__)
    "directory",  # Directory where trial data is stored
    "hyperparameters",  # Dictionary containing the hyperparameters
    "figures",  # Dictionary to store figures generated during the trial
    "evaluation_metrics",  # Dictionary to store evaluation metrics
    "training_history",  # Dictionary to store training history
}


def get_default_experiment_data():
    """
    Returns the default experiment data.

    Returns:
        - dict: The default experiment data.
    """
    return deepcopy(_DEFAULT_EXPERIMENT_DATA)


def assert_experiment_data(experiment_data):
    """
    Asserts that the experiment data has the expected keys.

    Args:
        - experiment_data (dict): The experiment data to assert.

    Raises:
        - ValueError: If the experiment data does not have the expected
            keys.
    """
    expected_keys = set(get_default_experiment_data().keys())
    actual_keys = set(experiment_data.keys())
    if expected_keys != actual_keys:
        missing_keys = expected_keys - actual_keys
        extra_keys = actual_keys - expected_keys
        msg = "Experiment data does not have the expected keys: "
        if missing_keys:
            msg += f"Missing keys: {missing_keys}."
        if extra_keys:
            msg += f"Extra keys: {extra_keys}."
        raise ValueError(msg)


def assert_trial_data(trial_data):
    """
    Asserts that the trial data has the expected keys.

    Args:
        - trial_data (dict): The trial data to assert.

    Raises:
        - ValueError: If the trial data does not have the expected keys.
    """
    expected_keys = _TRIAL_KEYS
    actual_keys = set(trial_data.keys())
    if expected_keys != actual_keys:
        missing_keys = expected_keys - actual_keys
        extra_keys = actual_keys - expected_keys
        msg = "Trial data does not have the expected keys:\n "
        if missing_keys:
            msg += f"Missing keys: {missing_keys}."
        if extra_keys:
            msg += f"Extra keys: {extra_keys}."
        raise ValueError(msg)


def load_experiment_data(experiment_dir):
    """
    Loads the experiment data from the given directory. Raises FileNotFoundError
    if the experiment data file is not found.

    Args:
        - experiment_dir (str): The directory to load the experiment data
            from.
        - default_experiment_data (dict): The default experiment data to
            initialize if the directory is empty.

    Returns:
        - dict: The loaded or initialized experiment data.
    """
    experiment_info_path = os.path.join(experiment_dir, "experiment_info.json")
    if not os.path.exists(experiment_info_path):
        msg = f"File {experiment_info_path} not found."
        raise FileNotFoundError(msg)

    with open(experiment_info_path, "r", encoding="utf-8") as f:
        experiment_data = json.load(f)

    assert_experiment_data(experiment_data)

    # Load trial dictionaries from their corresponding files
    trials = []
    for trial_name in experiment_data["trials"]:
        folder_name = trial_name.replace(" ", "_")
        trial_file = os.path.join(experiment_dir, folder_name, "trial_info.json")
        if os.path.exists(trial_file):
            with open(trial_file, "r", encoding="utf-8") as trial_f:
                trial_data = json.load(trial_f)
                assert_trial_data(trial_data)
                trials.append(trial_data)
        else:
            msg = f"No trial_info.json found for trial {trial_name}."
            warnings.warn(msg)
    experiment_data["trials"] = trials
    return experiment_data
