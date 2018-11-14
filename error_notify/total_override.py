import os, sys

from error_notify.notification import notification_handler

# def notification(type_, value, traceback):
# 	notify = Notify(type_, value, traceback)
# 	notify.notify_system()

def CustomExceptHook(type_, value, traceback):
	notification_handler(type_, value, traceback) # call notification function

tempExceptHook = sys.excepthook
sys.excepthook = CustomExceptHook