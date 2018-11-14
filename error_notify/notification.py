import os
import traceback


class Notify(object):
	"""docstring for Notify"""
	def __init__(self, type_, value, traceback):
		super(Notify, self).__init__()
		self.traceback = traceback
		self.type_ = type_
		self.value = value

	def notify(self):
		self.echo_to_console()
		self.notify_system()

	def echo_to_console(self):
		listing = traceback.format_exception(self.type_, self.value, self.traceback)
		del listing[1]
		print("".join(listing))

	def notify_system(self):
		os.system("notify-send '{}' '{} at line number {}'".format(self.type_, self.value, self.traceback.tb_lineno))


def notification_handler(exc_type, exc_value, exc_traceback):
	notify = Notify(exc_type, exc_value, exc_traceback)
	notify.notify()