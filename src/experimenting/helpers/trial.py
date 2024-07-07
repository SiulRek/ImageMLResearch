import json
import os
import warnings

from src.experimenting.helpers.datetime_utils import get_datetime, get_duration
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
        # Reset attributes in experiment to avoid conflicts with other trials.
        experiment.reset_research_attributes(except_datasets=True)
        # Class Trial uses the research attributes from Experiment class.
        self.research_attributes = ResearchAttributes()
        copy_public_properties(experiment, self.research_attributes)
        experiment_directory = experiment.experiment_data["directory"]
        trial_directory = self._make_trial_directory(experiment_directory, name)
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

    def _write_trial_data(self):
        """ Writes the trial data to a JSON file. """
        trial_info_json = os.path.join(self.trial_data["directory"], "trial_info.json")
        # Remove history
        trial_data = self.trial_data.copy()
        trial_data.pop("training_history")
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
            exc = exc_type(exc_value).with_traceback(traceback)
            msg = "An error occurred during the trial."
            raise TrialError(msg) from exc

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Saves the trial data and figures and creates experiment report.

        Args:
            - exc_type: The exception type if an exception occurred.
            - exc_value: The exception value if an exception occurred.
            - traceback: The traceback if an exception occurred.

        Raises:
            - TrialError: If an exception occurred during the trial.
        """
        duration = get_duration(self.trial_data["start_time"])
        self.trial_data["duration"] = duration

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        trial_results = self.get_trial_results()
        # Assign 'figures' to trial_data replacing the figure objects
        # with their created paths.
        self.trial_data["figures"] = {
            name: f"{self.trial_data['directory']}/{name}.png"
            for name in trial_results["figures"]
        }
        for path, fig in zip(
            self.trial_data["figures"].values(), trial_results["figures"].values()
        ):
            fig.savefig(path)

        self.trial_data["evaluation_metrics"] = trial_results["evaluation_metrics"]

        self._write_trial_data()

        if self.research_attributes.training_history:
            self.trial_data["training_history"] = (
                self.research_attributes.training_history
            )
        self.experiment_trials.append(self.trial_data)
