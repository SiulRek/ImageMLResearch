import json
import os
import warnings

from imlresearch.src.experimenting.helpers.hparams_suggester import (
    HParamsSuggester,
)


class _TrialDefinitionsIterator:
    """
    Iterator for generating trial definitions.

    Parameters
    ----------
    suggester : HParamsSuggester
        The hyperparameters suggester object.
    num_trials : int
        The number of trials to generate.
    prefix : str
        The prefix for naming trials.
    """

    def __init__(self, suggester, num_trials, prefix):
        self.suggester = suggester
        self.num_trials = num_trials
        self.prefix = prefix
        self.trial_count = 0

    def __iter__(self):
        """
        Returns the iterator object.

        Returns
        -------
        _TrialDefinitionsIterator
            The iterator instance.
        """
        return self

    def __next__(self):
        """
        Generates the next trial definition.

        Returns
        -------
        dict
            The trial definition.
        """
        if self.trial_count == self.num_trials:
            raise StopIteration
        self.trial_count += 1
        name = f"{self.prefix}{self.trial_count}"
        hparams = self.suggester.suggest_next()
        return {"name": name, "hyperparameters": hparams}


def _load_definitions(definitions_json):
    """
    Loads experiment information from a JSON file.

    Parameters
    ----------
    definitions_json : str
        The path to the `definitions.json` file.

    Returns
    -------
    dict
        A dictionary containing experiment metadata.
    """
    if not os.path.exists(definitions_json):
        msg = f"{definitions_json} is not found in the experiment directory."
        raise FileNotFoundError(msg)
    with open(definitions_json, encoding="utf-8") as f:
        experiment_info = json.load(f)
    return experiment_info


def _assert_experiment_metadata(experiment_metadata):
    """
    Validates experiment metadata.

    Parameters
    ----------
    experiment_metadata : dict
        The experiment metadata to validate.
    """
    expected_keys = ["name", "description", "directory"]
    for key in expected_keys:
        msg = f"{key} is not found in experiment_metadata."
        assert key in experiment_metadata, msg


def _process_trial_definitions(trial_definitions, experiment_dir):
    """
    Processes the trial definitions to include trial names.

    Parameters
    ----------
    trial_definitions : list or dict
        The trial definitions, either a list of dictionaries or a dictionary
        containing hyperparameters configurations for `HParamsSuggester`.
    experiment_dir : str
        The directory of the experiment.

    Returns
    -------
    iterator
        An iterator of trial definitions.
    """
    if isinstance(trial_definitions, list):
        expected_keys = {"name", "hyperparameters"}
        for trial in trial_definitions:
            keys_match = set(trial.keys()) == expected_keys
            assert keys_match, (
                "Invalid keys in list elements of trial_definitions."
            )
        return iter(trial_definitions)

    if isinstance(trial_definitions, dict):
        num_trials = trial_definitions.pop("num_trials", 1)  # Default: 1 trial
        prefix = trial_definitions.pop("prefix", "trial_")
        hparams_configs = trial_definitions.pop("hparams_configs", None)
        msg = "hparams_configs is not a key in trial_definitions."
        assert hparams_configs is not None, msg
        if trial_definitions:
            for key in trial_definitions.keys():
                msg = f"Ignoring key '{key}' in trial_definitions."
                warnings.warn(msg)
        try:
            suggester = HParamsSuggester(
                hparams_configs, storage_dir=experiment_dir
            )
        except AssertionError as e:
            msg = "Invalid hparams_configs in trial_definitions."
            raise AssertionError(msg) from e
        return _TrialDefinitionsIterator(suggester, num_trials, prefix)

    msg = "trial_definitions should be a list or a dict."
    raise ValueError(msg)


def load_experiment_definition(definition_json):
    """
    Loads experiment metadata and trial definitions from a JSON file.

    Parameters
    ----------
    definition_json : str
        The path to the JSON file containing the experiment definition.

    Returns
    -------
    tuple
        A tuple containing:
        - dict: Experiment metadata.
        - iterator: Trial definitions.
    """
    exp_def = _load_definitions(definition_json)
    msg = "Expected 2 keys in the definition file."
    assert len(exp_def) == 2, msg
    msg = "experiment_metadata is not found in the definition file."
    assert "experiment_metadata" in exp_def, msg
    msg = "trial_definitions is not found in the definition file."
    assert "trial_definitions" in exp_def, msg
    experiment_metadata = exp_def["experiment_metadata"]
    _assert_experiment_metadata(experiment_metadata)
    experiment_dir = experiment_metadata["directory"]
    trial_definitions = exp_def["trial_definitions"]
    trial_definitions = _process_trial_definitions(
        trial_definitions, experiment_dir
    )
    return experiment_metadata, trial_definitions
