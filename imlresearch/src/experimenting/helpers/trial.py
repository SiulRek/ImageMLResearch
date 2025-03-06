from contextlib import AbstractContextManager
from copy import copy
import json
import os
import shutil
import warnings

from imlresearch.src.experimenting.helpers.last_score_singleton import (
    LastScoreSingleton,
)
from imlresearch.src.research.attributes.attributes_utils import (
    copy_public_properties,
)
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.utils import transform_figures_to_files
from imlresearch.src.utils import get_datetime, get_duration


class ResultsEmptyError(ValueError):
    """
    Raised when trial results are empty and the trial was never run before.
    """


def normalize_trial_name(trial_name):
    """
    Normalize the trial name by converting it to lowercase and replacing
    spaces with underscores.

    Parameters
    ----------
    trial_name : str
        The name of the trial.

    Returns
    -------
    str
        The normalized trial name.
    """
    return trial_name.replace(" ", "_").lower()


class Trial(AbstractContextManager):
    """
    A context manager class to manage individual trials within an experiment.

    Attributes
    ----------
    experiment : Experiment
        The experiment instance this trial belongs to.
    research_attributes : ResearchAttributes
        Research attributes for the trial.
    trial_assets : dict
        Dictionary storing trial assets.
    trial_directory : str
        Directory where the trial assets are saved.
    experiment_trials : list
        Reference to the list of trials in the experiment.
    """

    def __init__(self, experiment, name, hyperparameters):
        """
        Initialize the Trial with the given parameters.

        Parameters
        ----------
        experiment : Experiment
            The experiment instance this trial belongs to.
        name : str
            The name of the trial.
        hyperparameters : dict
            Dictionary containing the hyperparameters.
        """
        self._assert_required_experiment_attributes(experiment)
        self._init_research_attributes(experiment)
        self._init_trial_assets(experiment, name, hyperparameters)
        self.experiment_trials = experiment.experiment_assets["trials"]
        self.fetch_trial_results = experiment.get_results
        self.logger = experiment.logger
        self._already_runned = self._check_if_already_runned()

    @property
    def already_runned(self):
        """
        Check if the trial has already been run.

        Returns
        -------
        bool
            True if the trial has been run before, False otherwise.
        """
        return self._already_runned

    def _assert_required_experiment_attributes(self, experiment):
        """
        Assert if the experiment object has the required attributes.

        Parameters
        ----------
        experiment : Experiment
            The experiment instance to check.

        Raises
        ------
        AttributeError
            If the experiment object does not have the required attributes.
        """
        required_attributes = ["figures", "evaluation_metrics"]
        for attr in required_attributes:
            if not hasattr(experiment, attr):
                msg = f"Experiment object does not have {attr} attribute."
                raise AttributeError(msg)

    def _init_research_attributes(self, experiment):
        """
        Initialize the research attributes from the Experiment class.
        """
        self.research_attributes = ResearchAttributes()
        copy_public_properties(experiment, self.research_attributes)

    def _init_trial_assets(self, experiment, name, hyperparameters):
        """
        Initialize the trial assets dictionary to store trial information.

        Parameters
        ----------
        experiment : Experiment
            The experiment instance.
        name : str
            The name of the trial.
        hyperparameters : dict
            The hyperparameters for the trial.
        """
        trial_directory = self._make_trial_directory(
            experiment.experiment_assets["directory"],
            normalize_trial_name(name),
        )
        self.trial_assets = {
            "name": name,
            "start_time": None,
            "duration": None,
            "directory": trial_directory,
            "hyperparameters": hyperparameters,
            "figures": None,
            "evaluation_metrics": None,
            "training_history": None,
        }

    def _make_trial_directory(self, experiment_directory, name):
        """
        Create the directory for the trial.

        Parameters
        ----------
        experiment_directory : str
            The directory of the experiment.
        name : str
            The name of the trial.

        Returns
        -------
        str
            The path to the trial directory.
        """
        trial_directory = os.path.join(
            experiment_directory,
            f"{name.replace(' ', '_')}".lower(),
        )
        os.makedirs(trial_directory, exist_ok=True)
        return trial_directory

    def _check_if_already_runned(self):
        """
        Check if the trial has already been run.

        Returns
        -------
        bool
            True if the trial exists in the experiment's trial list,
            False otherwise.
        """
        trial = self.trial_assets["name"]
        experiment_trials = [trial["name"] for trial in self.experiment_trials]
        return trial in experiment_trials

    def __enter__(self):
        """
        Set up the trial by creating the necessary directories.

        Returns
        -------
        Trial
            The Trial instance.
        """
        self.trial_assets["start_time"] = get_datetime()
        return self

    def _raise_exception_if_any(self, exc_type, exc_value, traceback):
        """
        Raise any encountered exception during trial execution.

        Parameters
        ----------
        exc_type : Exception type
            The exception type if an exception occurred.
        exc_value : Exception value
            The exception value if an exception occurred.
        traceback : traceback
            The traceback if an exception occurred.
        """
        if exc_type is not None:
            raise

    def _remove_trial(self, trial_name):
        """
        Remove the trial from the experiment's trial list.

        Parameters
        ----------
        trial_name : str
            The name of the trial to remove.
        """
        names = [trial["name"] for trial in self.experiment_trials]
        if trial_name not in names:
            msg = f"Trial {trial_name} not found in experiment trials."
            raise ValueError(msg)
        index = names.index(trial_name)
        trial = self.experiment_trials.pop(index)
        trial_dir = trial["directory"]
        shutil.rmtree(trial_dir)
        os.makedirs(trial_dir)

    def _write_trial_assets(self):
        """
        Write the trial assets to a JSON file.
        """
        trial_info_json = os.path.join(
            self.trial_assets["directory"], "trial_info.json"
        )
        trial_assets = self.trial_assets.copy()
        try:
            with open(trial_info_json, "w", encoding="utf-8") as f:
                json.dump(trial_assets, f, indent=4)
        except TypeError:
            msg = "Hyperparameters are not JSON serializable for trial "
            msg += f"{trial_assets['name']}. Saving None instead."
            warnings.warn(msg)
            self.logger.warning("Hyperparameters are not JSON serializable")
            trial_assets["hyperparameters"] = None
            with open(trial_info_json, "w", encoding="utf-8") as f:
                json.dump(trial_assets, f, indent=4)

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Save the trial assets, figures, and results.

        Parameters
        ----------
        exc_type : Exception type
            The exception type if an exception occurred.
        exc_value : Exception value
            The exception value if an exception occurred.
        traceback : traceback
            The traceback if an exception occurred.
        """
        duration = get_duration(self.trial_assets["start_time"])
        self.trial_assets["duration"] = duration

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        trial_results = self.fetch_trial_results()

        results_empty = all(value == {} for value in trial_results.values())
        trial_name = self.trial_assets["name"]
        if results_empty and self.already_runned:
            msg = f"Skipping '{trial_name}'. Already run, no new results."
            warnings.warn(msg)
            self.logger.warning(f"Skipping {trial_name}")
            LastScoreSingleton().set(None)
            return

        self.logger.info(f"Finalizing trial: {trial_name}")

        if results_empty:
            msg = f"'{trial_name}' produced no results. Nothing saved."
            warnings.warn(msg)
            self.logger.warning(f"{trial_name} produced no results")
            return

        if self.already_runned:
            msg = f"'{trial_name}' already run. Overwriting old results."
            warnings.warn(msg)
            self.logger.warning(f"Overwriting old results for {trial_name}")
            self._remove_trial(trial_name)

        self.trial_assets["figures"] = transform_figures_to_files(
            trial_results["figures"], self.trial_assets["directory"]
        )
        self.trial_assets["evaluation_metrics"] = copy(
            trial_results["evaluation_metrics"]
        )
        training_history = copy(trial_results["training_history"])
        self.trial_assets["training_history"] = training_history

        loss = training_history.get("val_loss") or training_history.get("loss")
        last_score = loss[-1] if loss else None
        if last_score is not None:
            LastScoreSingleton().set(last_score)

        self._write_trial_assets()
        self.experiment_trials.append(self.trial_assets)
