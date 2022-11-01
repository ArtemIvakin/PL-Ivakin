summ=int(0)
umn=int(1)
x=[]
for i in range(6):
	x.append( int( input() ))
	if i % 2 == 0:
		summ+= x[i]
	else:
		umn*=x[i]
print(summ)
print(umn)
