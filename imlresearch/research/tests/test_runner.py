from imlresearch.research.tests.data_retriever_test import TestDataRetriever
from imlresearch.research.tests.module_level_workflow.binary_workflow_test import (
    TestBinaryModuleLevelWorkflow,
)
from imlresearch.research.tests.module_level_workflow.multi_class_workflow_test import (
    TestMultiClassModuleLevelWorkflow,
)
from imlresearch.research.tests.researcher_level_workflow.binary_workflow_test import (
    TestBinaryResearcherLevelWorkflow,
)
from imlresearch.research.tests.researcher_level_workflow.multi_class_workflow_test import (
    TestMultiClassResearcherLevelWorkflow,
)
from imlresearch.testing.bases.test_runner_base import TestRunnerBase


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
