import logging
import os


class Logger:
    def __init__(self, log_file, log_level=logging.INFO, mode="w"):
        """
        Initialize the Logger class with basic configuration.

        Parameters
        ----------
        log_file : str
            Path to the log file.
        log_level : logging.level, optional
            Level of logging, by default logging.INFO.
        mode : str, optional
            The mode to open the log file, by default "w".
        """
        self.log_file = log_file
        self.log_level = log_level
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        self.setup_logger(mode)

    def setup_logger(self, mode):
        """
        Set up the logger with a file handler and a standard logging format.

        Parameters
        ----------
        mode : str
            The mode to open the log file.

        Notes
        -----
        This method configures the logger to write to the log file specified
        in the `log_file` attribute.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)
        handler = logging.FileHandler(self.log_file, mode=mode)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def close_logger(self):
        """Close and remove all handlers attached to the logger."""
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)

    def info(self, message):
        """
        Write an info message to the log.

        Parameters
        ----------
        message : str
            The message to log at INFO level.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Write a warning message to the log.

        Parameters
        ----------
        message : str
            The message to log at WARNING level.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Write an error message to the log.

        Parameters
        ----------
        message : str
            The message to log at ERROR level.
        """
        self.logger.error(message)

    def log_title(self, title):
        """
        Log a title string with a specific format.

        Parameters
        ----------
        title : str
            The title string to log.

        Notes
        -----
        This method formats the given title string with a pattern of dashes
        before and after, then logs it at the INFO level.
        """
        formatted_title = (
            "-" * 14 + f" {title} " + "-" * (60 - len(title) - 14)
        )
        self.logger.info(formatted_title)


if __name__ == "__main__":
    # Example usage:
    log_file = os.path.join(os.path.curdir, "logfile.log")
    logger = Logger(log_file)
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    print(f"Log file saved to {log_file}")
