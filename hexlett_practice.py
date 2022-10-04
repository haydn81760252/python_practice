# stark = 'Arya'

# BEGIN (write your solution here)
# text = f'''Do you want to eat, {stark}?
# Yes, I'm hungry, mom.'''
# print(text)

#
#
# magic = '\nyou'
# print(magic[1])
#
# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
#
# print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
#
# text = 'Hexlet'
#
# print(text[2::-1])
#
# date = '28-10-2022'
#
# print(date[3:5])

# value = 'Hexlet'
# print(value[2:5])
#
# print(value[-4:-1])

# result = sum_(sum_(1, 3), sum_(sum_(4, 2), 3))

# name = 'Tirion'
# print(name.replace('Ti', 'Ki').lower())  # => ?
# print(name[1:5].upper().find('I'))


# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
#
# # BEGIN (write your solution here)
# print(len(text[5:16].strip()))


# END

#
# def run():
#     return 5
#     return 10
#
# #
# # # Что будет выведено на экран?
# # print(run())
#
#
# def get_last_char(text):
#     return text[-1]
#
#
# print(get_last_char('Chaos'))
#
#
# def truncate(string, number):
#     stroka = (string[:number]) + '...'
#     return stroka
#
# stroka = input("Введите строку для обрезки:\n")
# print(truncate(stroka, 2))


# # Кредитка передается внутрь как строка
# get_hidden_card('2034399002121100', 1)  # "*1100"
#
# get_hidden_card('123456781234567', 2)  # "**5678"
#
# get_hidden_card('1234567812345678', 3)  # "***5678"
#
# get_hidden_card('1234567812345678')     # "****5678"
#
# card_number = '1234123412341234'

#
# # number_of_digits = 10
# def get_hidden_card(card_number, number_of_digits=4):
# #    result = '*' * number_of_digits + card_number[12:16]
#     result = '*' * number_of_digits + card_number[:4]
#     return result
#
#
# print(get_hidden_card(card_number))

text = 'python'


#
# trim_and_repeat(text, offset=3, repetitions=2)  # honhon
#
# trim_and_repeat(text, repetitions=3)  # pythonpythonpython
#
# trim_and_repeat(text)  # python

# def trim_and_repeat(text, offset=0, repetitions=1):
#     return text[offset:] * repetitions
#     #return result
#
# print(trim_and_repeat(text))

# def get_age_difference(age1, age2):
#  #   result = 'The age difference is ' + str(age2 - age1)
#     return 'The age difference is ' + str(abs(age2 - age1))
#
# print(get_age_difference(2020, 2010))

# def has_upper_case(string):
#     return string != string.lower()
#
# print(has_upper_case('Hexlet'))

# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
#
# print(is_leap_year(2018))


# def string_or_not(value):
#     return isinstance(value, str) and 'Yes' or 'No'
#
# print(string_or_not(3))

#
# def normalize_url(url):
#     http_string = url[:7]
#     if http_string == 'https:/':
#         http_string_normal = url
#     elif http_string == 'http://':
#          http_string_normal = 'https://' + url[7:]
#     else:
#         http_string_normal = 'https://' + url
#     return http_string_normal
#
#     'https://' + url[7:] if url[:7] == 'https:/' else 'https://' + url:


# print(normalize_url('https://ya.ru'))
# print(normalize_url('google.com'))
# print(normalize_url('http://ai.fi'))
#
# print(normalize_url('https://yandex.ru'))
#
# a = 4
# a -= 8 - a
#
# print(a)
#
# a = 5
#
# a -= 4
#
# a += 1
#
# print(a)


# print_numbers(4)

# => 4
# => 3
# => 2
# => 1
# => finished!

# def print_numbers(number):
#     counter = number
#     while counter >= 1:
#         print(counter)
#         counter -= 1
#     print('finished!')
#
# print(print_numbers(4))
#
#
# join_numbers_from_range(1, 1)  # '1'
# join_numbers_from_range(2, 3)  # '23'
# join_numbers_from_range(5, 10)  # '5678910'

# def join_numbers_from_range(start, finish):
#     i = start
#     result = ''
#     while i <= finish:
#         result += str(i)
#         i += 1
#     return result
#
# # print(join_numbers_from_range(5,10))
#
# text = 'Haydn'
# print(text[::-1])


# string = 'If I look back I am lost'
# print(my_substr(string, 1))  # => 'I'
# print(my_substr(string, 7))  # => 'If I lo'

# def my_substr(string, count):
#     i = 0
#     one_char = string
#     result_string = ''
#     while i < count:
#         result_string += one_char[i]
#         i += 1
#     return result_string
#
# string = 'If I look back I am lost'
# print(my_substr(string, 7))

# def is_contains_char(string, char):
#     string_low, char_low = string.lower(), char.lower()
#     i = 0
#     while i < len(string):
#         #         if char_low == string_low[i]:
#         if char.lower() == string[i].lower():
#             return True
#         i += 1
#     return False
#
#
# # print(is_contains_char('Hexlet', 'H'))
# print(is_contains_char('Awesomeness', 'm'))

def sum(numbers):
    result = 0
    for num in numbers:
        result += int(num)
    return result

print(sum("12345"))