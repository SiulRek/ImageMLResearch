from src.plotting.tests.binary_plotter_test import TestBinaryPlotter
from src.plotting.tests.multi_class_plotter_test import TestMultiClassPlotter
from src.plotting.tests.plot_confusion_matrix_test import TestPlotConfusionMatrix
from src.plotting.tests.plot_decorator_test import TestPlotDecorator
from src.plotting.tests.plot_images_test import TestPlotImages
from src.plotting.tests.plot_model_summary_test import TestPlotModelSummary
import src.plotting.tests.plot_results_test as plot_results_test
from src.plotting.tests.plot_text_test import TestPlotText
from src.plotting.tests.plot_training_history_test import TestPlotTrainingHistory
from src.plotting.tests.plotter_test import TestPlotter
from src.testing.helpers.test_runner_base import TestRunnerBase


class PlottingTestRunner(TestRunnerBase):
    """ Test Runner for the Plotting Module. """

    def load_tests(self):
        self.load_test_case(TestPlotConfusionMatrix)
        self.load_test_case(TestPlotText)
        self.load_test_case(TestPlotImages)
        self.load_test_case(TestPlotter)
        self.load_test_case(TestBinaryPlotter)
        self.load_test_case(TestMultiClassPlotter)
        self.load_test_case(TestPlotTrainingHistory)
        self.load_test_case(TestPlotDecorator)
        self.load_test_case(TestPlotModelSummary)
        self.load_test_module(plot_results_test)


if __name__ == "__main__":
    runner = PlottingTestRunner()
    runner.run_tests()
