import os, sys

from error_notify.notification import Notify

def notification(type_, value, traceback):
	notify = Notify(type_, value, traceback)
	notify.notify_system()

def CustomExceptHook(type_, value, traceback):
	notification(type_, value, traceback) # call notification function
	tempExceptHook(type_, value, traceback)

tempExceptHook = sys.excepthook
sys.excepthook = CustomExceptHook