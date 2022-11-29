import random
n = int(4)
m = int(4)
k = int(1)
iM = int(0)
iX = int(0)
jM = int(0)
jX = int(0)
maxx=int(0)
minn=int(100)
null=int(0)
A = []
for i in range(n):
    B = []
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
for i in range(n):
    for j in range(m):
        print(A[i][j],' ', end=' ')
    print()
print('---------')