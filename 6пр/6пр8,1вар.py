summ=int(0)
umn=int(1)
x=[]
for i in range (5):
	x.append (int(input()))
	summ+=x[i]
	umn*=x[i]
print(summ)
print(umn)
print(len(x))
