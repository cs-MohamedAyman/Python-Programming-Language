#Map and Filter Function

def filter_fun(x):
	return x % 2 == 0

y = [1, 4, 6, 5, 8]
r = list(filter(filter_fun, y))
print(r)

def map_fun(x):
	return x * 2

y = [1, 5, 4, 6, 8]
r = list(map(map_fun, y))
print(r)


y = [1, 4, 6, 5, 8]
r = list(filter(lambda x: (x%2 == 0), y))
print(r)

y = [1, 5, 4, 6, 8]
r = list(map(lambda x: x * 2, y))
print(r)
