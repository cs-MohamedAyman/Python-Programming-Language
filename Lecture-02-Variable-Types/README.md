<img align="right" width="90" height="90" src="https://github.com/cs-MohamedAyman/Computer-Science-Textbooks/blob/master/logos/python.jpg">

# Lecture 02 - Variable Types
## 2.1- Python Variables
- ***Assigning Values to Variables***
```python
#Assigning Values to Variables

url = 'www.google.com'
print(url)

n = 5
print(n)
```
- ***Multiple Assignment***
```python
#Multiple Assignment

a, b, c = 5, 3.2, "Hello"

print(a)
print(b)
print(c)

x = y = z = "same"

print(x)
print(y)
print(z)
```
- ***Python Constant***
```python
#Python Constant

PI = 3.14
GRAVITY = 9.8

print(PI)
print(GRAVITY)
```

## 2.2- Python Numbers
- ***Python Numbers***
```python
#Python Numbers

x = 5
print(x)

x = 2.0
print(x)

x = 1+2j
print(x)
```

## 2.3- Python Strings
- ***Python Strings***
```python
#Python Strings

x = "Hello Programming"
print(x)
print(len(x))
print(x[2])
print(x[2:9])
print(x[:4])
print(x[11:])
print(x[-1])
print(x[-5:])
print(x[:-7])
print(x[-8:-2])
print(x[4:-2])
print(x[-8:14])
print(x[:])
```
- ***Python Strings***
```python
#Python Strings

x = "Hello Python"
print(x)
print(len(x))
print(x[2:5] + x[9:12])
print(x[:6] + 'World')
print(x * 2)
print(2 * x[6:])
print((x[6:8] + ' ') * 3)
```
- ***Python Strings***
```python
#Python Strings

x = "Hello Python"
print(x)
print(len(x))
print(x[::4])
print(x[::3])
print(x[::2])
print(x[::1])
print(x[::-1])
print(x[::-2])
print(x[::-3])
print(x[::-4])
```
- ***Python Strings***
```python
#Python Strings

x = "Hello Python"
print(x)
print(len(x))
print(x[3:8:4])
print(x[3:8:3])
print(x[3:8:2])
print(x[3:8:1])
print(x[7:2:-1])
print(x[7:2:-2])
print(x[7:2:-3])
print(x[7:2:-4])
```

## 2.4- Python Lists
- ***Python Lists***
```python
#Python Lists

x = ['c++', 123, 'abcd', 2.3, 'python']
print(x)
print(len(x))
print(x[3])
print(x[2:4])
print(x[:4])
print(x[2:])
print(x[-1])
print(x[-4:])
print(x[:-3])
```
- ***Python Lists***
```python
#Python Lists

x = ['python', 2000, 'c++', 3.2, 'java']
print(x)
print(len(x))
print(x[1] + x[3])
print(x[0] + x[-1])
print(x[:2] + x[3:])
print(x[2] * 3)
print(x[1] * 3)
print(x[2:4] * 2)
print((x[1:3] + x[4:5]) * 2)
```
- ***Python Lists***
```python
#Python Lists

x = ['python', 2000, 'c++', 3.2, 'java']
print(x)
print(len(x))
print(x[::4])
print(x[::3])
print(x[::2])
print(x[::1])
print(x[::-1])
print(x[::-2])
print(x[::-3])
print(x[::-4])
```
- ***Python Lists***
```python
#Python Lists

x = ['python', 2000, 'c++', 3.2, 'java']
print(x)
print(len(x))
print(x[1:4:4])
print(x[1:4:3])
print(x[1:4:2])
print(x[1:4:1])
print(x[-2:0:-4])
print(x[-2:0:-3])
print(x[-2:0:-2])
print(x[-2:0:-1])
```

