n = int(input())
pred = n
kolvo = 0
while n != 0:
    if n > pred:
        kolvo += 1
    pred = n
    n = int(input())
print(kolvo)
