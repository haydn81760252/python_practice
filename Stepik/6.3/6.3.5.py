a = int(len(input()))
b = int(len(input()))
c = int(len(input()))

maximum = max(a, b, c)
minimum = min(a, b, c)
midd = a + b + c - maximum - minimum

if (midd - minimum) == (maximum - midd):
    print('YES')
else:
    print('NO')



