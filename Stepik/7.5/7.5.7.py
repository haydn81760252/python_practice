n = int(input())
sravn = n % 10
flag = True
while n != 0:
    last_d = n % 10
    if last_d != sravn:
        flag = False


if flag:
    print('YES')
else:
    print('NO')
