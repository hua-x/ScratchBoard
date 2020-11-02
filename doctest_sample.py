def pow2(x):

	""" Return square of the input x.
	
	>>> pow2(2)
	4
	>>> pow2(-3)
	9
	"""
	
	return pow(x,2)
	
def pow2_incorrect(x):
	""" Negative test case when the function does not work as intended
	
	>>> pow2_incorrect(2)
	4
	>>> pow2_incorrect(-5)
	15
	
	"""
	return pow(x,2)
	
	
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()