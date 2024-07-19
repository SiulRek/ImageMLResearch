from copy import copy
import json
import os
import warnings

from src.experimenting.helpers.map_figures_to_paths import map_figures_to_paths
from src.experimenting.helpers.time_utils import get_datetime, get_duration
from src.research.attributes.attributes_utils import copy_public_properties
from src.research.attributes.research_attributes import ResearchAttributes


class TrialError(Exception):
    """ Exception raised for errors that occur during a trial. """


class Trial:
    """
    A class to manage individual trials within an experiment.

    Attributes:
        - experiment (Experiment): The experiment instance this trial
            belongs to.
        - research_attributes (ResearchAttributes): Research attributes from
        - trial_data (dict): Dictionary to store trial data.
        - keys: 'name', 'description', 'start_time', 'directory',
            'hyperparameters', 'figures', 'evaluation_metrics',
            'training_history' (optional).
        - trial_directory (str): Directory where the trial data is saved.
        - experiment_trials (list): Reference to the list of trials in the
            experiment, used to append the trial data.
    """

    def __init__(self, experiment, name, description, hyperparameters):
        """
        Initializes the Trial with the given parameters.

        Args:
            - experiment (Experiment): The experiment instance this trial
                belongs to.
            - description (str): The description of the trial.
            - hyperparameters (dict): Dictionary containing the
                hyperparameters.
        """
        self._assert_required_experiment_attributes(experiment)
        self._init_research_attributes(experiment)
        self._init_trial_data(name, description, hyperparameters, experiment)
        self.experiment_trials = experiment.experiment_data[
            "trials"
        ]  # Keep reference to track trials in experiment.
        self.get_trial_results = (
            experiment.get_results
        )  # Keep reference to retrieve results from trial.

    def _assert_required_experiment_attributes(self, experiment):
        """
        Assert if the experiment object has the required attributes.

        Args:
            - experiment (Experiment): The experiment instance to check.

        Raises:
            - AttributeError: If the experiment object does not have the
                required attributes.
        """
        required_attributes = ["figures", "evaluation_metrics"]
        for attr in required_attributes:
            if not hasattr(experiment, attr):
                msg = f"Experiment object does not have {attr} attribute."
                raise AttributeError(msg)

    def _init_research_attributes(self, experiment):
        """ Initialize the research attributes from the Experiment class. """
        self.research_attributes = ResearchAttributes()
        copy_public_properties(experiment, self.research_attributes)

    def _init_trial_data(self, name, description, hyperparameters, experiment):
        """
        Initialize the trial data dictionary to store trial information.

        Args:
            - name (str): The name of the trial.
            - description (str): The description of the trial.
            - hyperparameters (dict): The hyperparameters for the trial.
            - experiment (Experiment): The experiment instance.
            - dict: Initialized trial data dictionary.
        """
        trial_directory = self._make_trial_directory(
            experiment.experiment_data["directory"], name
        )
        self.trial_data = {
            "name": name,
            "description": description,
            "start_time": None,
            "duration": None,
            "directory": trial_directory,
            "hyperparameters": hyperparameters,
            "figures": {},
            "evaluation_metrics": {},
            "training_history": None,
        }

    def _make_trial_directory(self, experiment_directory, name):
        """
        Makes the directory for the trial.

        Args:
            - experiment_directory (str): The directory of the experiment.
            - name (str): The name of the trial.

        Returns:
            - str: The path to the trial directory.
        """
        trial_directory = os.path.join(
            experiment_directory,
            f"{name.replace(' ', '_')}",
        )
        os.makedirs(trial_directory, exist_ok=True)
        return trial_directory

    def __enter__(self):
        """
        Sets up the trial by creating the necessary directories.

        Returns:
            - self: The Trial instance.
        """
        os.makedirs(self.trial_data["directory"], exist_ok=True)
        self.trial_data["start_time"] = get_datetime()
        return self

    def _raise_exception_if_any(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            raise

    def _write_trial_data(self):
        """ Writes the trial data to a JSON file. """
        trial_info_json = os.path.join(self.trial_data["directory"], "trial_info.json")
        # Remove history
        trial_data = self.trial_data.copy()
        try:
            # Hyperparameters may not be JSON serializable.
            with open(trial_info_json, "w", encoding="utf-8") as f:
                json.dump(trial_data, f, indent=4)
        except TypeError:
            msg = "Hyperparameters are not JSON serializable for trial"
            msg += f"{trial_data['name']}. Saving None instead."
            warnings.warn(msg)
            trial_data["hyperparameters"] = None
            with open(trial_info_json, "w", encoding="utf-8") as f:
                json.dump(trial_data, f, indent=4)

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Saves the trial data and figures and creates experiment report.

        Args:
            - exc_type: The exception type if an exception occurred.
            - exc_value: The exception value if an exception occurred.
            - traceback: The traceback if an exception occurred. C
            - Raises:
            - TrialError: If an exception occurred during the trial.
        """
        duration = get_duration(self.trial_data["start_time"])
        self.trial_data["duration"] = duration

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        trial_results = self.get_trial_results()

        self.trial_data["figures"] = map_figures_to_paths(
            trial_results["figures"], self.trial_data["directory"]
        )
        self.trial_data["evaluation_metrics"] = copy(
            trial_results["evaluation_metrics"]
        )  # Copy as the source trial_results might be modified later (e.g. in next Trial)
        self.trial_data["training_history"] = copy(trial_results["training_history"])

        self._write_trial_data()

        self.experiment_trials.append(self.trial_data)
