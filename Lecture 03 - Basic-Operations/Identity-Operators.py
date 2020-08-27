#Identity Operators

x, y = 10, 10
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = 21, 10
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = 'abc', 'abc'
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = 'abc', 'bca'
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = (1, 2, 3), (1, 2, 3)
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = (1, 2, 3), (2, 3, 1)
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = [1, 2, 3], [1, 2, 3]
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = [1, 2, 3], [2, 3, 1]
print(x, id(x))
print(y, id(y))
print(x is y)

x = {'a':1, 'b':2, 'c':3}
y = {'a':1, 'b':2, 'c':3}
print(x, id(x))
print(y, id(y))
print(x is y)

x = {'a':1, 'b':2, 'c':3}
y = {'a':2, 'b':3, 'c':1}
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = {1, 2, 3}, {1, 2, 3}
print(x, id(x))
print(y, id(y))
print(x is y)

x, y = {1, 2, 3}, {2, 3, 1}
print(x, id(x))
print(y, id(y))
print(x is y)
