n = int(input())
max1, max2 = 0, 0
while n != 0:
    if n > max2:
        max2 = n
        print('if 1 -max1=', max1, 'max2=', max2)
    if n > max1:
        max2, max1 = max1, n
        print('if 2 - max1=', max1, 'max2=', max2)
        # max2 = max1
        # max1 = n
    n = int(input())
print(max2)
print('max1=', max1, 'max2=', max2)