#Python Input

x = input('Enter a string: ')
print(x)
print(type(x))

x = int(input('Enter an int number: '))
print(x)
print(type(x))

x = float(input('Enter a float number: '))
print(x)
print(type(x))

x, y, z = input('Enter 3 values: ').split()
print(x, y, z)
print(type(x), type(y), type(z))
x, y, z = int(x), str(y), float(z)
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = map(str, input('Enter 3 strings: ').split())
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = map(int, input('Enter 3 int numbers: ').split())
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = map(float, input('Enter 3 float numbers: ').split())
print(x, y, z)
print(type(x), type(y), type(z))
