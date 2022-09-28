inp = int(input())
x, a, b = 0, 0, 0
for i in range(1, inp + 1):
    if i <= 2:
        x, a, b = 1, 1, 1
    if i > 2:
        x = a + b
        a = b
        b = x
    print(x, end=' ')
