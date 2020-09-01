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
