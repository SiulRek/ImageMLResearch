from contextlib import AbstractContextManager
from copy import deepcopy
import json
import os
import warnings

from src.experimenting.helpers.create_experiment_report import create_experiment_report
from src.experimenting.helpers.experiment_data import (
    get_default_experiment_data,
    load_experiment_data,
)
from src.experimenting.helpers.time_utils import (
    get_datetime,
    get_duration,
    add_durations,
)
from src.experimenting.helpers.transform_figures_to_files import (
    transform_figures_to_files,
)
from src.experimenting.helpers.trial import Trial
from src.plotting.functions.plot_training_histories import plot_training_histories
from src.research.attributes.research_attributes import ResearchAttributes
from src.utils import Logger


class ExperimentError(Exception):
    """ Exception raised for errors that occur during the experiment. """


class Experiment(AbstractContextManager, ResearchAttributes):
    """ A context manager class to manage experiments and trials, inheriting from
    ResearchAttributes. """

    def __init__(
        self, research_attributes, directory, name, description, sort_metric="accuracy"
    ):
        """
        Initializes the Experiment with the given parameters.

        Args:
            - research_attributes (ResearchAttributes): The research
                attributes for the experiment.
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment. for the
                report.
            - sort_metric (str): The metric to sort the trials by. Default
                is "accuracy".

        NOTE:
            - `Experiment` is the only research module that requires
                `research_attributes` during initialization, as it simplifies
                the usage within a context manager.
        """
        exp_dir = self._make_experiment_directory(directory, name)
        self._init_logger(exp_dir)

        # ResearchAttributes required for the experiment.
        self._figures = {
            # Name: Figure
        }  # Read only
        self._evaluation_metrics = {
            # Set Name: Metrics -> {Metric: Value}
        }  # Read only
        self._training_history = {
            # Metric: List of values
        }  # Read only
        self.synchronize_research_attributes(research_attributes)

        self._init_experiment_data(exp_dir, name, description, sort_metric)

        self._no_trial_executed = True
        self._initial_trial_num = len(self.experiment_data["trials"])

    def _make_experiment_directory(self, directory, name):
        """
        Creates the experiment directory path, makes the directory, and returns
        the path.

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

    def _init_logger(self, directory):
        log_file = os.path.join(directory, "execution.log")
        self.logger = Logger(log_file, mode="a")

    def _init_experiment_data(self, exp_dir, name, description, sort_metric):
        """
        Initializes the experiment data to store the experiment information.

        Args:
            - exp_dir (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment.
            - sort_metric (str): The metric to sort the trials by.

        NOTE: 'directory' 'name' and 'description' are only used when the
        experiment is created for the first time and not when the experiment is
        resumed.
        """
        try:
            # Try loading existing experiment data to resume the experiment.
            experiment_data = load_experiment_data(exp_dir)
            self.logger.info(f"Resuming experiment: {name}")
        except FileNotFoundError:
            self.logger.info(f"Creating new experiment: {name}")
            experiment_data = get_default_experiment_data()
            # Assign directory and name only when creating a new experiment.
            experiment_data["directory"] = exp_dir
            experiment_data["name"] = name
        else:
            if exp_dir or name:
                msg = "Directory and name parameters are ignored when resuming"
                msg += "an experiment."
                warnings.warn(msg)
                msg = "Ignoring directory and/or name parameters"
                self.logger.warning(msg)

        # In any case, description and sort_metric are updated with
        # the given instanciation parameters. However, it is not
        # supported to change the directory or name of
        # the experiment after it is created.
        experiment_data["description"] = description
        experiment_data["sort_metric"] = sort_metric

        self.experiment_data = experiment_data

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
        Gets the current results (figures, evaluation_metrics, training_history)
        recorded in experiment.

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
        self.logger.info(f"Starting trial: {name}")
        if self._no_trial_executed:
            # Allow for figures outside of trials to be stored.
            figures = self._figures
            experiment_dir = self.experiment_data["directory"]
            figures = transform_figures_to_files(figures, experiment_dir)
            self.experiment_data["figures"] = figures
            self._no_trial_executed = False

        # Avoids conflicts between trials, as the ResearchAttributes are shared.
        self.reset_research_attributes(except_datasets=True)

        return Trial(self, name, hyperparameters)

    def _calculate_total_duration(self):
        """ Calculates the total duration of the experiment. """
        duration = get_duration(self.experiment_data["resume_time"])
        previous_duration = self.experiment_data["duration"] or "0"
        duration = add_durations(previous_duration, duration)
        self.experiment_data["duration"] = duration

    def _raise_exception_if_any(self, exc_type, exc_value, exc_traceback):
        """ Raises an exception if an exception occurred during the experiment. """
        if exc_type is not None:
            self.logger.error(f"Exception occurred:\n {exc_value}")
            # XXX: In case of an exception and at least one trial runned successfully
            # before, should an attempt to write the experiment data be done?
            # if self._initial_trial_num > len(self.experiment_data["trials"]):
            #     try:
            #         self._sort_trials()
            #         self._write_experiment_data()
            #         msg = "Experiment data is updated with available trials."
            #         self.logger.info(msg)
            #     except Exception as e:
            #         pass
            raise

    def _sort_trials(self):
        """ Sorts the trials by the specified sort metric in descending order. """
        if len(self.experiment_data["trials"]) <= 1:
            return

        sort_metric = self.experiment_data["sort_metric"]

        def sort_metric_val(trial):
            evaluation_metrics = trial["evaluation_metrics"]
            metrics_set = evaluation_metrics.get("test", {}) or evaluation_metrics.get(
                "complete", {}
            )
            value = metrics_set.get(sort_metric, None)
            if value is None:
                msg = f"{sort_metric} not found in evaluation metrics for\n"
                msg += f"Trial: {trial['name']}"
                self.logger.error(msg)
                raise ExperimentError(msg)
            return value

        self.experiment_data["trials"].sort(key=sort_metric_val, reverse=True)

    def _write_experiment_data(self):
        """ Writes the experiment data to a JSON file. """
        info_json = os.path.join(
            self.experiment_data["directory"], "experiment_info.json"
        )
        experiment_data = self.experiment_data.copy()
        # Only store the trial names in the experiment data
        # as the trial data is stored in separate files in the
        # trial directories.
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

        fig = plot_training_histories(histories, title="History of Best 3 Trials")
        figures = transform_figures_to_files(
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
        """
        self._calculate_total_duration()

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        msg = f"Finalizing experiment: {self.experiment_data['name']}"
        self.logger.info(msg)

        self._sort_trials()
        self._plot_history_of_best_3_trials()
        self._write_experiment_data()
        create_experiment_report(self.experiment_data)

        self.logger.close_logger()
