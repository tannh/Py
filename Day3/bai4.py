s = list(range(5, 20))
ss = list(enumerate(s, start=1))
for i in range(len(ss)):
	sss = ss[i]
	print(sss[0], sss[1]) 
