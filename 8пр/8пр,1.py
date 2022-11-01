import random
n = int(4)
m = int(4)
k = int(1)
summ=int(0)
koll=int(0)

mull=int(0)
A = []
#for i in range(n):
	#A.append(random.randint(-10,10))
for i in range(n):
	B=[]
	for j in range(m):
		B.append(int(random.randint(-10,10)))
	A.append(B)
	
for i in range(n):
	for j in range(m):
		print(A[i][j],' ', end=' ')
	print()
print('---------')
		
for i in range(n):
	for j in range(m):
		if (i == j) or (j >= k) :
			print(A[i][j],' ', end=' ')
		else :
			print('  ',end=' ')
	print()
	k=k+1
k = 1
for i in range(n):
	for j in range(m):
		if  (j >= k) :
			if (A[i][j] > 0 ):
				summ=summ+A[i][j]
				koll=koll+1
	print()
	k=k+1
print('------')
print(summ,' ',koll)
print('------')
