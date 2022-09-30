alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
stroka = input('Введите строку:\n')

for i in alphabet:
    count = 0
    for m in stroka:
        if i == m:
            count += 1
    if count > 0:
        print('Кол-во букв ', i, ' было ', count)
