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
