from src.research.tests.data_retriever_test import TestDataRetriever
from src.research.tests.module_level_workflow.binary_workflow_test import (
    TestBinaryModuleLevelWorkflow,
)
from src.research.tests.module_level_workflow.multi_class_workflow_test import (
    TestMultiClassModuleLevelWorkflow,
)
from src.research.tests.researcher_level_workflow.binary_workflow_test import (
    TestBinaryResearcherLevelWorkflow,
)
from src.research.tests.researcher_level_workflow.multi_class_workflow_test import (
    TestMultiClassResearcherLevelWorkflow,
)
from src.testing.helpers.test_runner_base import TestRunnerBase


class ResearchTestRunner(TestRunnerBase):
    """ Test Runner for the Research Module. """

    def load_tests(self):
        self.load_test_case(TestBinaryModuleLevelWorkflow)
        self.load_test_case(TestBinaryResearcherLevelWorkflow)
        self.load_test_case(TestMultiClassModuleLevelWorkflow)
        self.load_test_case(TestMultiClassResearcherLevelWorkflow)
        self.load_test_case(TestDataRetriever)


if __name__ == "__main__":
    runner = ResearchTestRunner()
    runner.run_tests()
