#программа переворачивает строку

string = input('Введите строку для переворота:\n')
print('Перевернутая строка:\n', string[::-1])

#попробую реализовать функцию циклом for сам
def string_reverse(text):
    result_string = ''
    for i in range(len(text)-1, -1, -1):
        result_string += text[i]
    return result_string

#print(string_reverse('Привет!'))
print(string_reverse(string))

#попробую через while
def string_reverse_while(text):
    result_string =''
    i = len(text) - 1
    while i > 0:
        result_string += text[i]
        i += 1
    return result_string

print(string_reverse(string))


