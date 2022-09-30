a=int(input("первое число: "))
b=int(input("второе число: "))
for i in range(a, b-1,-1):
    if (i % 2 == 0):
        print(i)
