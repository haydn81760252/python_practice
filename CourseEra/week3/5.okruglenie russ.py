import math
x = float(input())

ostatok = x - math.floor(x)
if ostatok >= 0.5:
    print(math.ceil(x))
else:
    print(math.floor(x))
