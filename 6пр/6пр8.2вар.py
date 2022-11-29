x=[]
for i in range (5):
	x.append (int(input()))
sr=int(sum(x)/5)
for k,a in enumerate(x):
	if a==0:
		x[k] = sr
print(x)
