import os
import sys


def check_experiment_dir(experiment_metadata):
    experiment_dir = experiment_metadata["directory"]
    execution_dir = os.path.dirname(sys.argv[0])  # Directory of the executed file

    experiment_dir = os.path.abspath(experiment_dir)
    execution_dir = os.path.abspath(execution_dir)
    experiment_dir = os.path.normpath(experiment_dir)
    execution_dir = os.path.normpath(execution_dir)

    if experiment_dir != execution_dir:
        msg = f"Experiment directory {experiment_dir} is not the same as the "
        msg += f"directory of the executed file {execution_dir}."
        raise ValueError(msg)
