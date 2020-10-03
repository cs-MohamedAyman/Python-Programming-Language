summation = lambda n : n * (n+1) // 2

x, y = map(int, input().split())
print(summation(y) - summation(x-1))
