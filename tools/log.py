# coding: utf-8

import sys
import logging
from logging import (
    StreamHandler, Formatter, PercentStyle,
    DEBUG, INFO, WARN, WARNING, ERROR, CRITICAL
)
from logging.handlers import TimedRotatingFileHandler


colors = {
    'DEBUG':    ('\033[34m', '\033[0m',),
    'INFO':     ('\033[0m',  '\033[0m',),
    'WARNING':  ('\033[33m', '\033[0m',),
    'WARN':     ('\033[33m', '\033[0m',),
    'ERROR':    ('\033[31m', '\033[0m',),
    'CRITICAL': ('\033[31m', '\033[0m',),
}


class PyPercentStyle(PercentStyle):
    def __init__(self, fmt: str, stream=False):
        super().__init__(fmt)
        self.stream = stream

    # Python 3.9
    def _format(self, record):
        if self.stream:
            pre, sub = colors[record.levelname]
            return pre + self._fmt % record.__dict__ + sub
        else:
            return self._fmt % record.__dict__

    # Python 3.7
    def format(self, record):
        return self._format(record)


class PyFormatter(Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', stream=False):
        super(PyFormatter, self).__init__(fmt, datefmt, style)
        self._style = PyPercentStyle(fmt, stream)  # Rewrite style


class Py39Formatter(Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, stream=False):
        super(Py39Formatter, self).__init__(fmt, datefmt, style, validate)
        self._style = PyPercentStyle(fmt, stream)  # Rewrite style


# 需要注意不同Python版本logging的差异
if (sys.version_info.major == 3) and (sys.version_info.minor >= 9):
    PyFormatter = Py39Formatter


class PyTimedRotatingFileHandler(TimedRotatingFileHandler):
    pass  # 可以重写相关的日志滚动


logger = logging.getLogger('log')
logger.setLevel(DEBUG)

form = "%(asctime)s %(levelname)s\t%(filename)s.%(funcName)s:%(lineno)d\t- %(message)s"

stream_formatter = PyFormatter(form, stream=True)
stream_handler = StreamHandler(sys.stdout)
stream_handler.setLevel(DEBUG)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

file_formatter = PyFormatter(form, stream=False)
file_handler = PyTimedRotatingFileHandler(
    'log.log',
    when='D',
    interval=1,
    backupCount=10,
    encoding='utf-8'
)
file_handler.setLevel(DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

msg = 'Let\'s see what happened.'
logger.debug(msg)
logger.info(msg)
logger.warning(msg)
logger.error(msg)
logger.critical(msg)
