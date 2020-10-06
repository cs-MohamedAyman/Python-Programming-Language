<img align="right" width="90" height="90" src="https://github.com/cs-MohamedAyman/Computer-Science-Textbooks/blob/master/logos/python.jpg">

# Lecture 03 - Basic Operations
## 3.1- Arithmetic Operators
- ***Arithmetic Operators***
```python
#Arithmetic Operators

x, y = 21, 10
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
x, y = 2, 3
print(x ** y)
x, y = 11, 5
print(x // y)
```
### Quiz
## 3.2- Comparison Operators
- ***Comparison Operators***
```python
#Comparison Operators

x, y = 21, 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x, y = 'a', 'd'
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```
### Quiz
## 3.3- Bitwise Operators
- ***Bitwise Operators***
```python
#Bitwise Operators

x, y = 60, 13
print(x, bin(x))
print(y, bin(y))
print(x & y)
print(x | y)
print(x ^ y)
print(~x)

print(y, bin(y))
print(y >> 3)
print(y << 3)
```
### Quiz
## 3.4- Assignment Operators
- ***Assignment Operators***
```python
#Assignment Operators

x, y, z = 21, 10, 0
z += x
print(z)
z -= y
print(z)
z *= x
print(z)
z //= y
print(z)
z %= x
print(z)
z **= y
print(z)
z /= y
print(z)
```
### Quiz
## 3.5- Logical Operators
- ***Logical Operators***
```python
#Logical Operators

x, y = True, False
print(x and y)
print(x or y)
print(not x)
print(not y)

a, b, c, d = 10, 5, 7, 3
print(a > b and c < d)
print(a > b or c < d)
print(not a > b)
print(not c < d)
```
### Quiz
## 3.6- Membership Operators
- ***Membership Operators***
```python
#Membership Operators

x = 'Hello World'
y = {'a':1, 'b':2, 'c':3}
z = [17, -31, 'Hello World', [20, 61], (15, -9)]
print('H' in x)
print('Hello' in x)
print('b' in y)
print(3 not in y)
print(-31 in z)
print(61 not in z)
print(61 in z[3])
print('W' in z[2])
print('World' in z[2])
print('W' not in z)
```
### Quiz
## 3.7- Identity Operators
- ***Identity Operators***
```python
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
```
- ***Identity Operators***
```python
#Identity Operators

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
```
- ***Identity Operators***
```python
#Identity Operators

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
```
### Quiz
## 3.8- Operators Precedence
- ***Operators Precedence***
```python
#Operators Precedence

a, b, c, d = 20, 10, 15, 5
print(a + b * c / d)
print((a + b) * c / d)
print(a + b * (c / d))
print(a + b ** d * c)
print(a + b * c >> d)
print(a + b * c << d)

a, b, c, d = True, False, False, True
print(a and b or c and d)
print(a or b and c or d)
print(a and not b or c and d)
print(a or b and not c or d)
```
### Quiz
### Practice
- ***Practice fahrenheit conversion***
```python
f = float(input())
print((f - 32) / 1.8)
```
- ***Practice kilometer conversion***
```python
k = float(input())
print(k * 0.621371)
```
- ***Practice quadratic equation***
```python
a, b, c = map(float, input().split())
d = (b ** 2) - (4 * a * c)
sol1 = (-b - (d ** 0.5)) / (2 * a)
sol2 = (-b + (d ** 0.5)) / (2 * a)
print(sol1, sol2)
```
- ***Practice simple equation***
```python
x = int(input())
y = (x - 1) ** 3 + (x + 1) ** 2 + 2*x + 7
print(y)
```
- ***Practice square root***
```python
x = float(input())
print(x ** 0.5)
```
- ***Practice swap numbers***
```python
x, y = map(int, input().split())
x, y = y, x
print(x, y)
```
