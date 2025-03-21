from imlresearch.src.plotting.tests.binary_plotter_test import (
    TestBinaryPlotter,
)
from imlresearch.src.plotting.tests.multi_class_plotter_test import (
    TestMultiClassPlotter,
)
from imlresearch.src.plotting.tests.plot_confusion_matrix_test import (
    TestPlotConfusionMatrix,
)
from imlresearch.src.plotting.tests.plot_decorator_test import (
    TestPlotDecorator,
)
from imlresearch.src.plotting.tests.plot_images_test import TestPlotImages
from imlresearch.src.plotting.tests.plot_model_summary_test import (
    TestPlotModelSummary,
)
from imlresearch.src.plotting.tests.plot_pr_curve_test import TestPlotPRCurve
import imlresearch.src.plotting.tests.plot_results_test as plot_results_test
from imlresearch.src.plotting.tests.plot_roc_curve_test import TestPlotRocCurve
from imlresearch.src.plotting.tests.plot_text_test import TestPlotText
from imlresearch.src.plotting.tests.plot_training_histories_test import (
    TestPlotTrainingHistories,
)
from imlresearch.src.plotting.tests.plot_training_history_test import (
    TestPlotTrainingHistory,
)
from imlresearch.src.plotting.tests.plotter_test import TestPlotter
from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase


class PlottingTestRunner(TestRunnerBase):
    """
    Test Runner for the Plotting Module.
    """

    def load_tests(self):
        """
        Loads all test cases and modules for the Plotting module.
        """
        self.load_test_case(TestPlotConfusionMatrix)
        self.load_test_case(TestPlotText)
        self.load_test_case(TestPlotImages)
        self.load_test_case(TestPlotter)
        self.load_test_case(TestBinaryPlotter)
        self.load_test_case(TestMultiClassPlotter)
        self.load_test_case(TestPlotTrainingHistory)
        self.load_test_case(TestPlotTrainingHistories)
        self.load_test_case(TestPlotDecorator)
        self.load_test_case(TestPlotModelSummary)
        self.load_test_case(TestPlotRocCurve)
        self.load_test_case(TestPlotPRCurve)
        self.load_test_module(plot_results_test)


def run_tests():
    """
    Run the tests for the Plotting module.

    Returns
    -------
    unittest.TestResult
        The test result object.
    """
    runner = PlottingTestRunner()
    return runner.run_tests()


if __name__ == "__main__":
    run_tests()
