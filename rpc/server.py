# -*- coding: utf-8 -*-

import zerorpc
from functools import wraps
from typing import Callable


def singleton(cls):
    _instances = {}

    def _single(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return _single


@singleton
class ServerHub:

    def __init__(self):
        self.functions = {}

    def register(self, func: Callable):
        name = func.__name__
        if name in self.functions:
            raise AttributeError('Duplicate method trying to register')
        self.functions[name] = func
        setattr(self, name, func)


hub = ServerHub()


def register(func):
    print('call register')
    hub.register(func)

    @wraps
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


@register
def add(x, y):
    print('add called, x is %s, y is %s' % (x, y))
    return x + y


@register
def mp(x, y):
    print('mp called, x is %s, y is %s' % (x, y))
    return x * y


server = zerorpc.Server(hub)
server.bind('tcp://0.0.0.0:4242')
server.run()
