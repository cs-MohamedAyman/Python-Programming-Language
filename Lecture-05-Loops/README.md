<img align="right" width="90" height="90" src="https://github.com/cs-MohamedAyman/Computer-Science-Textbooks/blob/master/logos/python.jpg">

# Lecture 05 - Loops
## 5.1- Loop Definition
## 5.2- While Loop Statements
- ***While Loop Statements***
```python
#While Loop Statements

i = 0
while i < 3:
    print(i)
    i += 1
print('the program completed')
```
## 5.3- Else with While Loop
- ***Else with While Loop***
```python
#Else with While Loop

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('i not less than 3')
```
##
### Practice
- ***Practice While Loops factorial***
```python
n = int(input())
i, res = 1, 1
while i <= n:
    res *= i
    i += 1
print(res)
```
- ***Practice While Loops factors***
```python
n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print(i, end = ' ')
    i += 1
```
- ***Practice While Loops power of 2***
```python
n = int(input())
i = 0
while i <= n:
    print(2**i, end = ' ')
    i += 1
```
- ***Practice While loops summation of n***
```python
n = int(input())
i, res = 1, 0
while i <= n:
    res += i
    i += 1
print(res)
```
## 5.4- For Loop Statements
- ***The Range Function***
```python
#The Range Function

fruits = ['banana', 'apple', 'orange']
for i in range(len(fruits)):
    print(fruits[i])
print('the program completed')

x = ['c', 'java', 'c++', 'python', 'scala', 'R', 'matlab']
for i in range(2, len(x)-2):
    print(x[i])
print('the program completed')
```
- ***For Loop Statements***
```python
#For Loop Statements

for i in 'python':
    print(i)
print('the program completed')

fruits = ['banana', 'apple', 'orange']
for i in fruits:
    print(i)
print('the program completed')
```
## 5.5- Else with For Loop
- ***Else with For Loop***
```python
#Else with For Loop

x = [48, 67, 73]
for i in range(len(x)):
    print(x[i])
else:
    print('we reach the end of the list')
```
##
### Practice
- ***Practice For Loops factorial***
```python
n = int(input())
res = 1
for i in range(1, n+1):
    res *= i
print(res)
```
- ***Practice For Loops factors***
```python
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end = ' ')
```
- ***Practice For Loops power of 2***
```python
n = int(input())
for i in range(n+1):
    print(2**i, end = ' ')
```
- ***Practice For loops summation of n***
```python
n = int(input())
res = 0
for i in range(1, n+1):
    res += i
print(res)
```
## 5.6- Nested Loops
- ***Nested Loops***
```python
#Nested Loops

i = 1
while i < 4:
    j = 1
    while j < 4:
        print(i*j, end = ' ')
        j += 1
    print()
    i += 1

for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end = ' ')
    print()
```
##
### Practice
- ***Practice While Loops identity matrix***
```python
n = int(input())
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
        j += 1
    print()
    i += 1
```
- ***Practice For Loops identity matrix***
```python
n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()
```
## 5.7- Loop Control Statements
- ***Loop Control Statement Break***
```python
#Loop Control Statement Break

i = 0
while i < 4:
    if i == 2:
        break
    print(i)
    i += 1
print('the program completed')

for i in 'python':
    if i == 't':
        break
    print(i)
print('the program completed')
```
- ***Loop Control Statement Continue***
```python
#Loop Control Statement Continue

i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i)
print('the program completed')

for i in 'python':
    if i == 't':
        continue
    print(i)
print('the program completed')
```
- ***Loop Control Statement Pass***
```python
#Loop Control Statement Pass

n = int(input())
if n < 0:
    pass

n = int(input())
for i in range(n):
    pass
```
##
### Practice
- ***Practice While Loops prime number***
```python
n = int(input())
i = 2
while i < n:
    if n % i == 0:
        print('NO')
        break
    i += 1
else:
    print('YES')
```
- ***Practice For Loops prime number***
```python
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print('NO')
            break
else:
    print('YES')
```
