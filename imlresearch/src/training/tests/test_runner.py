from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase
from imlresearch.src.training.tests.evaluate_test import TestEvaluate
from imlresearch.src.training.tests.trainer_test import TestTrainer


class TrainingTestRunner(TestRunnerBase):
    """ Test Runner for the Training Module. """

    def load_tests(self):
        self.load_test_case(TestEvaluate)
        self.load_test_case(TestTrainer)


if __name__ == "__main__":
    runner = TrainingTestRunner()
    runner.run_tests()
