x = int(input())
if x >= 85: 
	print('Excellent ' + ('A+' if x >= 90 else 'A'))
elif x >= 75: 
	print('Very Good ' + ('B+' if x >= 80 else 'B'))
elif x >= 65: 
	print('Good ' + ('C+' if x >= 70 else 'C'))
elif x >= 50: 
	print('Pass ' + ('D+' if x >= 60 else 'D'))
else: 
	print('Fail')
