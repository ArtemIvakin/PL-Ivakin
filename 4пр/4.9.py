n=int(input("число: "))
sum=int(1)
i1=int(0)
i2=int(1)
for i in range(n-2):
    i3=i1+i2
    sum=sum+i3
    i1=i2
    i2=i3
print(sum)
