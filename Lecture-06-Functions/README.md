<img align="right" width="90" height="90" src="https://github.com/cs-MohamedAyman/Computer-Science-Textbooks/blob/master/logos/python.jpg">

# Lecture 06 - Functions
## 6.1- Function Definition
## 6.2- Calling a Function
- ***Calling a Function***
```python
#Calling a Function

def summation(x, y):
	res = x + y
	return res

r = summation(4, 3)
print(r)

a, b = 6, 8
r = summation(a, b)
print(r)
```
## 6.3- Return Statement
- ***Return Statement***
```python
#Return Statement

def add_one_hundred(x, y):
	x += 100
	y += '100'

a, b = 6, '8'
a, b = add_one_hundred(a, b)
print(a)
print(b)
```
### Quiz
### Practice
- ***Practice computing the number of days in a month***
```python
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

print(days_in_month(2000, 3))
print(days_in_month(2010, 6))
print(days_in_month(2100, 2))
print(days_in_month(2400, 2))
```
- ***Practice comparing two dates***
```python
def compare_dates(year1, month1, day1, year2, month2, day2):
    if year1 != year2:
        return 1 if year1 > year2 else -1
    if month1 != month2:
        return 1 if month1 > month2 else -1
    if day1 != day2:
        return 1 if day1 > day2 else -1
    return 0

print(compare_dates(2010, 1, 1,  2011, 1, 1 ))
print(compare_dates(2000, 7, 31, 2000, 4, 30))
print(compare_dates(2010, 1, 1,  2010, 1, 1 ))
```
- ***Practice calculate the next day***
```python
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

def next_date(year, month, day):
    day += 1
    if day > days_in_month(year, month):
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month, day

print(next_date(2010, 1, 1))
print(next_date(2010, 1, 31))
print(next_date(2100, 2, 28))
print(next_date(2010, 12, 31))
```
- ***Practice checking if a date is valid***
```python
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

def is_valid_date(year, month, day):
    return 1 <= year <= 9999 and \
           1 <= month <= 12 and \
           1 <= day <= days_in_month(year, month)

print(is_valid_date(2000, 2, 29))
print(is_valid_date(2010, 4, 31))
print(is_valid_date(2020, 8, 32))
print(is_valid_date(2100, 2, 29))
```
- ***Practice computing the number of days between two dates***
```python
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28

def is_valid_date(year, month, day):
    return 1 <= year <= 9999 and \
           1 <= month <= 12 and \
           1 <= day <= days_in_month(year, month)

def compare_dates(year1, month1, day1, year2, month2, day2):
    if year1 != year2:
        return 1 if year1 > year2 else -1
    if month1 != month2:
        return 1 if month1 > month2 else -1
    if day1 != day2:
        return 1 if day1 > day2 else -1
    return 0

def next_date(year, month, day):
    day += 1
    if day > days_in_month(year, month):
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month, day

def days_between(y1, m1, d1, y2, m2, d2):
    if not is_valid_date(y1, m1, d1) or \
       not is_valid_date(y2, m2, d2):
       return 0

    cur_y, cur_m, cur_d = y1, m1, d1
    n_days = 0
    while compare_dates(cur_y, cur_m, cur_d, y2, m2, d2) == -1:
        n_days += 1
        cur_y, cur_m, cur_d = next_date(cur_y, cur_m, cur_d)

    return n_days

print(days_between(2010, 1, 1,  2011, 1, 1 ))
print(days_between(2000, 4, 30, 2000, 7, 31))
print(days_between(2010, 1, 1,  2000, 12,31))
print(days_between(2020, 4, 31, 2020, 7, 31))
```
## 6.4- Passing by Reference and Value
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
### Practice
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
### Quiz
## 6.5- Function Arguments
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
### Quiz
### Practice
- ***Practice prime number***
```python
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
print('prime' if is_prime(n) else 'not prime')
```
- ***Practice min max***
```python
def calc_min(x, y, *z):
    res = x if x < y else y
    for i in z:
        if res > i:
            res = i
    return res

def calc_max(x, y, *z):
    res = x if x > y else y
    for i in z:
        if res < i:
            res = i
    return res

print(calc_min(7, 4))
print(calc_min(7, 4, 8))
print(calc_min(7, 4, 8, 3))
print(calc_min(7, 4, 8, 3, 1))

print(calc_max(7, 4))
print(calc_max(7, 4, 8))
print(calc_max(7, 4, 8, 3))
print(calc_max(7, 4, 8, 3, 11))
```
## 6.6- Anonymous Function
- ***Anonymous Function***
```python
#Anonymous Function

summation = lambda x, y, z : x + y + z

r = summation(5, 11, 7)
print(r)
r = summation(y = 5, z = 11, x = 7)
print(r)

summation = lambda x, y = 3, z = 2 : x + y + z

r = summation(5, 11, 7)
print(r)
r = summation(5, 11)
print(r)
r = summation(5)
print(r)
```
- ***Map and Filter Function***
```python
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
```
### Quiz
### Practice
- ***Practice distance two points***
```python
dist = lambda x1, y1, x2, y2 : ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print(dist(x1, y1, x2, y2))
```
- ***Practice distance two points***
```python
def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print(dist(x1, y1, x2, y2))
```
- ***Practice summation range***
```python
def summation(x, y):
    res = 0
    for i in range(x, y+1):
        res += i
    return res

x, y = map(int, input().split())
print(summation(x, y))
```
- ***Practice summation range***
```python
summation = lambda n : n * (n+1) // 2

x, y = map(int, input().split())
print(summation(y) - summation(x-1))
```
## 6.7- Inner Functions
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
### Quiz
### Practice
- ***Python Input***
```python
#Python Input

```
## 6.8- Global and Local Variables
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
### Quiz
### Practice
- ***Python Input***
```python
#Python Input

```
- ***Python Input***
```python
#Python Input

```
