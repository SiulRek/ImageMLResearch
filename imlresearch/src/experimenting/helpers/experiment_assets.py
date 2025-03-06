from copy import deepcopy
import json
import os
import warnings

from imlresearch.src.experimenting.helpers.trial import normalize_trial_name

_DEFAULT_EXPERIMENT_ASSETS = {
    "name": None,  # Name of the experiment
    "description": None,  # Description of the experiment
    "directory": None,  # Directory where experiment assets are stored
    "sort_metric": "accuracy",  # Metric used for sorting results
    "start_time": None,  # Time when the experiment started
    "resume_time": None,  # Time when the experiment was resumed
    "duration": None,  # Total duration of the experiment
    "figures": {},  # Dictionary to store figures during the experiment
    "trials": [],  # List to store individual trial assets
}

_TRIAL_KEYS = {
    "name",  # Name of the trial
    "start_time",  # Time when the trial started
    "duration",  # Duration of the trial
    "directory",  # Directory where trial assets are stored
    "hyperparameters",  # Dictionary containing the hyperparameters
    "figures",  # Dictionary to store figures generated during the trial
    "evaluation_metrics",  # Dictionary to store evaluation metrics
    "training_history",  # Dictionary to store training history
}


def get_default_experiment_assets():
    """
    Return the default experiment assets.

    Returns
    -------
    dict
        The default experiment assets.
    """
    return deepcopy(_DEFAULT_EXPERIMENT_ASSETS)


def assert_experiment_assets_attribute(experiment_assets):
    """
    Assert that the experiment assets attribute has the expected keys.

    Parameters
    ----------
    experiment_assets : dict
        The experiment assets attribute to assert.
    """
    expected_keys = set(get_default_experiment_assets().keys())
    actual_keys = set(experiment_assets.keys())
    if expected_keys != actual_keys:
        missing_keys = expected_keys - actual_keys
        extra_keys = actual_keys - expected_keys
        msg = "Experiment assets attribute does not have the expected keys: "
        if missing_keys:
            msg += f"Missing keys: {missing_keys}. "
        if extra_keys:
            msg += f"Extra keys: {extra_keys}."
        raise ValueError(msg)


def assert_trial_assets_attribute(trial_assets):
    """
    Assert that the trial assets attribute has the expected keys.

    Parameters
    ----------
    trial_assets : dict
        The trial assets attribute to assert.
    """
    expected_keys = _TRIAL_KEYS
    actual_keys = set(trial_assets.keys())
    if expected_keys != actual_keys:
        missing_keys = expected_keys - actual_keys
        extra_keys = actual_keys - expected_keys
        msg = "Trial assets attribute does not have the expected keys:\n"
        if missing_keys:
            msg += f"Missing keys: {', '.join(missing_keys)}\n"
        if extra_keys:
            msg += f"Extra keys: {', '.join(extra_keys)}."
        raise ValueError(msg)


def load_trials(experiment_assets, experiment_dir):
    """
    Load the trial assets from the given experiment directory and the
    experiment assets.

    Parameters
    ----------
    experiment_assets : dict
        The experiment assets containing trial names.
    experiment_dir : str
        The directory to load the trial assets from.

    Returns
    -------
    None
    """
    experiment_dir = experiment_dir

    # Load existing trials from two sources
    tracked_names = experiment_assets["trials"]
    tracked_names = [normalize_trial_name(name) for name in tracked_names]

    # Load from experiment output directory
    paths = [
        os.path.join(experiment_dir, name)
        for name in os.listdir(experiment_dir)
    ]
    dirs = [path for path in paths if os.path.isdir(path)]
    dir_names = [os.path.basename(d) for d in dirs]
    dir_names = [normalize_trial_name(name) for name in dir_names]

    trial_names = list(set(tracked_names + dir_names))

    # Load trial dictionaries from their corresponding files
    trials = []
    for trial_name in trial_names:
        trial_file = os.path.join(
            experiment_dir, trial_name, "trial_info.json"
        )
        if os.path.exists(trial_file):
            with open(trial_file, "r", encoding="utf-8") as trial_f:
                trial_assets = json.load(trial_f)
                assert_trial_assets_attribute(trial_assets)
                trials.append(trial_assets)
        elif trial_name in tracked_names:
            msg = f"No trial_info.json found for trial {trial_name}."
            warnings.warn(msg)
    experiment_assets.update({"trials": trials})


def load_experiment_assets(experiment_dir):
    """
    Load the experiment assets from the given directory.

    Parameters
    ----------
    experiment_dir : str
        The directory to load the experiment assets from.

    Returns
    -------
    dict
        The loaded experiment assets.
    """
    experiment_info_path = os.path.join(
        experiment_dir, "experiment_info.json"
    )
    if not os.path.exists(experiment_info_path):
        msg = f"File {experiment_info_path} not found."
        raise FileNotFoundError(msg)

    with open(experiment_info_path, "r", encoding="utf-8") as f:
        experiment_assets = json.load(f)

    assert_experiment_assets_attribute(experiment_assets)

    load_trials(experiment_assets, experiment_dir)
    return experiment_assets
