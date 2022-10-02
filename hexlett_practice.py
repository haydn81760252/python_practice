stark = 'Arya'

# BEGIN (write your solution here)
text = f'''Do you want to eat, {stark}?
Yes, I'm hungry, mom.'''
print(text)

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


text = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
print(len(text[5:16].strip()))


# END

#
# def run():
#     return 5
#     return 10
#
#
# # Что будет выведено на экран?
# print(run())


def get_last_char(text):
    return text[-1]


print(get_last_char('Chaos'))


def truncate(string, number):
    stroka = (string[:number]) + '...'
    return stroka

stroka = input("Введите строку для обрезки:\n")
print(truncate(stroka, 2))
