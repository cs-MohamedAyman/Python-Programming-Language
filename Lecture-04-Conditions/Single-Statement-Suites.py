#Single Statement Suites

n = 3
print('positive') if n > 0 else print('negative') if n < 0 else print('zero')
print('positive' if n > 0 else 'negative' if n < 0 else 'zero')

n = 3
print('even') if n % 2 == 0 else print('odd')
print('even' if n % 2 == 0 else 'odd')
