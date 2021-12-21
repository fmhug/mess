# coding: utf-8

from functools import wraps

# Keep this just before your first function
_imports = {key: value for key, value in globals().items() if not key.startswith('_')}


# Retry decorator implemented with function
def retry(times=3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == (times - 1):
                        raise e
        return inner
    return wrapper


# Retry decorator implemented with class
class Retry:
    def __init__(self, times=3):
        self.times = times

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(self.times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == (self.times - 1):
                        raise e
        return inner


# Singleton decorator implemented with function
def singleton(cls):
    classes = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls in classes:
            return classes[cls]
        classes[cls] = cls(*args, **kwargs)
        return classes[cls]
    return wrapper


# Modify the singleton of the realization of the __new__ method
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# Lazy loading
class Lazy:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


# Keep this at the end of this script
__all__ = [k for k, v in globals().items() if not k.startswith('_') and k not in _imports and k != '_imports']
