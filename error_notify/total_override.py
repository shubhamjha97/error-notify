import os, sys

def placeholder_notific_fn():
	print("PLACEHOLDER CALLED")

def Notify(type_, value, traceback):
	placeholder_notific_fn() # call notification function
	tempExceptHook(type_, value, traceback)

tempExceptHook = sys.excepthook
sys.excepthook = Notify