import traceback
import os, sys

from error_notify.notification import notification_handler

def partial_override(func):
    def wrapper(*args, **kw):
        try:
            func(*args, **kw)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            notification_handler(exc_type, exc_value, exc_traceback)
    return wrapper


def override_class(decorator=partial_override, exclude=[], include=[]):
    if exclude and include:
        raise Exception("either `exclude` or `include` is to be used")
    def decorate(cls):
        attrs = cls.__dict__
        if include:
            attrs = include
        for attr in attrs:
            if callable(getattr(cls, attr)) and attr not in exclude:
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate