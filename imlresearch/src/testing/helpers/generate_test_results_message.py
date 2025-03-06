def generate_test_results_message(result):
    """
    Generate a test result message based on the given test result object.

    Parameters
    ----------
    result : unittest.TestResult
        The test result object.

    Returns
    -------
    str
        The generated test result message.
    """
    num_passed_tests = (
        result.testsRun
        - len(result.errors)
        - len(result.failures)
        - len(result.skipped)
    )
    runned_tests = result.testsRun - len(result.skipped)

    if num_passed_tests == runned_tests:
        message = f"All tests passed! ({num_passed_tests}/{runned_tests})"
    else:
        message = (
            f"{num_passed_tests} out of {runned_tests} tests passed.\n"
            f"Failures: {len(result.failures)}\n"
            f"Errors: {len(result.errors)}"
        )

    return message
