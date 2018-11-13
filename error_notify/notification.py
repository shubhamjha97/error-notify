import os

class Notify(object):
	"""docstring for Notify"""
	def __init__(self, type_, value, traceback):
		super(Notify, self).__init__()
		self.traceback = traceback
		self.type_ = type_
		self.value = value


	def notify_system(self):
		os.system("notify-send '{}' '{} at line number {}'".format(self.type_, self.value, self.traceback.tb_lineno))