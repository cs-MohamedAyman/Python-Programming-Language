#Python Sets

x = {5, 2, 1, 4, 3}
print(x)
print(len(x))

x = {2, 2, 1, 1, 3}
print(x)
print(len(x))

x = {'ab', 'cd', 'ef'}
print(x)
print(len(x))

x = {'ab', 'ef', 'cd', 'ab', 'ef'}
print(x)
print(len(x))

x = {0, 2, 'ab', 4, 6, 'cd', 8}
y = {1, 2, 'ef', 3, 4, 'cd', 5}

print(x | y)
print(x & y)
print(x - y)
print(y - x)
print(x ^ y)
