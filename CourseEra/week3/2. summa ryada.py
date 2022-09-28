n = int(input())
i, summa = 1, 0

while i <= n:
    summa += 1 / i ** 2
    i += 1
print('{0:.5f}'.format(summa))
