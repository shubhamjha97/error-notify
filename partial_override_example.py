from error_notify.partial_override import partial_override

@partial_override
def FunctionWithError():
	temp = 1/0

if __name__=='__main__':
	FunctionWithError()