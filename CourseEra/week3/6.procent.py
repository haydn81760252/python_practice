import math

p = float(input())
x = float(input())
y = float(input())

# procent = p / 100
vklad = ((x + y / 100) * p / 100) + x + y / 100
rub = math.floor(vklad)
kop = (vklad - math.floor(vklad)) * 100

print('{0:.0f} {1:.0f}'.format(rub, kop))
