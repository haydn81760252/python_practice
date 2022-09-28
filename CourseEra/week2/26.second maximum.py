n = int(input())
max1 = 0
max2 = 0
while n != 0:
    if n > max1:
       # max2 = max1
        max1 = n
        # print('if2')
    if n < max1:
        if n > max2:
            max2 = n
    if n == max1:
        max2 = max1

        # print('if4')

        # print('if3')
    n = int(input())
print(max2)
