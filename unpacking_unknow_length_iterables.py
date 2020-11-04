records = [
	('foo',1,2),
	('bar','hello'),
	('foo',3,4)
	]

def do_foo(x,y):
	print('foo',x,y)

def do_bar(s):
	print('bar',s)
	
for tag, *arg in records:
	if tag=='foo':
		do_foo(*arg)
	elif tag == 'bar':
		do_bar(*arg)