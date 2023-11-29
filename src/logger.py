import os
import sys

from loguru import logger

from src.config import config, LogConfig


def setup_logger(logger_config: LogConfig = config.logger):
    """
    :param logger_config: config class for logger setup, by default config.logger
    """

    is_debug = logger_config.level == "DEBUG"

    # logfile path
    log_path = os.sep + os.path.join(*__file__.split(os.sep)[:-2]) + f'{os.sep}{config.logger.file_path}'

    # Remove existing loggers to prevent log duplication
    logger.remove()

    # File handler
    logger.add(
        log_path,
        format=logger_config.format,
        rotation=logger_config.rotation,
        enqueue=logger_config.enqueue,
        serialize=logger_config.serialize,
        level=logger_config.level,
        backtrace=is_debug,
        diagnose=is_debug,
    )

    # Stdout handler
    logger.add(
        sys.stderr,
        format=logger_config.format,
        enqueue=logger_config.enqueue,
        level=logger_config.level,
        backtrace=is_debug,
        diagnose=is_debug,
        colorize=True,
    )
