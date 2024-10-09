from copy import deepcopy
from typing import Dict

from numpy import log2
import optuna
from optuna.distributions import (
    CategoricalDistribution,
    FloatDistribution,
    IntDistribution,
)

from src.experimenting.helpers.last_score_singleton import LastScoreSingleton


def _assert_hparam_configs(
    configs, hparam_name, hp_type, required_keys, optional_keys=[]
):
    for key in required_keys:
        msg = f"Required key '{key}' not found in config "
        msg += f"for {hp_type} parameter '{hparam_name}'"
        assert key in configs, msg
    for key in configs.keys():
        msg = f"Invalid key '{key}' in config for {hp_type}"
        msg += f" parameter '{hparam_name}'"
        assert key in required_keys + optional_keys, msg


def _get_suggest_float_method(name, config):
    def wrapper(trial):
        return trial.suggest_float(name, **config)

    return wrapper


def _to_nearest_power_of_two(value):
    return 2 ** round(log2(value))


def _get_suggest_int_method(name, config):
    # nearest_power2 is consumed inside the wrapper, so we can safely remove it
    # from the config.
    to_power_2 = config.pop("nearest_power2", False)

    def wrapper(trial):
        suggested = trial.suggest_int(name, **config)
        if to_power_2:
            suggested = _to_nearest_power_of_two(suggested)
            # Overwrite the true suggested value with the nearest power of 2.
            trial.params[name] = suggested
        return suggested

    return wrapper


def _get_suggest_categorical_method(name, config):
    def wrapper(trial):
        return trial.suggest_categorical(name, **config)

    return wrapper


class HParamsSuggester:
    """ A class to suggest hyperparameters using Optuna. """

    def __init__(self, hparams_configs: Dict[str, dict]):
        """
        Initializes the HParamsSuggester with the given hyperparameter
        configurations.

        Args:
            - hparams_configs (Dict[str, dict]): The hyperparameter
                configurations.
        """
        # TODO: Think of a way to allow sampler and pruner to be defined by the
        # user with hparams_configs. Pass them to create_study.
        self.study = optuna.create_study(direction="minimize")
        self.trials = []
        self.hp_names = hparams_configs.keys()
        self.hparams_distributions = {}
        self.suggest_methods = {}
        self._compile_hparams_configs(hparams_configs)
        self.current_trial = None

    def _compile_hparams_configs(self, hparams_configs):
        """
        Compiles the hyperparameter configurations into distributions and
        suggest methods.

        Args:
            - hparams_configs (Dict[str, dict]): The hyperparameter
                configurations.
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
                self.suggest_methods[name] = _get_suggest_float_method(name, configs)
            elif hp_type == "int":
                _assert_hparam_configs(
                    configs,
                    hparam_name=name,
                    hp_type=hp_type,
                    required_keys=["low", "high"],
                    optional_keys=["step", "log", "nearest_power2"],
                )
                self.suggest_methods[name] = _get_suggest_int_method(name, configs)
                self.hparams_distributions[name] = IntDistribution(**configs)
            elif hp_type == "categorical":
                _assert_hparam_configs(
                    configs,
                    hparam_name=name,
                    hp_type=hp_type,
                    required_keys=["choices"],
                )
                self.hparams_distributions[name] = CategoricalDistribution(**configs)
                self.suggest_methods[name] = _get_suggest_categorical_method(
                    name, configs
                )
            else:
                msg += f"Invalid hyperparameter type: {hp_type} "
                raise ValueError(msg)

    def suggest_next(self):
        """
        Returns the next set of hyperparameters to try.

        Returns:
            - dict: The next set of hyperparameters.
        """
        if self.current_trial is not None:
            # If set_last_score() has not been called after the last call to
            # next(), try to get the last score from the singleton.
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

        self.current_trial = trial

        return next_hparams

    def set_last_score(self, score: float):
        """
        Sets the score for the last suggested hyperparameters.

        Args:
            - score (float): The score for the last suggested
                hyperparameters.
        """
        if self.current_trial is None:
            msg += "No pending trial to set score for. Consider calling next() "
            msg = "first."
            raise ValueError(msg)

        self.study.tell(self.current_trial, score)
        self.current_trial = None
