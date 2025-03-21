from imlresearch.src.research.tests.data_retriever_test import (
    TestDataRetriever,
)
from imlresearch.src.research.tests.module_level_workflow.binary_workflow_test import (  # noqa
    TestBinaryModuleLevelWorkflow,
)
from imlresearch.src.research.tests.module_level_workflow.multi_class_workflow_test import (  # noqa
    TestMultiClassModuleLevelWorkflow,
)
from imlresearch.src.research.tests.researcher_level_workflow.binary_workflow_test import (  # noqa
    TestBinaryResearcherLevelWorkflow,
)
from imlresearch.src.research.tests.researcher_level_workflow.multi_class_workflow_test import (  # noqa
    TestMultiClassResearcherLevelWorkflow,
)
from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase


class ResearchTestRunner(TestRunnerBase):
    """Test runner for the Research Module."""

    def load_tests(self):
        """
        Loads and adds research-related test cases to the test suite.
        """
        test_cases = [
            TestBinaryModuleLevelWorkflow,
            TestBinaryResearcherLevelWorkflow,
            TestMultiClassModuleLevelWorkflow,
            TestMultiClassResearcherLevelWorkflow,
            TestDataRetriever,
        ]
        for test in test_cases:
            self.load_test_case(test)


def run_tests():
    """
    Run the tests for the Research module.

    Returns
    -------
    unittest.TestResult
        The test result object.
    """
    runner = ResearchTestRunner()
    return runner.run_tests()


if __name__ == "__main__":
    run_tests()
