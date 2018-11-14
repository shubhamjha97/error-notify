import os, sys
from error_notify.decorators import partial_override, override_class

def test_total_override():
	temp = "total"/0

# partial_override

@partial_override
def test_partial_override():
	temp = "partial"/0

def test_class_override():

	@override_class()
	class Demo:
		def func_1(self):
			temp = "class"/0

		def func_2(self):
			temp = "class"/0

		def func_3(self):
			temp = "class"/0

		def run(self):
			self.func_3()

	Demo().run()


if __name__ == '__main__':
	
	if sys.argv[1] == "partial":
		test_partial_override()
	elif sys.argv[1] == "total":
		from error_notify import total_override
		test_total_override()
	elif sys.argv[1] == "class":
		test_class_override()