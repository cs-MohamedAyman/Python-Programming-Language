

s = set()
print(s)
print(len(s))
print(type(s))

s = {1, 4, 3, 5}
print(s)
print(len(s))
print(type(s))

s = {'ab', 'cd', 'ef'}
print(s)
print(len(s))
print(type(s))

x = {2, 5, 'ab', 7, 9, 'cd'}
y = {3, 2, 'cd', 9, 8, 1}

print(x)
print(y)

print(x | y)
print(x & y)
print(x - y)
print(y - x)
print(x ^ y)

s = set()
for i in range(5):
    s.add(i)
print(s)

s.remove(1)
print(s)
s.discard(2)
print(s)
s.discard(7)
print(s)
s.remove(7)
print(s)

x = {2, 5, 'ab', 7, 9, 'cd'}
y = {3, 2, 'cd', 9, 8, 1}

print(x)
print(y)

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))

x = {3, 6, 5, 7}
y = x.copy()
print(id(x))
print(id(y))

print(len(x))
x.clear()
print(len(x))

x = {4, 2, -7}
y = {-7, 4}

print(x.issuperset(y))
print(y.issuperset(x))

print(x.issubset(y))
print(y.issubset(x))

print(x.isdisjoint(y))
print(y.isdisjoint(x))

x = {4, 2, -7}
y = {-1, 3}

print(x.isdisjoint(y))
print(y.isdisjoint(x))
