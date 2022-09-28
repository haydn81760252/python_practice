n = int(input())
summa = 1
pred = 0
tek = 0
while n != 0:
    if pred == tek:
        summa += 1
    if n > pred:
        pred = n
        if summa >= 2:
            summa = 0
        # print('if 1 -max1=', tek, 'max2=', pred)
    if n > tek:
        pred, tek = tek, n
        # print('if 2 - max1=', tek, 'max2=', pred)
        # max2 = max1
        # max1 = n
        if summa >= 2:
            summa = 0

    n = int(input())
print(summa)
# print('max1=', tek, 'max2=', pred)


#    if n == pred:
#        summa += 1
#    pred = n
#    n = int(input())
# print(summa)
