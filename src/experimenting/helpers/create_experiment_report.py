import json
import os


def create_experiment_report(experiment_data):
    """
    Creates the experiment report by saving the experiment data to a JSON file.

    Args:
        - experiment_data (dict): The experiment data to save.
    """
    experiment_directory = experiment_data["directory"]
    report_file = os.path.join(experiment_directory, "experiment_report.json")
    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(experiment_data, file, indent=4)
