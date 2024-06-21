from datetime import datetime
import json
import os

from src.experimenting.helpers.trial import Trial
from src.research.attributes.research_attributes import ResearchAttributes


class ExperimentError(Exception):
    """ Exception raised for errors that occur during the experiment. """
    pass


class Experiment(ResearchAttributes):
    """
    A class to manage experiments and trials, inheriting from
    ResearchAttributes.

    Attributes:
        - experiment_directory (str): Directory where the experiment data is
            saved.
        - experiment_name (str): Name of the experiment.
        - experiment_description (str): Description of the experiment.
        - trials (list): List to store trial data.
    """

    def __init__(self, directory, name, description, label_type, category_names=None):
        """
        Initializes the Experiment with the given parameters.

        Args:
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment.
            - label_type (str): The type of labels used in the experiment.
            - category_names (list, optional): List of category names if
                applicable.
        """
        super().__init__(label_type, category_names)
        self.experiment_data = {
            "name": name,
            "description": description,
            "start_time": str(datetime.now()),
            "directory": os.path.abspath(os.path.normpath(directory)),
            "trials": [],
        }

    def __enter__(self):
        """
        Sets up the experiment by creating the necessary directories and files.

        Returns:
            - self: The Experiment instance.
        """
        os.makedirs(self.experiment_data["directory"], exist_ok=True)
        info_json = os.path.join(
            self.experiment_data["directory"], "experiment_info.json"
        )
        with open(info_json, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "experiment_name": self.experiment_data["name"],
                    "description": self.experiment_data["description"],
                    "start_time": self.experiment_data["start_time"],
                },
                f,
                indent=4,
            )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Cleans up the experiment and saves the report.

        Args:
            - exc_type: The exception type if an exception occurred.
            - exc_value: The exception value if an exception occurred.
            - traceback: The traceback if an exception occurred.

        Raises:
            - ExperimentError: If an exception occurred during the
                experiment.
        """
        if exc_type is not None:
            exc = exc_type(exc_value).with_traceback(traceback)
            msg = "An error occurred during the experiment."
            raise ExperimentError(msg) from exc
        self.experiment_data["end_time"] = str(datetime.now())
        report_json = os.path.join(
            self.experiment_data["directory"], "experiment_report.json"
        )
        with open(report_json, "w", encoding="utf-8") as f:
            json.dump(self.experiment_data, f, indent=4)

    def trial(self, trial_name, description, hyperparameters):
        """
        Context manager to handle trials within an experiment.

        Args:
            - trial_name (str): Name of the trial.
            - description (str): Description of the trial.
            - hyperparameters (dict): Dictionary containing the
                hyperparameters.

        Returns:
            - Trial: A Trial context manager instance.
        """
        return Trial(self, trial_name, description, hyperparameters)
