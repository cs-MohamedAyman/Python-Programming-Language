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
