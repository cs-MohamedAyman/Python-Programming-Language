#Return Statement

def add_100(x, y):
	x += 100
	y += '100'

a, b = 6, '8'
a, b = add_100(a, b)
print(a)
print(b)
