import math
x = float(input())

rub = math.floor(x)
kop = (x - rub) * 100

# print(rub, kop)
# print(f'{rub:.0f} {kop:.0f}')
print('{0:.0f} {1:.0f}'.format(rub, kop))
