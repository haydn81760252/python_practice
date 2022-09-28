a = input()
b = input()

red, blue, yellow = 'красный', 'синий', 'желтый'

# if a == red or a == blue or a == yellow and b == red or b == blue or b == yellow:
if (a == red or a == blue or a == yellow) and a == b:
    print(a)
elif a == red and b == blue or b == red and a == blue:
    print('фиолетовый')
elif a == red and b == yellow or b == red and a == yellow:
    print('оранжевый')
elif a == blue and b == yellow or b == blue and a == yellow:
    print('зеленый')
else:
    print('ошибка цвета')