n = 30
i = 1
a = 301

for i in range(n, a):
	if i%7 == 0 and i%13 == 0:
		print ('abc')
	elif i%7 == 0:
		print ('xyz')
	elif i%13 == 0:
		print ('a-z')
	else:
		print (i)
		
