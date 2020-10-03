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
