from collections import deque

def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	print(f"outside scope: ++{previous_lines}++")	
	for line in lines:
		if pattern in line:
			print(f"inside scope: ++{previous_lines}++")	
			yield line, previous_lines
		previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
	with open('unpacking_unknow_length_iterables.py') as f:
		for line, prevlines in search(f, 'bar', 5):
			for pline in prevlines:
				print(pline, end='*')
			print(line, end='|')
			print('-'*20)
