n = int(input())
summa = 0
pred = n
while n != 0:
    if n == pred:
        summa += 1
    pred = n
    n = int(input())
print(summa)
