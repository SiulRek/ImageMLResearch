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
    """
    Exception raised for errors occurring during the experiment.
    """


class Experiment(AbstractContextManager, ResearchAttributes):
    """
    A context manager for managing experiments and trials.

    Inherits from `ResearchAttributes` to facilitate research-related
    attributes.
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
        Initializes the experiment.

        Parameters
        ----------
        research_attributes : ResearchAttributes
            Research attributes to be used in the experiment.
        directory : str
            Directory where the experiment outputs will be stored.
        name : str
            Name of the experiment.
        description : str
            Description of the experiment.
        sort_metric : str, optional
            Metric to sort trials (default is 'accuracy').
        ask_for_analysis : bool, optional
            Whether to ask for AI-based experiment analysis.
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
        Creates an output directory for the experiment.

        Parameters
        ----------
        experiment_dir : str
            The base directory for the experiment.

        Returns
        -------
        str
            The full path to the experiment output directory.
        """
        experiment_dir = os.path.abspath(os.path.normpath(experiment_dir))
        output_dir = os.path.join(experiment_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def _init_logger(self, directory):
        """
        Initializes the logger.

        Parameters
        ----------
        directory : str
            The directory where logs should be stored.
        """
        log_file = os.path.join(directory, "execution.log")
        self.logger = Logger(log_file, mode="a")

    def _init_experiment_assets(self, out_dir, name, description, sort_metric):
        """
        Initializes or loads experiment assets.

        Parameters
        ----------
        out_dir : str
            The directory where experiment assets are stored.
        name : str
            Name of the experiment.
        description : str
            Description of the experiment.
        sort_metric : str
            The metric used for sorting trials.
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
        Sets up the experiment.

        Returns
        -------
        Experiment
            The experiment instance.
        """
        datetime = get_datetime()
        if self.experiment_assets["start_time"] is None:
            self.experiment_assets["start_time"] = datetime
        self.experiment_assets["resume_time"] = datetime
        return self

    def get_results(self):
        """
        Retrieves the current experiment results.

        Returns
        -------
        dict
            Dictionary containing figures, evaluation metrics, and training
            history.
        """
        return {
            "figures": self._figures,
            "evaluation_metrics": self._evaluation_metrics,
            "training_history": self._training_history,
        }

    def run_trial(self, name, hyperparameters):
        """
        Runs a trial within the experiment context.

        Parameters
        ----------
        name : str
            The name of the trial.
        hyperparameters : dict
            The hyperparameters for the trial.

        Returns
        -------
        Trial
            The trial instance.
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
        """
        Calculates the total duration of the experiment.
        """
        duration = get_duration(self.experiment_assets["resume_time"])
        previous_duration = self.experiment_assets["duration"] or "0"
        duration = add_durations(previous_duration, duration)
        self.experiment_assets["duration"] = duration

    def _raise_exception_if_any(self, exc_type, exc_value, exc_traceback):
        """
        Raises an exception if one occurred during the experiment.

        Parameters
        ----------
        exc_type : Exception
            The exception type.
        exc_value : Exception
            The exception instance.
        exc_traceback : traceback
            The traceback object.

        Raises
        ------
        Exception
            The original exception raised during the experiment.
        """
        if exc_type is not None:
            self.logger.error(f"Exception occurred:\n {exc_value}")
            self._write_experiment_assets()
            self.logger.close_logger()
            raise

    def _sort_trials(self):
        """
        Sorts trials based on the specified sort metric.
        """
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
        """
        Writes experiment assets to a JSON file.
        """
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
        Plots the training histories of the best 3 trials.

        Skips plotting if there are fewer than 3 trials or if any histories
        are empty.
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
        Cleans up and finalizes the experiment.
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
