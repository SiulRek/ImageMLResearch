import os

from src.experimenting.helpers.markdown_file_writer import MarkdownFileWriter


def _get_results_summary_table(experiment_data):
    """
    Generate a summary table for the experiment results of all trials.

    Args:
        - experiment_data (dict): Dictionary containing experiment data.

    Returns:
        - dict: Dictionary containing the summary table with metrics as keys
            and trial names as sub-keys.
    """

    results_table = dict()
    chapters = dict()
    trials = experiment_data.get("trials", [])

    # Rows correspond to trials, columns correspond to metrics.
    for trial in trials:
        row = trial.get("name", "No Name")
        chapters[row] = f"[Chapter](#{row.lower().replace(' ', '-')})"
        metrics = trial.get("evaluation_metrics", {})
        metrics = metrics.get("test", metrics.get("complete", {}))
        for col, value in metrics.items():
            if col not in results_table:
                results_table[col] = {}
            results_table[col][row] = value
    results_table["Chapters"] = chapters
    return results_table


def _get_hyperparameters_summary_table(experiment_data):
    """
    Generate a hyperaparameters summary table of all trials in the experiment.

    Args:
        - experiment_data (dict): Dictionary containing experiment data.

    Returns:
        - dict: Dictionary containing the summary table with metrics as keys
            and trial names as sub-keys.
    """

    hparam_table = dict()
    chapters = dict()
    trials = experiment_data.get("trials", [])

    # Rows correspond to trials, columns correspond to metrics.
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


def create_experiment_report(experiment_data):
    """
    Generate a comprehensive experiment report in Markdown format and save it to
    a file.

    Args:
        - experiment_data (dict): Dictionary containing experiment data.
    """

    def from_exp_get(key, default="N/A"):
        return experiment_data.get(key, default)

    report_path = os.path.join(from_exp_get("directory"), "experiment_report.md")
    writer = MarkdownFileWriter(report_path)

    # Write Experiment Metadata
    writer.write_title(f"Experiment Report: {from_exp_get('name')}", level=1)
    writer.write_title("Metadata", level=2)
    writer.write_key_value("Description", from_exp_get("description"))
    start_time = from_exp_get("start_time").split(".")[0]
    writer.write_key_value("Start Time", start_time)
    writer.write_key_value("Duration", from_exp_get("duration"))
    experiment_directory_link = writer.create_link(from_exp_get("directory"), "Link")
    writer.write_key_value("Directory", experiment_directory_link)

    # Show Initial Visualizations
    if "figures" in experiment_data and experiment_data["figures"]:
        writer.write_title("Initial Visualizations", level=2)
        for fig_name, fig_path in experiment_data["figures"].items():
            writer.write_figure(fig_name, fig_path)

    # Write Description Summary
    writer.write_title("Summary", level=2)
    writer.write_title("Hyperparameters", level=3)
    hyperparameter_table = _get_hyperparameters_summary_table(experiment_data)
    writer.write_nested_table(hyperparameter_table)

    # Write Results Summary
    writer.write_title("Test Results", level=3)
    results_table = _get_results_summary_table(experiment_data)
    writer.write_nested_table(results_table)

    # Write Trials
    trials = from_exp_get("trials", [])
    for trial in trials:

        def from_trial_get(key, default="N/A"):
            return trial.get(key, default)

        writer.write_title(from_trial_get("name"), level=2)
        start_time = from_trial_get("start_time").split(".")[0]
        writer.write_key_value("Start Time", start_time)
        writer.write_key_value("Duration", from_trial_get("duration"))
        trial_directory_link = writer.create_link(from_trial_get("directory"), "Link")
        writer.write_key_value("Directory", trial_directory_link)
        hyperparameter_table = {
            param: str(value)
            for param, value in from_trial_get("hyperparameters", {}).items()
        }
        writer.write_title("Hyperparameters:", level=3)
        writer.write_key_value_table(
            hyperparameter_table, key_label="Hyperparameter", value_label="Value"
        )

        if "figures" in trial and trial["figures"]:
            writer.write_title("Figures:", level=3)
            for fig_name, fig_path in trial["figures"].items():
                writer.write_figure(fig_name, fig_path)

        if "evaluation_metrics" in trial and trial["evaluation_metrics"]:
            writer.write_title("Evaluation Metrics:", level=3)
            evaluation_metrics_table = from_trial_get("evaluation_metrics", {})
            writer.write_nested_table(evaluation_metrics_table)

    # Save the report
    writer.save_file()
