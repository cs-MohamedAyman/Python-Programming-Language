<img align="right" width="90" height="90" src="https://github.com/cs-MohamedAyman/Computer-Science-Textbooks/blob/master/logos/python.jpg">

# Lecture 04 - Conditions

<details>
	<summary>4.1- Decision making Definition</summary>

</details>

<details>
	<summary>4.2- IF Statement</summary>

  - ***IF Statement***
  ```python
  #If Statement

  x = 3
  if x > 0:
		print("it's a positive number")
  x = -3
  if x > 0:
		print("it's a positive number")
  ```

</details>

<details>
	<summary>4.3- IF and ELSE Statements</summary>

  - ***IF and ELSE Statements***
  ```python
  #If and Else Statements

  n = 3
  if n % 2 == 0:
		print("it's an even number")
  else:
		print("it's an odd number")
  ```

</details>

<details>
	<summary>4.4- IF, ELIF and ELSE Statements</summary>

  - ***IF, ELIF and ELSE Statements***
  ```python
  #If, Elif and Else Statements

  n = 3
  if n > 0:
		print("it's a positive number")
  elif n < 0:
		print("it's a negative number")
  else:
		print("It's zero")
  ```

  ### Practice
  - ***Practice max number***
  ```python
  x, y, z = map(int, input().split())
  if x >= y and x >= z:
		print(x)
  elif y >= x and y >= z:
		print(y)
  else:
		print(z)
  ```
  - ***Practice grading system 1***
  ```python
  x = int(input())
  if x >= 85: print('Excellent')
  elif x >= 75: print('Very Good')
  elif x >= 65: print('Good')
  elif x >= 50: print('Pass')
  else: print('Fail')
  ```

</details>

<details>
	<summary>4.5- Nested IF Statements</summary>

  - ***Nested If Statements***
  ```python
  #Nested If Statements

  n = 6
  if n % 2 == 0:
		if n % 3 == 0:
			print("this number divisible by 2 and 3")
		else:
			print("this number divisible by 2")
  else:
		if n % 3 == 0:
			print("this number divisible by 3")
		else:
			print("this number not divisible by 2 nor 3")
  ```

  ### Practice
  - ***Practice grading system 2***
  ```python
  x = int(input())
  if x >= 85: 
		print('Excellent')
		if x >= 90: print('A+')
		else: print('A')
  elif x >= 75: 
		print('Very Good')
		if x >= 80: print('B+')
		else: print('B')
  elif x >= 65: 
		print('Good')
		if x >= 70: print('C+')
		else: print('C')
  elif x >= 50: 
		print('Pass')
		if x >= 60: print('D+')
		else: print('D')
  else: 
		print('Fail')
  ```

</details>

<details>
	<summary>4.6- Single Statement Suites</summary>

  - ***Single Statement Suites***
  ```python
  #Single Statement Suites

  n = 3
  print('positive') if n > 0 else print('negative') if n < 0 else print('zero')
  print('positive' if n > 0 else 'negative' if n < 0 else 'zero')

  n = 3
  print('even') if n % 2 == 0 else print('odd')
  print('even' if n % 2 == 0 else 'odd')
  ```

  ### Practice
  - ***Practice grading system 3***
  ```python
  x = int(input())
  if x >= 85: 
		print('Excellent ' + ('A+' if x >= 90 else 'A'))
  elif x >= 75: 
		print('Very Good ' + ('B+' if x >= 80 else 'B'))
  elif x >= 65: 
		print('Good ' + ('C+' if x >= 70 else 'C'))
  elif x >= 50: 
		print('Pass ' + ('D+' if x >= 60 else 'D'))
  else: 
		print('Fail')
  ```

</details>
