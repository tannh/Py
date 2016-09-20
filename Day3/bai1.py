a = bin(10)
b = 0
for i in range(len(a)):
	if a[i] == '1':
		b = i
		print(a[b:])
print(a[b:])
		
