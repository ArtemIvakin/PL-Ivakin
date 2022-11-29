v=int(input('введите начало интервала \n'))
k=int(input('введите конец интервала \n'))
if v < 2 and k == 1:
	print(v-k+1)
elif k>v:
	print(pow(k,2)+pow(v,2))
else:
	print(pow(k,2)+v)
