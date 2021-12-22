# coding: utf-8

import os
import sys
import logging
from logging import StreamHandler, Formatter, PercentStyle, DEBUG
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


colors = {
    'DEBUG': ('\033[34m', '\033[0m',),
    'INFO': ('\033[30m', '\033[0m',),
    'WARNING': ('\033[33m', '\033[0m',),
    'WARN': ('\033[33m', '\033[0m',),
    'ERROR': ('\033[31m', '\033[0m',),
    'CRITICAL': ('\033[31m', '\033[0m',),
}


class PyPercentStyle(PercentStyle):

    def __init__(self, fmt: str, stream=False):
        super().__init__(fmt)
        self.stream = stream

    def _format(self, record):
        if self.stream:
            pre, sub = colors[record.levelname]
            return pre + self._fmt % record.__dict__ + sub
        else:
            return self._fmt % record.__dict__


class PyFormatter(Formatter):

    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, stream=False):
        super(PyFormatter, self).__init__()
        # Rewrite style
        self._style = PyPercentStyle(fmt, stream)


_defaultFormatter = PyFormatter()


class PyStreamHandler(StreamHandler):
    pass


class PyTimedRotatingFileHandler(TimedRotatingFileHandler):

    def rotation_filename(self, default_name):
        name_lst = default_name.split(os.sep)
        file_lst = name_lst[-1].split('.')
        file_lst[-2], file_lst[-1] = file_lst[-1], file_lst[-2]
        name_lst[-1] = '.'.join(file_lst)
        default_name = os.sep.join(name_lst)
        if not callable(self.namer):
            result = default_name
        else:
            result = self.namer(default_name)
        return result


class Logger:

    def __init__(self, name: str = 'log', path: str = ''):
        # Log name
        self.name = name
        # Log path
        self.path = Path(path) if path else Path().joinpath('.logs')
        self.path.mkdir(exist_ok=True)
        # Log formatter
        self._formatter = "%(asctime)s %(levelname)s\t%(filename)s.%(funcName)s:%(lineno)d - %(message)s"
        # Get logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(DEBUG)
        # Add handler
        self._add_file_handler()
        self._add_stream_handler()

    # Add stream handler
    def _add_stream_handler(self):
        stream_formatter = PyFormatter(self._formatter, stream=True)
        stream_handler = PyStreamHandler(sys.stdout)
        # stream_handler.setLevel(DEBUG)
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

    # Add file handler
    def _add_file_handler(self):
        when = 'D'
        interval = 1
        backup_count = 10
        log_path = self.path.joinpath(f'{self.name}.log')
        file_formatter = PyFormatter(self._formatter, stream=False)
        file_handler = PyTimedRotatingFileHandler(
            log_path,
            when=when,
            interval=interval,
            backupCount=backup_count
        )
        # file_handler.setLevel(DEBUG)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)


logger = Logger().logger
