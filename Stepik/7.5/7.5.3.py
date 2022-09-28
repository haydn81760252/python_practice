n = int(input())
minimum, maximum = n, 0
while n != 0:
    last_digit = n % 10
    if last_digit > maximum:
        maximum = last_digit
    if last_digit < minimum:
        minimum = last_digit
    n //= 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)
