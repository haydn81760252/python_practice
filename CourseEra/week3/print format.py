#x = 0.1
#print('{0:.25f}'.format(x))

if 0.1 + 0.2 == 0.3:
    print('YES')
else:
    print('NO')

x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')