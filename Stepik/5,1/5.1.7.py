x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

x = x1 - x2
y = y1 - y2
# модуль числа
if x < 0:
    x *= -1
if y < 0:
    y *= -1

if x == 1 and y == 2 or x == 2 and y == 1 :
    print('YES')
else:
    print('NO')