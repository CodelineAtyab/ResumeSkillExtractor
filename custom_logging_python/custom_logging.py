import logging
import os

from logging.config import fileConfig

class CustomLogging:
    """
    A custom logging class that provides methods to log messages with different levels of severity.
    """
    def __init__(self, config_file='logging_config.ini'):
        """
        Initializes a logger object with the configuration specified in a file, and defines default messages for each log level.

        Args:
            config_file (str): The path to the logging configuration file. Default is 'logging_config.ini'.
        """
        # Check if the logs directory exists, and create it if it doesn't
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Load the logging configuration from the file
        fileConfig(config_file)

        # Get a logger object with the root logger's configuration
        self.logger = logging.getLogger()

        # Define default messages for each log level
        self.default_info_message = 'This is an info-level log message'
        self.default_warning_message = 'This is a warning-level log message'
        self.default_error_message = 'This is an error-level log message'

    def info(self, message=None):
        """
        Logs a message with info severity level.

        Args:
            message (str): The message to log. If None, uses the default info message.

        Returns:
            None
        """
        if message is None:
            message = self.default_info_message
        self.logger.info(message)

    def warning(self, message=None):
        """
        Logs a message with warning severity level.

        Args:
            message (str): The message to log. If None, uses the default warning message.

        Returns:
            None
        """
        if message is None:
            message = self.default_warning_message
        self.logger.warning(message)

    def error(self, message=None):
        """
        Logs a message with error severity level.

        Args:
            message (str): The message to log. If None, uses the default error message.

        Returns:
            None
        """
        if message is None:
            message = self.default_error_message
        self.logger.error(message)

# Create an instance of the CustomLogging class and assign it to the app_logger variable.
# This allows the application to use a custom logging interface with methods to log messages
# at different levels of severity. By default, the CustomLogging class uses the logging_config.ini
# file to configure the logging settings, and creates log files in the 'logs' directory if it
# doesn't already exist. Once you have created an instance of the CustomLogging class, you can use
# its info(), warning(), and error() methods to log messages in your application with the
# appropriate level of severity.
app_logger = CustomLogging()

