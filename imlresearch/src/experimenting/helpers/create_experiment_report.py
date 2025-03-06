import os

from imlresearch.src.utils import MarkdownFileWriter


def _get_results_summary_table(experiment_assets):
    """
    Generate a summary table for the experiment results of all trials.

    Parameters
    ----------
    experiment_assets : dict
        Dictionary containing experiment assets.

    Returns
    -------
    dict
        Dictionary containing the summary table with metrics as keys
        and trial names as sub-keys.
    """
    results_table = dict()
    chapters = dict()
    trials = experiment_assets.get("trials", [])

    # Rows correspond to trials, columns correspond to metrics.
    for trial in trials:
        row = trial.get("name", "No Name")
        chapters[row] = f"[Chapter](#{row.lower().replace(' ', '-')})"
        metrics = trial.get("evaluation_metrics", {})
        metrics = metrics.get("test", metrics.get("complete", {}))
        for col, value in metrics.items():
            if col == "classification_report":
                continue
            if col not in results_table:
                results_table[col] = {}
            results_table[col][row] = value
    results_table["Chapters"] = chapters
    return results_table


def _get_hyperparameters_summary_table(experiment_assets):
    """
    Generate a hyperparameters summary table of all trials in the experiment.

    Parameters
    ----------
    experiment_assets : dict
        Dictionary containing experiment assets.

    Returns
    -------
    dict
        Dictionary containing the summary table with hyperparameters as keys
        and trial names as sub-keys.
    """
    hparam_table = dict()
    chapters = dict()
    trials = experiment_assets.get("trials", [])

    # Rows correspond to trials, columns correspond to hyperparameters.
    for trial in trials:
        row = trial.get("name", "No Name")
        chapters[row] = f"[Chapter](#{row.lower().replace(' ', '-')})"
        hparams = trial.get("hyperparameters", {})
        for col, value in hparams.items():
            if col not in hparam_table:
                hparam_table[col] = {}
            hparam_table[col][row] = value
    hparam_table["Chapters"] = chapters
    return hparam_table


def _pop_classification_reports(trial):
    """
    Pop the classification reports from the evaluation metrics of a trial.

    Parameters
    ----------
    trial : dict
        Dictionary containing trial assets.

    Returns
    -------
    list
        List of classification reports maintaining the order of the
        metrics sets in the evaluation metrics dictionary.

    Notes
    -----
    This function modifies the original evaluation metrics dictionary
    by removing the classification reports.
    """
    classification_reports = []
    for metrics_set in trial.get("evaluation_metrics", {}).values():
        if "classification_report" in metrics_set:
            classification_report = metrics_set.pop("classification_report")
            classification_reports.append(classification_report)
        else:
            classification_reports.append({})
    return classification_reports


def create_experiment_report(experiment_assets):
    """
    Generate a comprehensive experiment report in Markdown format and save it
    to a file.

    Parameters
    ----------
    experiment_assets : dict
        Dictionary containing experiment assets.
    """
    def from_exp_get(key, default="N/A"):
        return experiment_assets.get(key, default)

    report_dir = from_exp_get("directory")
    report_path = os.path.join(report_dir, "experiment_report.md")
    writer = MarkdownFileWriter(report_path)

    # Write Experiment Metadata
    writer.write_title(f"Experiment Report: {from_exp_get('name')}", level=1)
    writer.write_title("Metadata", level=2)
    writer.write_key_value("Description", from_exp_get("description"))
    start_time = from_exp_get("start_time").split(".")[0]
    writer.write_key_value("Start Time", start_time)
    resume_time = from_exp_get("resume_time").split(".")[0]
    if resume_time != start_time:
        writer.write_key_value("Last Resume Time", resume_time)
    writer.write_key_value("Total Duration", from_exp_get("duration"))

    exp_dir_link = writer.create_link(from_exp_get("directory"), "Link")
    writer.write_key_value("Directory", exp_dir_link)

    # Show Initial Visualizations
    if "figures" in experiment_assets and experiment_assets["figures"]:
        writer.write_title("Initial Visualizations", level=2, page_break=True)
        for fig_name, fig_path in experiment_assets["figures"].items():
            writer.write_figure(fig_name, fig_path)

    # Write Description Summary
    writer.write_title("Summary", level=2)
    writer.write_title("Hyperparameters", level=3)
    hyperparameter_table = _get_hyperparameters_summary_table(experiment_assets)
    writer.write_nested_table(hyperparameter_table)

    # Write Results Summary
    writer.write_title("Test Results", level=3)
    results_table = _get_results_summary_table(experiment_assets)
    writer.write_nested_table(results_table)

    # Write Trials
    trials = from_exp_get("trials", [])
    for trial in trials:

        def from_trial_get(key, default="N/A"):
            return trial.get(key, default)

        # Write Trial Metadata
        writer.write_title(from_trial_get("name"), level=2, page_break=True)
        start_time = from_trial_get("start_time").split(".")[0]
        writer.write_key_value("Start Time", start_time)
        writer.write_key_value("Duration", from_trial_get("duration"))

        trial_dir_link = writer.create_link(
            from_trial_get("directory"), "Link"
        )
        writer.write_key_value("Directory", trial_dir_link)

        hyperparameter_table = {
            param: str(value)
            for param, value in from_trial_get("hyperparameters", {}).items()
        }
        writer.write_title("Hyperparameters:", level=3)
        writer.write_key_value_table(
            hyperparameter_table,
            key_label="Hyperparameter",
            value_label="Value"
        )

        # The last classification report is the test set report.
        classification_report = _pop_classification_reports(trial)[-1]

        # Write Evaluation Metrics
        writer.write_title("Evaluation Metrics:", level=3)
        evaluation_metrics_table = from_trial_get("evaluation_metrics", {})
        writer.write_nested_table(evaluation_metrics_table)

        # Show Plots
        writer.write_title("Figures:", level=3, page_break=True)
        for fig_name, fig_path in trial["figures"].items():
            writer.write_figure(fig_name, fig_path)

        # Write Classification Report
        writer.write_title(
            "Detailed Report of Test Set:",
            level=3,
            page_break=True
        )
        writer.write_nested_table(classification_report, transpose=True)

    writer.save_file()
