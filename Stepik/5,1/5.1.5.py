n = int(input())

if n % 2 != 0:
    print('YES')
elif n % 2 == 0 and n > 20:
    print('NO')
elif 2 <= n <= 5:
    print('NO')
elif 6 <= n <= 20:
    print('YES')
