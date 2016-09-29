def FiBu(n):
#	result = ()
	for n in range(1, n):
		if n % 3 == 0 and n % 5 == 0:
			print('FizzBuzz', ' ',end='')
		elif n % 3 == 0:
		#	result.append('Fizz', end='')
			print('Fizz', ' ' ,end = '')
		elif n % 5 == 0:
		#	result.append('Buzz', end = )
			print('Buzz', ' ', end = '')
		else:
#			result.append(n)
			print(n, ' ', end = '')
	print()

FiBu(100)
					
