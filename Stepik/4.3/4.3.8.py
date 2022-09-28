n = int(input())

if n > 36 or n < 0:
    print('ошибка ввода')
elif n == 0:
    print('зеленый')
elif n <= 10:
    if n % 2 == 0:
        print('черный')
    else:
        print('красный')
elif n <= 18:
    if n % 2 == 0:
        print('красный ')
    else:
        print('черный ')
elif n <= 28:
    if n % 2 == 0:
        print('черный')
    else:
        print('красный')
elif n <= 36:
    if n % 2 == 0:
        print('красный ')
    else:
        print('черный ')