from math import log
n = int(input())

summa = 1
for i in range(2, n+1):
    summa += 1 / i
print((summa)-log(n))
