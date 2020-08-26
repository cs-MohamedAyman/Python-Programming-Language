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
