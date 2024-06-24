from datetime import datetime
import json
import os
import warnings


class TrialError(Exception):
    """ Exception raised for errors that occur during a trial. """


class Trial:
    """
    A class to manage individual trials within an experiment.

    Attributes:
        - experiment (Experiment): The experiment instance this trial
            belongs to.
        - trial_data (dict): Dictionary to store trial data.
        - trial_directory (str): Directory where the trial data is saved.
    """

    def __init__(self, experiment, trial_name, description, hyperparameters):
        """
        Initializes the Trial with the given parameters.

        Args:
            - experiment (Experiment): The experiment instance this trial
                belongs to.
            - trial_name (str): The name of the trial.
            - description (str): The description of the trial.
            - hyperparameters (dict): Dictionary containing the
                hyperparameters.
        """
        self._assert_required_experiment_attributes(experiment)
        self.experiment = experiment
        trial_directory = self._make_trial_directory(trial_name)
        self.trial_data = {
            "trial_name": trial_name,
            "description": description,
            "start_time": str(datetime.now()),
            "directory": trial_directory,
            "hyperparameters": hyperparameters,
            "figures": {},
            "evaluation_metrics": {},
        }
        try:
            self._write_trial_data()
        # Hyperparameters may not be JSON serializable
        except TypeError:
            msg = "Hyperparameters are not JSON serializable for trial"
            msg += f"{trial_name}. Saving None instead."
            warnings.warn(msg)
            self.trial_data["hyperparameters"] = None
            self._write_trial_data()

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

    def _make_trial_directory(self, trial_name):
        """
        Makes the directory for the trial.

        Args:
            - trial_name (str): The name of the trial.

        Returns:
            - str: The path to the trial directory.
        """
        trial_directory = os.path.join(
            self.experiment.experiment_data["directory"],
            f"trial_{trial_name.replace(' ', '_')}",
        )
        os.makedirs(trial_directory, exist_ok=True)
        return trial_directory

    def _write_trial_data(self):
        """ Writes the trial data to a JSON file. """
        trial_info_json = os.path.join(self.trial_data["directory"], "trial_info.json")
        with open(trial_info_json, "w", encoding="utf-8") as f:
            json.dump(self.trial_data, f, indent=4)

    def __enter__(self):
        """
        Sets up the trial by creating the necessary directories.

        Returns:
            - self: The Trial instance.
        """
        # Reset the figures and evaluation metrics for the trial
        self.experiment.figures = {}
        self.experiment.evaluation_metrics = {}
        os.makedirs(self.trial_data["directory"], exist_ok=True)
        return self

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
        if exc_type is not None:
            exc = exc_type(exc_value).with_traceback(traceback)
            msg = "An error occurred during the trial."
            raise TrialError(msg) from exc

        self.trial_data["figures"] = {
            name: f"{self.trial_data['directory']}/{name}.png"
            for name in self.experiment.figures
        }

        for name, fig in self.experiment.figures.items():
            fig.savefig(self.trial_data["figures"][name])

        self.trial_data["evaluation_metrics"] = self.experiment.evaluation_metrics

        self.experiment.experiment_data["trials"].append(self.trial_data)

        trial_info_json = os.path.join(self.trial_data["directory"], "trial_info.json")
        with open(trial_info_json, "w", encoding="utf-8") as f:
            json.dump(self.trial_data, f, indent=4)
