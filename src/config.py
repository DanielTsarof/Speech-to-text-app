import os
from typing import Literal

import yaml
from pydantic import BaseModel


class SpeechToText(BaseModel):
    model: str = Literal['tiny', 'base', 'small', 'medium', 'large']


class LogConfig(BaseModel):
    """
    :param file_path: path to log file
    :param format: log format ("{time} | {level} | {message} | {extra} | {user} | {ip}")
    :param rotation: max log file size ("50 KB, "100 MB" etc.)
    :param enqueue: queue log messages (for multiprocessor and asynchronous programs)
    :param serialize: write log in JSON format
    :param level: log level
    """
    file_path: str = './logs.log'
    format: str = '{time} | {level} | {name}:{function}:{line} | {message}'
    rotation: str = '50 MB'
    enqueue: bool = False
    serialize: bool = False
    level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "TRACE"]


class Config(BaseModel):
    speech2text: SpeechToText
    logger: LogConfig


config_path = os.sep + os.path.join(*__file__.split(os.sep)[:-2]) + f'{os.sep}config.yaml'
config = Config(**(yaml.safe_load(open(config_path) or {})))
