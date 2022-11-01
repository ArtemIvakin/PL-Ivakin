minn=int(1000000)
mini=int(0)
maxx=int(0)
maxi=int(0)
x=[]
for i in range(6):
	x.append( int( input() ))
	if x[i] < minn:
		minn= x[i]
		mini= i
	if x[i] > maxx:
		maxx= x[i]
		maxi= i
x[mini]=maxx
x[maxi]=minn
print(x)
