from datetime import datetime
import json
import os


class TrialError(Exception):
    """ Exception raised for errors that occur during a trial. """

    pass


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
        self.experiment = experiment
        self.trial_data = {
            "trial_name": trial_name,
            "description": description,
            "start_time": str(datetime.now()),
            "hyperparameters": hyperparameters,
            "figures": {},
            "evaluation_metrics": {},
        }
        self.trial_directory = os.path.join(
            self.experiment.experiment_data["directory"],
            f"trial_{self.trial_data['trial_name']}",
        )

    def __enter__(self):
        """
        Sets up the trial by creating the necessary directories.

        Returns:
            - self: The Trial instance.
        """
        os.makedirs(self.trial_directory, exist_ok=True)
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
            name: f"{self.trial_directory}/{name}.png"
            for name in self.experiment.figures
        }

        for name, fig in self.experiment.figures.items():
            fig.savefig(self.trial_data["figures"][name])

        self.trial_data["evaluation_metrics"] = self.experiment.evaluation_metrics

        self.experiment.experiment_data["trials"].append(self.trial_data)

        #TODO: Create experiment report
        trial_info_json = os.path.join(self.trial_directory, "trial_info.json")
        with open(trial_info_json, "w", encoding="utf-8") as f:
            json.dump(self.trial_data, f, indent=4)
