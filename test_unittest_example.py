import unittest

def fun(x):
	return pow(x,2)/ x
	
class MyTest(unittest.TestCase):
	def test_positive_input(self):
		self.assertEqual(fun(3),3)
		
	def test_negative_inputs(self):
		self.assertEqual(fun(-4),-4)
		
	def test_divide_by_zero_error(self):
		self.assertRaises(ZeroDivisionError, fun, 0)

	def test_input_non_numeric(self):
		self.assertRaises(TypeError, fun, "test phrase")
		
		
if __name__ == '__main__':
	print(f"Function returns {fun(3)} with input 3.")