## 2.5- Python Tuples
- ***Python Tuples***
```python
#Python Tuples

x = ('c++', 123, 'abcd', 2.3, 'python')
print(x)
print(len(x))
print(x[3])
print(x[2:4])
print(x[:4])
print(x[2:])
print(x[-1])
print(x[-4:])
print(x[:-3])
```
- ***Python Tuples***
```python
#Python Tuples

x = ('python', 2000, 'c++', 3.2, 'java')
print(x)
print(len(x))
print(x[1] + x[3])
print(x[0] + x[-1])
print(x[:2] + x[3:])
print(x[2] * 3)
print(x[1] * 3)
print(x[2:4] * 2)
print((x[1:3] + x[4:5]) * 2)
```
- ***Python Tuples***
```python
#Python Tuples

x = ('python', 2000, 'c++', 3.2, 'java')
print(x)
print(len(x))
print(x[::4])
print(x[::3])
print(x[::2])
print(x[::1])
print(x[::-1])
print(x[::-2])
print(x[::-3])
print(x[::-4])
```
- ***Python Tuples***
```python
#Python Tuples

x = ('python', 2000, 'c++', 3.2, 'java')
print(x)
print(len(x))
print(x[1:4:4])
print(x[1:4:3])
print(x[1:4:2])
print(x[1:4:1])
print(x[-2:0:-4])
print(x[-2:0:-3])
print(x[-2:0:-2])
print(x[-2:0:-1])
```

## 2.6- Python Dictionaries
- ***Python Dictionaries***
```python
#Python Dictionaries

x = {'python':'easy', 'c++':'medium', 'java':'hard'}
print(x)
print(len(x))
print(x['python'])
x['c#'] = 'medium'
x['c++'] = 0
print(x)
print(len(x))
print(x['c#'])
print(x['c++'])
```
- ***Python Dictionaries***
```python
#Python Dictionaries

x = {'London': 6, 'Paris': 8, 'Barcelone': 11}
print(x)
x['Paris'] = {'Zurich': 2, 'Roma': 5}
x['Barcelone'] = 'windy'
print(x)
print(x['Paris']['Zurich'])
print(x['Barcelone'][:3])
```

## 2.7- Python Sets
- ***Python Sets***
```python
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
```
- ***Python Sets***
```python
#Python Sets

x = {0, 2, 'ab', 4, 6, 'cd', 8}
y = {1, 2, 'ef', 3, 4, 'cd', 5}

print(x | y)
print(x & y)
print(x - y)
print(y - x)
print(x ^ y)
```

## 2.8- Data Type Conversion
- ***Data Type Conversion***
```python
#Data Type Conversion

print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))
```
- ***Data Type Conversion***
```python
#Data Type Conversion

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
```
- ***Data Type Conversion***
```python
#Data Type Conversion

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
```
- ***Data Type Conversion***
```python
#Data Type Conversion

x, y, z = 'a', 97, 24
print(ord(x))
print(chr(y))
print(hex(z))
print(oct(z))
print(bin(z))
```
- ***Data Type Conversion***
```python
#Data Type Conversion

x = 'hello python'
print(list(x))
print(tuple(x))
print(set(x))
```
- ***Data Type Conversion***
```python
#Data Type Conversion

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
```
- ***Data Type Conversion***
```python
#Data Type Conversion

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
```
- ***Python Input***
```python
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
```
- ***Python Input***
```python
#Python Input

x, y, z = input('Enter 3 values: ').split()
print(x, y, z)
print(type(x), type(y), type(z))
x, y, z = int(x), str(y), float(z)
print(x, y, z)
print(type(x), type(y), type(z))
```
- ***Python Input***
```python
#Python Input

x, y, z = map(str, input('Enter 3 strings: ').split())
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = map(int, input('Enter 3 int numbers: ').split())
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = map(float, input('Enter 3 float numbers: ').split())
print(x, y, z)
print(type(x), type(y), type(z))
```
- ***Python Output***
```python
#Python Output

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='$', end='&')
print(1, 2, 3, 4)

x = 87.654321
print('The value of x is %.0f' % x)
print('The value of x is %.1f' % x)
print('The value of x is %.2f' % x)
print('The value of x is %.3f' % x)
print('The value of x is %.4f' % x)
```

### Practice

- ***Practice input 1***
```python
name = str(input())
age = int(input())
weight = float(input())
print(name, age, weight)
```

- ***Practice input 2***
```python
course1, course2, course3 = map(int, input().split())
print(course1)
print(course2)
print(course3)
```

- ***Practice input 3***
```python
name, age, weight = input().split()
age = int(age)
weight = float(weight)
print(name, age, weight, sep = '\n')
```
