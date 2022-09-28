x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

x = x1 - x2
y = y1 - y2

if x < 0:
    x *= -1
if y < 0:
    y *= -1

if x == y:
    print('YES')
else:
    print('NO')