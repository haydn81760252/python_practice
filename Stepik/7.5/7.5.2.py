n = int(input())
total = ''
while n != 0:
    last_digit = n % 10
    total = total + str(last_digit)
    n //= 10
print(total)