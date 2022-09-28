n = int(input())
max1 = n
kolvo = 0
while n != 0:
    if n >= max1:
        max2 = max1
        max1 = n
    n = int(input())
print(kolvo)
