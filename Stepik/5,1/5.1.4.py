n = int(input())

if 1 <= n <= 3:
    print('I'*n)
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif 6 <= n <= 8:
    print('V'+'I'* (n-5))
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('ошибка')