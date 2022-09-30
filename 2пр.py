import math
x = 0.1722
y = 6.33
z = 3.25 * pow(10,-4)
print ( 5 * math.atan(x) - ( 1 / 4 ) * (math.acos(x)) * ((x+3*(abs(x-y))+pow(x,2))/(abs(x-y)*z+pow(x,2))) )


