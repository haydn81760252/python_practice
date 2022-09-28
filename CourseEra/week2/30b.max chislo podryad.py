n = int(input())
summa1, summa2, maximum = 1, 0, 0
pred = 0
tek = 0
while n != 0:
    if n == pred:
        summa1 += 1
    elif summa1 >= summa2:
        summa2, summa1 = summa1, 1
    elif summa1 >= summa2:
        summa2, summa1 = summa1, 1

    # print('pred = ', pred)
    # print('tek = ', n)
    print('summa1 = ', summa1)
    print('summa2 = ', summa2)
    pred = n
    n = int(input())
if summa1 > summa2:
    print(summa1)
else:
    print(summa2)
