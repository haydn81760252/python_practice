x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

x = x1 - x2
y = y1 - y2
# модуль числа
if x < 0:
    x *= -1
if y < 0:
    y *= -1

if x == y: # ход по диагонали
    print('YES')
elif x1 == x2 or y1 == y2:
    print('YES')
elif -1 <= x <= 1 and -1 <= y <= 1:
    print('YES')
else:
    print('NO')