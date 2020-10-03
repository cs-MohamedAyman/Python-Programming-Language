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
