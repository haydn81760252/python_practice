a = int(input())
b = int(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif b == 0  and op == '/':
    print('На ноль делить нельзя!')
elif op == '/':
    print(a / b)
else:
    print('Неверная операция')