def rarup(a, b):
    print(a)
    if a == b:
        return 1
    return rarup(a+1,b)

def rardown(a, b):
    print(a)
    if a == b:
         return 1
    return rardown(a-1,b)

x=int(input('x='))
n=int(input('n='))
if x > n:
    rardown(x, n)
else:
    rarup(x, n)
