import math
def prtreug(a,b):
	print('площадь прямоугольного треугольника: ',(a*b)/2)
def treug(a,b,c,d):
	gip= math.ceil(math.sqrt(pow(a,2)+pow(b,2))) #нахождение гиппотинузы
	print("гиппотинуза", gip)
	p=math.ceil((c+b+gip)/2) #полупериметр
	print("полупериметр", p)
	print('нахождение второго треугольника: ', math.ceil(math.sqrt(p*(p-gip)*(p-c)*(p-d)))) #площадь второго теугольтника


print("стороны при прямом углу: ")
X=int(input('X='))
Y=int(input('Y='))
print("остальные стороны: ")
Z=int(input('Z='))
T=int(input('T='))
prtreug(X, Y)
treug(X,Y,Z,T)
