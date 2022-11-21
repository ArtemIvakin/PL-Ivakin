k=int(1)
v=int(0)
v1=int(0)
summ=int(0)
koll=int(0)
iM = int(0)
iX = int(0)
jM = int(0)
jX = int(0)
maxx=int(0)
minn=int(100)

file_i = open('input.txt','r')
file_o = open('output.txt','r+')

D=[[int(x) for x in i.split()]for i in file_i]
l=len(D)

A=[]
for i in range(l):
	B=[]
	for j in range(l):
			B.append(D[i][j])
	A.append(B)

for i in range(l):
	for j in range(l):
		print(A[i][j],' ', end=' ')
	print()
print(A[1][0])
############################1111
for i in range(l):
	for j in range(l):
		if  (j >= k) :
			if (A[i][j] > 0 ):
				summ=summ+A[i][j]
				koll=koll+1
	k=k+1
print('------')
print(summ,' ',koll)
print('------')
file_o.write('		1.1 сумма и количество положительных элементов над главной диагональю')
file_o.write('\n')
file_o.write('сумма:'+ str(summ)+'; количество элементов:'+str(koll)+'.')
file_o.write('\n')
file_o.write('\n')

############################3333
file_o.write('		2.1')
file_o.write('\n')
for i in range(l):
	v=v+A[1][i]
print(v)
for i in range(l):
	for j in range(l):
		v1=v1+A[i][j]
	if v1 != v:
		print('стрi',i)
		print()
		k=1
	else:
		v1=0
for i in range(l):
	for j in range(l):
		v1=v1+A[j][i]
	if v1 != v:
		k=1
	else:
		v1=0
if k == 1:
	file_o.write('не магический квадрат')
else:
	file_o.write('магический квадрат')
file_o.write('\n')
file_o.write('\n')
############################3333
file_o.write('		1.2 замена максимального и минимального в строке')
file_o.write('\n')
for i in range(l):
    for j in range(l):
        if A[i][j] > maxx:
            maxx=A[i][j]
            iX=i
            jX=j
        if A[i][j] < minn:
            minn= A[i][j]
            iM=i
            jM=j
    print(i)
    print('max', A[iX][jX])
    print('min', A[iM][jM])
    print('---')
    null=A[iX][jX]
    A[iX][jX]=A[iM][jM]
    A[iM][jM]=null
    iM = int(0)
    iX = int(0)
    jM = int(0)
    jX = int(0)
    maxx=int(0)
    minn=int(100)
    null=int(0)

for i in range(l):
	for j in range(l):
		file_o.write(str(A[i][j])+' ')
	file_o.write('\n')
	k=k+1
file_o.write('\n')

############################4444
file_o.write('		2.2 замена первого и последнего столбца')
file_o.write('\n')
A=[]
for i in range(l):
	B=[]
	for j in range(l):
			B.append(D[i][j])
	A.append(B)
file_o.write('оригинал')
file_o.write('\n')
for i in range(l):
	for j in range(l):
		file_o.write(str(A[i][j])+' ')
	file_o.write('\n')
	k=k+1
file_o.write('\n')

for i in range(l):
	null=A[i][0]
	A[i][0]=A[i][l-1]
	A[i][l-1]=null
file_o.write('замена')
file_o.write('\n')
for i in range(l):
	for j in range(l):
		file_o.write(str(A[i][j])+' ')
	file_o.write('\n')
	k=k+1
file_o.write('\n')
file_i.close
file_o.close	
