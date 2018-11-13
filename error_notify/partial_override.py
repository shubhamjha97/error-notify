import traceback
import os, sys

def placeholder_notific_fn(exc_type, exc_value, exc_traceback):
	print("PLACEHOLDER STARTS")
	listing = traceback.format_exception(exc_type, exc_value, exc_traceback)
	del listing[1]
	print("".join(listing))
	print("PLACEHOLDER ENDS")

def partial_override(func):
	def wrapper(*args, **kw):
		try:
			func(*args, **kw)
		except:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			placeholder_notific_fn(exc_type, exc_value, exc_traceback)
	return wrapper