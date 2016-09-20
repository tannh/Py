s = 'Shigeo.Tokuda.jp'
index = 0
for i in range(len(s)):
	if s[i] == '.':
		index = i
print(s[:index]) 
