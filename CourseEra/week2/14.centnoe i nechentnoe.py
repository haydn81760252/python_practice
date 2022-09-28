a = int(input())
b = int(input())
c = int(input())

if not a % 2 and not b % 2 and not c % 2:
    print('NO')
elif a % 2 and b % 2 and c % 2:
    print('NO')
else:
    print('YES')
