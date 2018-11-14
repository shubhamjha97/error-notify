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


def override_class(decorator=partial_override, exclude=[]):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and attr not in exclude:
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate