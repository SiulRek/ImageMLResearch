from copy import deepcopy
import os
import warnings

from numpy import log2
import optuna
from optuna.distributions import (
    CategoricalDistribution,
    FloatDistribution,
    IntDistribution,
)

from imlresearch.src.experimenting.helpers.last_score_singleton import (
    LastScoreSingleton,
)

DEFAULT_STUDY_NAME = "hparams_suggester_study"


def _assert_hparam_configs(
    configs, hparam_name, hp_type, required_keys, optional_keys=[]
):
    """
    Validates the hyperparameter configuration.

    Parameters
    ----------
    configs : dict
        The configuration dictionary for the hyperparameter.
    hparam_name : str
        The name of the hyperparameter.
    hp_type : str
        The type of the hyperparameter (float, int, categorical).
    required_keys : list
        The required keys that must be present in the configuration.
    optional_keys : list, optional
        The optional keys that can be present in the configuration.
    """
    for key in required_keys:
        msg = f"Required key '{key}' not found in config "
        msg += f"for {hp_type} parameter '{hparam_name}'"
        assert key in configs, msg
    for key in configs.keys():
        msg = f"Invalid key '{key}' in config for {hp_type}"
        msg += f" parameter '{hparam_name}'"
        assert key in required_keys + optional_keys, msg


def _get_suggest_float_method(name, config):
    """
    Returns a wrapper function to suggest a float hyperparameter.

    Parameters
    ----------
    name : str
        The name of the hyperparameter.
    config : dict
        The configuration dictionary for the hyperparameter.

    Returns
    -------
    function
        A wrapper function that suggests a float hyperparameter.
    """
    def wrapper(trial):
        return trial.suggest_float(name, **config)

    return wrapper


def _to_nearest_power_of_two(value):
    """
    Rounds a given value to the nearest power of two.

    Parameters
    ----------
    value : float
        The value to round.

    Returns
    -------
    int
        The nearest power of two.
    """
    return 2 ** round(log2(value))


def _get_suggest_int_method(name, config):
    """
    Returns a wrapper function to suggest an integer hyperparameter.

    Parameters
    ----------
    name : str
        The name of the hyperparameter.
    config : dict
        The configuration dictionary for the hyperparameter.

    Returns
    -------
    function
        A wrapper function that suggests an integer hyperparameter.
    """
    to_power_2 = config.pop("nearest_power2", False)

    def wrapper(trial):
        suggested = trial.suggest_int(name, **config)
        if to_power_2:
            suggested = _to_nearest_power_of_two(suggested)
            trial.params[name] = suggested
        return suggested

    return wrapper


def _get_suggest_categorical_method(name, config):
    """
    Returns a wrapper function to suggest a categorical hyperparameter.

    Parameters
    ----------
    name : str
        The name of the hyperparameter.
    config : dict
        The configuration dictionary for the hyperparameter.

    Returns
    -------
    function
        A wrapper function that suggests a categorical hyperparameter.
    """
    def wrapper(trial):
        return trial.suggest_categorical(name, **config)

    return wrapper


class HParamsSuggester:
    """
    A class to suggest hyperparameters using Optuna.

    This class manages the process of suggesting hyperparameters
    based on predefined configurations and an Optuna study.
    """

    def __init__(
        self,
        hparams_configs,
        direction="minimize",
        storage_dir=None,
        load_if_exists=True,
        study_name=DEFAULT_STUDY_NAME,
    ):
        """
        Initializes the HParamsSuggester with hyperparameter configurations.

        Parameters
        ----------
        hparams_configs : dict
            The hyperparameter configurations.
        direction : str, optional
            The optimization direction, either "minimize" or "maximize".
            Defaults to "minimize".
        storage_dir : str, optional
            The directory to save the study. Defaults to None.
        load_if_exists : bool, optional
            Whether to load an existing study if it exists. Defaults to True.
        study_name : str, optional
            The name of the study. Defaults to DEFAULT_STUDY_NAME.
        """
        study_kwargs = {"study_name": study_name, "direction": direction}
        if storage_dir is not None:
            study_kwargs["storage"] = self._process_storage_path(
                storage_dir, study_name
            )
            study_kwargs["load_if_exists"] = load_if_exists

        self.study = optuna.create_study(**study_kwargs)
        self.trials = []
        self.hp_names = hparams_configs.keys()
        self.hparams_distributions = {}  # TODO: Remove, as not used.
        self.suggest_methods = {}
        self._compile_hparams_configs(hparams_configs)
        self.pending_trial = None

    def _process_storage_path(self, storage_dir, study_name):
        """
        Processes the storage path for Optuna.

        Parameters
        ----------
        storage_dir : str
            The directory to save the study.
        study_name : str
            The name of the study.

        Returns
        -------
        str
            The formatted storage path for Optuna.
        """
        if os.path.isdir:
            os.makedirs(storage_dir, exist_ok=True)
            file_name = f"{study_name}.db"
            storage_file = os.path.join(storage_dir, file_name)
        storage_file = os.path.normpath(storage_file)
        storage_file = storage_file.replace(os.sep, "/")
        storage_file = f"sqlite:///{storage_file}"
        return storage_file

    def _compile_hparams_configs(self, hparams_configs):
        """
        Compiles hyperparameter configurations into distributions
        and suggestion methods.

        Parameters
        ----------
        hparams_configs : dict
            The hyperparameter configurations.
        """
        hparams_configs = deepcopy(hparams_configs)
        for name, configs in hparams_configs.items():
            hp_type = configs.pop("type")
            if hp_type == "float":
                _assert_hparam_configs(
                    configs,
                    hparam_name=name,
                    hp_type=hp_type,
                    required_keys=["low", "high"],
                    optional_keys=["step", "log"],
                )
                self.hparams_distributions[name] = FloatDistribution(**configs)
                self.suggest_methods[name] = (
                    _get_suggest_float_method(name, configs)
                )
            elif hp_type == "int":
                _assert_hparam_configs(
                    configs,
                    hparam_name=name,
                    hp_type=hp_type,
                    required_keys=["low", "high"],
                    optional_keys=["step", "log", "nearest_power2"],
                )
                self.suggest_methods[name] = (
                    _get_suggest_int_method(name, configs)
                )
                self.hparams_distributions[name] = IntDistribution(**configs)
            elif hp_type == "categorical":
                _assert_hparam_configs(
                    configs,
                    hparam_name=name,
                    hp_type=hp_type,
                    required_keys=["choices"],
                )
                self.hparams_distributions[name] = (
                    CategoricalDistribution(**configs)
                )
                self.suggest_methods[name] = (
                    _get_suggest_categorical_method(name, configs)
                )
            else:
                msg = f"Invalid hyperparameter type: {hp_type} "
                raise ValueError(msg)

    def suggest_next(self):
        """
        Returns the next set of hyperparameters to try.

        Returns
        -------
        dict
            The next set of suggested hyperparameters.
        """
        if self.pending_trial is not None:
            try:
                last_score = LastScoreSingleton().take()
                self.set_last_score(last_score)
            except ValueError:
                msg = "A trial is still pending. Call set_last_score() "
                msg += "before calling next() again."
                raise ValueError(msg)
        trial = self.study.ask()
        next_hparams = {}
        for name in self.hp_names:
            suggest_method = self.suggest_methods[name]
            next_hparams[name] = suggest_method(trial)

        self.pending_trial = trial

        return next_hparams

    def set_last_score(self, score: float):
        """
        Sets the score for the last suggested hyperparameters.

        Parameters
        ----------
        score : float
            The score for the last suggested hyperparameters.
            If None, the last trial will be dropped.
        """
        if self.pending_trial is None:
            msg = "No pending trial to set score for. "
            msg += "Consider calling next() first."
            raise ValueError(msg)

        if score is not None:
            self.study.tell(self.pending_trial, score)
        else:
            msg = "Dropping the last trial as the score is None."
            warnings.warn(msg)

        self.pending_trial = None
