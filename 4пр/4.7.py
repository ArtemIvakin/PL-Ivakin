n=int(input("число: "))
fac=int(1)
sum=int(0)
for i in range(1,n+1):
    fac=fac*i
    sum=sum+fac
print(sum)