x = int(input())
y = int(input())
if y % (y - x + 1):
    print('NO')
else:
    print('YES')
