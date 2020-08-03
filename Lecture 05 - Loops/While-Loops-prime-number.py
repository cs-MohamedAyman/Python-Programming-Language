n = int(input())
i = 2
while i < n:
	if n % i == 0:
		print('NO')
		break
	i += 1
else:
	print('YES')
