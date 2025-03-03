from contextlib import AbstractContextManager
from copy import deepcopy
import json
import os
import warnings

from imlresearch.src.experimenting.helpers.ai_support import (
    ask_for_experiment_analysis,
)
from imlresearch.src.experimenting.helpers.create_experiment_report import (
    create_experiment_report,
)
from imlresearch.src.experimenting.helpers.experiment_assets import (
    get_default_experiment_assets,
    load_experiment_assets,
)
from imlresearch.src.experimenting.helpers.trial import Trial
from imlresearch.src.plotting.functions.plot_training_histories import (
    plot_training_histories,
)
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.utils import (
    transform_figures_to_files,
    get_datetime,
    get_duration,
    add_durations,
    Logger,
)


class ExperimentError(Exception):
    """ Exception raised for errors that occur during the experiment. """


class Experiment(AbstractContextManager, ResearchAttributes):
    """
    A context manager class to manage experiments and trials, inheriting from
    ResearchAttributes.
    """

    def __init__(
        self,
        research_attributes,
        directory,
        name,
        description,
        sort_metric="accuracy",
        ask_for_analysis=False,
    ):
        """
        Initializes the Experiment with the given parameters.
        """
        out_dir = self._make_output_directory(directory)
        self._init_logger(out_dir)

        self._figures = {}
        self._evaluation_metrics = {}
        self._training_history = {}
        self.synchronize_research_attributes(research_attributes)

        self._init_experiment_assets(out_dir, name, description, sort_metric)

        self._no_trial_executed = True
        self._initial_trial_num = len(self.experiment_assets["trials"])

        self._ask_for_analysis = ask_for_analysis

    def _make_output_directory(self, experiment_dir):
        """
        Creates an output directory of the experiment within the given
        directory.
        """
        experiment_dir = os.path.abspath(os.path.normpath(experiment_dir))
        output_dir = os.path.join(experiment_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def _init_logger(self, directory):
        log_file = os.path.join(directory, "execution.log")
        self.logger = Logger(log_file, mode="a")

    def _init_experiment_assets(self, out_dir, name, description, sort_metric):
        """
        Initializes the experiment assets to store the experiment information.
        """
        try:
            experiment_assets = load_experiment_assets(out_dir)
            self.logger.info(f"Resuming experiment: {name}")
        except FileNotFoundError:
            self.logger.info(f"Creating new experiment: {name}")
            experiment_assets = get_default_experiment_assets()
            experiment_assets["directory"] = out_dir
            experiment_assets["name"] = name
        else:
            if out_dir or name:
                msg = (
                    "Directory and name parameters are ignored when resuming "
                    "an experiment."
                )
                warnings.warn(msg)
                self.logger.warning("Ignoring directory and/or name parameters")

        experiment_assets["description"] = description
        experiment_assets["sort_metric"] = sort_metric

        self.experiment_assets = experiment_assets

    def __enter__(self):
        """
        Sets up the experiment by creating the necessary directories and files.
        """
        datetime = get_datetime()
        if self.experiment_assets["start_time"] is None:
            self.experiment_assets["start_time"] = datetime
        self.experiment_assets["resume_time"] = datetime
        return self

    def get_results(self):
        """
        Gets the current results (figures, evaluation_metrics, training_history)
        recorded in experiment.
        """
        return {
            "figures": self._figures,
            "evaluation_metrics": self._evaluation_metrics,
            "training_history": self._training_history,
        }

    def run_trial(self, name, hyperparameters):
        """
        Runs a trial context manager within the experiment context manager.
        """
        self.logger.info(f"Starting trial: {name}")
        if self._no_trial_executed:
            figures = self._figures
            experiment_dir = self.experiment_assets["directory"]
            figures = transform_figures_to_files(figures, experiment_dir)
            self.experiment_assets["figures"] = figures
            self._no_trial_executed = False

        self.reset_research_attributes(except_datasets=True)

        return Trial(self, name, hyperparameters)

    def _calculate_total_duration(self):
        """ Calculates the total duration of the experiment. """
        duration = get_duration(self.experiment_assets["resume_time"])
        previous_duration = self.experiment_assets["duration"] or "0"
        duration = add_durations(previous_duration, duration)
        self.experiment_assets["duration"] = duration

    def _raise_exception_if_any(self, exc_type, exc_value, exc_traceback):
        """
        Raises an exception if an exception occurred during the experiment.
        """
        if exc_type is not None:
            self.logger.error(f"Exception occurred:\n {exc_value}")
            self._write_experiment_assets()
            raise

    def _sort_trials(self):
        """ Sorts the trials by the specified sort metric in descending order. """
        if len(self.experiment_assets["trials"]) <= 1:
            return

        sort_metric = self.experiment_assets["sort_metric"]

        def sort_metric_val(trial):
            evaluation_metrics = trial["evaluation_metrics"]
            metrics_set = (
                evaluation_metrics.get("test", {})
                or evaluation_metrics.get("complete", {})
            )
            value = metrics_set.get(sort_metric, None)
            if value is None:
                msg = f"{sort_metric} not found in evaluation metrics for "
                msg += f"Trial: {trial['name']}"
                self.logger.error(msg)
                raise ExperimentError(msg)
            return value

        self.experiment_assets["trials"].sort(
            key=sort_metric_val, reverse=True
        )

    def _write_experiment_assets(self):
        """ Writes the experiment assets to a JSON file. """
        info_json = os.path.join(
            self.experiment_assets["directory"], "experiment_info.json"
        )
        experiment_assets = self.experiment_assets.copy()
        experiment_assets["trials"] = [
            trial["name"] for trial in experiment_assets["trials"]
        ]

        with open(info_json, "w", encoding="utf-8") as f:
            json.dump(experiment_assets, f, indent=4)

    def _plot_history_of_best_3_trials(self):
        """
        Plots the best of 3 trials for the experiment. Skips plotting if there
        are less than 3 trials or if any of the histories are empty.
        """
        if len(self.experiment_assets["trials"]) < 3:
            return

        trials = self.experiment_assets["trials"][:3]

        histories = {}
        for trial in trials:
            name = trial["name"]
            history = deepcopy(trial["training_history"])
            if not history:
                return
            histories[name] = history

        fig = plot_training_histories(
            histories, title="History of Best 3 Trials"
        )
        figures = transform_figures_to_files(
            {"history_of_best_3_trials": fig},
            self.experiment_assets["directory"],
        )
        self.experiment_assets["figures"].update(figures)

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Cleans up the experiment and saves the report.
        """
        self._calculate_total_duration()

        self._raise_exception_if_any(exc_type, exc_value, traceback)

        msg = f"Finalizing experiment: {self.experiment_assets['name']}"
        self.logger.info(msg)

        self._sort_trials()
        self._plot_history_of_best_3_trials()
        self._write_experiment_assets()
        create_experiment_report(self.experiment_assets)

        self.logger.close_logger()

        if self._ask_for_analysis:
            ask_for_experiment_analysis(self.experiment_assets["directory"])
