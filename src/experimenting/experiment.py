from contextlib import AbstractContextManager
from copy import deepcopy
import json
import os

from src.experimenting.helpers.create_experiment_report import create_experiment_report
from src.experimenting.helpers.experiment_data import (
    get_default_experiment_data,
    load_experiment_data,
)
from src.experimenting.helpers.map_figures_to_paths import map_figures_to_paths
from src.experimenting.helpers.time_utils import (
    get_datetime,
    get_duration,
    add_durations,
)
from src.experimenting.helpers.trial import Trial
from src.plotting.functions.plot_training_histories import plot_training_histories
from src.research.attributes.research_attributes import ResearchAttributes


class ExperimentError(Exception):
    """ Exception raised for errors that occur during the experiment. """


class Experiment(AbstractContextManager, ResearchAttributes):
    """ A class to manage experiments and trials, inheriting from
    ResearchAttributes. """

    def __init__(
        self, research_attributes, directory, name, description, report_kwargs=None
    ):
        """
        Initializes the Experiment with the given parameters.

        Args:
            - research_attributes (ResearchAttributes): The research
                attributes for the experiment.
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment.
            - report_kwargs (dict, optional): Additional keyword arguments
                for the report.

        Note:
            - `Experiment` is the only research module that requires
                `research_attributes` during initialization, as it simplifies
                the usage within a context manager.
        """
        # Not initializing ResearchAttributes here,
        # prefer call synchronize_research_attributes explicitly.
        # super().__init__()

        # Initialize research attributes used in the Experiment.
        # Note, each time a Trial starts the research attributes are reset
        # (except datasets) to avoid conflicts between trials.
        self._figures = {
            # Name: Figure
        }  # Read only
        self._evaluation_metrics = {
            # Set Name: Metrics -> {Metric: Value}
        }  # Read only
        self._training_history = {
            # Metric: List of values
        }  # Read only
        self._init_experiment_data(directory, name, description)
        self.synchronize_research_attributes(research_attributes)
        self.report_kwargs = report_kwargs or {}
        self._no_trial_executed = True

    def _init_experiment_data(self, directory, name, description):
        """
        Initializes the experiment data to store the experiment information.

        Args:
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment.
        """
        experiment_directory = self._make_experiment_directory(directory, name)
        try:
            # Try loading existing experiment data to resume the experiment.
            experiment_data = load_experiment_data(experiment_directory)
        except FileNotFoundError:
            experiment_data = get_default_experiment_data()
        experiment_data["description"] = description
        experiment_data["directory"] = experiment_directory
        experiment_data["name"] = name
        self.experiment_data = experiment_data

    def _make_experiment_directory(self, directory, name):
        """
        Creates the experiment directory.

        Args:
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.

        Returns:
            - str: The path to the experiment directory.
        """
        directory = os.path.abspath(os.path.normpath(directory))
        name = name.replace(" ", "_")
        experiment_dir = os.path.join(directory, name)
        os.makedirs(experiment_dir, exist_ok=True)
        return experiment_dir

    def __enter__(self):
        """
        Sets up the experiment by creating the necessary directories and files.

        Returns:
            - self: The Experiment instance.
        """
        datetime = get_datetime()
        if self.experiment_data["start_time"] is None:
            self.experiment_data["start_time"] = datetime
        self.experiment_data["resume_time"] = datetime
        return self

    def get_results(self):
        """
        Gets the current results (figures and evaluation_metrics) recorded in
        experiment.

        Returns:
            - dict: A dictionary containing the figures and
                evaluation_metrics.
        """
        return {
            "figures": self._figures,
            "evaluation_metrics": self._evaluation_metrics,
            "training_history": self._training_history,
        }

    def run_trial(self, name, hyperparameters):
        """
        Runs a trial context manager within the experiment context manager.

        Args:
            - name (str): Name of the trial.
            - hyperparameters (dict): Dictionary containing the
                hyperparameters.

        Returns:
            - Trial: A Trial context manager instance.
        """
        if self._no_trial_executed:
            # Allow for figures outside of trials.
            figures = self._figures
            experiment_dir = self.experiment_data["directory"]
            figures = map_figures_to_paths(figures, experiment_dir)
            self.experiment_data["figures"] = figures
            self._no_trial_executed = False

        # Avoids conflicts between trials.
        self.reset_research_attributes(except_datasets=True)

        return Trial(self, name, hyperparameters)

    def _calculate_total_duration(self):
        """ Calculates the total duration of the experiment. """
        duration = get_duration(self.experiment_data["resume_time"])
        previous_duration = self.experiment_data["duration"] or "0"
        duration = add_durations(previous_duration, duration)
        self.experiment_data["duration"] = duration

    def _raise_exception_if_any(self, exc_type, exc_value, traceback):
        """ Raises an exception if an exception occurred during the experiment. """
        if exc_type is not None:
            raise

    def _sort_trials(self):
        """ Sorts the trials by the accuracy in descending order. """
        if self.experiment_data["trials"] == []:
            return

        def get_accuracy(trial):
            evaluation_metrics = trial["evaluation_metrics"]
            metrics_set = evaluation_metrics.get("test", {}) or evaluation_metrics.get(
                "complete", {}
            )
            accuracy = metrics_set.get("accuracy", None)
            if accuracy is None:
                msg = "Accuracy not found in evaluation metrics for Trial"
                msg += f"{trial['name']}"
                raise ExperimentError(msg)
            return accuracy

        self.experiment_data["trials"].sort(key=lambda x: get_accuracy(x), reverse=True)

    def _write_experiment_data(self):
        """ Writes the experiment data to a JSON file. """
        info_json = os.path.join(
            self.experiment_data["directory"], "experiment_info.json"
        )
        experiment_data = self.experiment_data.copy()
        experiment_data["trials"] = [
            trial["name"] for trial in experiment_data["trials"]
        ]

        with open(info_json, "w", encoding="utf-8") as f:
            json.dump(
                experiment_data,
                f,
                indent=4,
            )

    def _plot_history_of_best_3_trials(self):
        """ Plots the best of 3 trials for the experiment. Skipps plotting if there
        are less than 3 trials or if any of the histories are empty. """
        if len(self.experiment_data["trials"]) < 3:
            return

        trials = self.experiment_data["trials"][:3]

        histories = {}
        for trial in trials:
            name = trial["name"]
            history = deepcopy(trial["training_history"])
            if not history:
                # If at least one history is empty, skip plotting.
                return
            histories[name] = history

        fig = plot_training_histories(histories)
        figures = map_figures_to_paths(
            {"history_of_best_3_trials": fig}, self.experiment_data["directory"]
        )
        self.experiment_data["figures"].update(figures)

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
        self._calculate_total_duration()

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        self._sort_trials()

        self._plot_history_of_best_3_trials()
        self._write_experiment_data()
        create_experiment_report(self.experiment_data, **self.report_kwargs)
