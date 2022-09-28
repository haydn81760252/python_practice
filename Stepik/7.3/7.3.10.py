flag = True

for _ in range(10):
    n = int(input())
    if n % 2 != 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')