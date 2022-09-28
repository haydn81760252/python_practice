n = int(input())

ed = n % 10
des = n // 10 % 10
sot = n // 100 % 10
t = n // 1000

print('Цифра в позиции тысяч равна {}'.format(t))
print('Цифра в позиции сотен равна {}'.format(sot))
print('Цифра в позиции десятков равна {}'.format(des))
print('Цифра в позиции единиц равна {}'.format(ed))

# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# print(t, sot, des, ed)
# print('Сумма цифр = {}'.format(sot+des+ed))
# print('Произведение цифр = {}'.format(sot*des*ed))
