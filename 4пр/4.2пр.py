a=int(input("первое число: "))
b=int(input("второе число: "))
if a <= b:
    for i in range(a, b):
       print(i)
    print(b)
if a > b:

    for i in range(a, b, -1):
        print(i)
    print(b)