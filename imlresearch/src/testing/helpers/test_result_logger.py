import logging


class TestResultLogger:
    """
    A Singleton logger for logging unittest results.

    This class generates three types of logs:
        - Detailed Log: Includes the status of each test.
        - Simplified Log: Only includes whether the test passed or failed.
        - Error Log: Only includes errors and failures with messages.
    """

    _instance = None
    _setup_file_handlers = True
    _failures_count = 0
    _errors_count = 0

    def __new__(cls, *args, **kwargs):
        """Ensures a single instance of the TestResultLogger class."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            cls._setup_file_handlers = False
        return cls._instance

    def __init__(self, log_file="./test_results.log"):
        """
        Initialize the TestResultLogger.

        Args:
            - log_file (str): Path to the detailed log file.
        """
        self.log_file = log_file
        self.log_file_simple = log_file.replace(".log", "_simple.log")
        self.log_file_errors = log_file.replace(".log", "_errors.log")
        self.setup_logger()
        self.title = ""  # Will be set through log_title method.
        self.error_logger_logged_title = False  # Logs title only if an error occurs.

    def _setup_file_handler(self, logger, file_path, level=logging.INFO):
        """
        Setup a file handler for the logger.

        Args:
            - logger (logging.Logger): Logger object to configure.
            - file_path (str): File path for logging.
            - level (int): Logging level (default: logging.INFO).
        """
        logger.setLevel(level)
        file_handler = logging.FileHandler(file_path, mode="w")
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(file_handler)

    def setup_logger(self):
        """Set up the loggers for detailed, simplified, and error logs."""
        self.logger = logging.getLogger("TestResultLogger")
        self.simple_logger = logging.getLogger("TestResultLoggerSimple")
        self.error_logger = logging.getLogger("TestResultLoggerErrors")

        if self._setup_file_handlers:
            self._setup_file_handler(self.logger, self.log_file)
            self._setup_file_handler(self.simple_logger, self.log_file_simple)
            self._setup_file_handler(self.error_logger, self.log_file_errors)

    def _format_title(self, title):
        """Format a title for logging."""
        return "-" * 14 + f" {title} " + "-" * (60 - len(title) - 14)

    def log_title(self, title):
        """
        Logs a formatted title.

        Args:
            - title (str): Title to be logged.
        """
        formatted_title = self._format_title(title)
        self.title = formatted_title
        self.logger.info(formatted_title)
        self.simple_logger.info(formatted_title)

    def _log_outcome(self, outcome_type, test_method_name, message=""):
        """
        Logs test outcomes, including errors and failures.

        Args:
            - outcome_type (str): 'passed', 'failure', or 'raised exc'.
            - test_method_name (str): Name of the test method.
            - message (str, optional): Error or failure message.
        """
        log_message = f"Test {outcome_type}: {test_method_name}"
        if outcome_type == "passed":
            self.simple_logger.info(log_message)
            self.logger.info(log_message)
        elif outcome_type in ["failure", "raised exc"]:
            self.simple_logger.error(log_message)
            log_message += f"\nMessage: {message}"
            self.logger.error(log_message)
            if not self.error_logger_logged_title and self.title:
                self.error_logger.info(f"{'-' * 14}{self.title}{'-' * 45}")
                self.error_logger_logged_title = True
            self.error_logger.error(log_message)
        else:
            raise ValueError(f"Outcome Type '{outcome_type}' is not recognized.")

    def log_test_outcome(self, result, test_method_name):
        """
        Log the outcome of a single test case.

        Args:
            - result (unittest.TestResult): The result object.
            - test_method_name (str): The name of the test method.
        """
        try:
            success = True

            if self._errors_count + 1 == len(result.errors):
                success = False
                error = result.errors[self._errors_count]
                self._log_outcome("raised exc", test_method_name, error[1])
                self._errors_count += 1

            if self._failures_count + 1 == len(result.failures):
                success = False
                failure = result.failures[self._failures_count]
                self._log_outcome("failure", test_method_name, failure[1])
                self._failures_count += 1

            if success:
                self._log_outcome("passed", test_method_name)
        except Exception as exc:
            print(f"Logging error: {exc}")  # Logger should not interrupt testing
