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
