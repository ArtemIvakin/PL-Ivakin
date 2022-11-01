#1 Найти наибольший элемент списка, который делиться на 2 без остатка и
#вывести его на экран.
maxx=int(0)
x=[]
for i in range(6):
    x.append(int(input()))
    if (x[i] > maxx) and (x[i] % 2 == 0):
        maxx=x[i]
print(x)
print(maxx)