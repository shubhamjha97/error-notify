import os, sys

from error_notify.notification import notification_handler

def CustomExceptHook(type_, value, traceback):
	notification_handler(type_, value, traceback) # call notification function

tempExceptHook = sys.excepthook
sys.excepthook = CustomExceptHook