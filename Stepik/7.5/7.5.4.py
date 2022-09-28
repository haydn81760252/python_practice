n = int(input())
summa, kolvo, umn, sr_arifm, first_digit, sum_first_last = 0, 0, 1, 0, 0, 0
last_digit2 = n % 10
while n != 0:
    last_digit = n % 10
    # first_digit = n % 10
    summa += last_digit
    kolvo += 1
    umn *= last_digit
    n //= 10

print(summa)
print(kolvo)
print(umn)
print(summa / kolvo)
print(last_digit)
print(last_digit + last_digit2)
