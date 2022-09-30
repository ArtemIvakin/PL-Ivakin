n=int(input("число: "))
k=int(input('число: '))
sum=int(0)
i1=int(0)
i2=int(1)
for i in range(n-2):
    i3=i1+i2
    if i+3>=k:
        print(i3)
        sum=sum+i3
    i1=i2
    i2=i3
print(sum)