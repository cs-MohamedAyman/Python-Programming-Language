#Data Type Conversion

print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))

x, y, z = '11000', '24', 24.0
print(int(x, 2))
print(int(x, 8))
print(int(x, 10))
print(int(x, 16))
print(int(y, 10))
print(float(x))
print(float(y))
print(float(z))
print(str(x))
print(str(y))
print(str(z))

x = [7, 'abc', -4.3, 7]
y = (7, 'abc', -4.3, 7)
z = {7, 'abc', -4.3, 7}
print(list(x))
print(list(y))
print(list(z))
print(tuple(x))
print(tuple(y))
print(tuple(z))
print(set(x))
print(set(y))
print(set(z))

x, y, z = 'a', 97, 24
print(ord(x))
print(chr(y))
print(hex(z))
print(oct(z))
print(bin(z))

x = 'hello python'
print(list(x))
print(tuple(x))
print(set(x))

print(bool(5))
print(bool(-7))
print(bool(5.1))
print(bool(-7.1))
print(bool(0))
print(bool(None))
print(bool('abc'))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool(dict()))

x = 5
print(type(x))
x = 7.3
print(type(x))
x = 'python'
print(type(x))
x = [2, 3.2, 'c++']
print(type(x))
x = (2, 3.2, 'c++')
print(type(x))
x = {'math': 92, 'programming': 96}
print(type(x))
x = {3.14, 8, 'java'}
print(type(x))
x = True
print(type(x))
