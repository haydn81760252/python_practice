a = int(input())
ost = a % 10
if 10 < a < 20:
    print('Коров')
if 5 <= ost <= 9:
    print('Коров')
elif ost == 1:
    print('Корова')
else:
    print('High')