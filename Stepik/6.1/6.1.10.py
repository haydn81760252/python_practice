n = int(input())

s = n //100
d = n // 10 % 10
ed = n % 10
maxim = max(s, d, ed)
minim = min(s, d, ed)
midd = s + d+ ed - maxim - minim

if maxim - minim == midd:
    print('Число интересное')
else:
    print('Число неинтересное')

# print(s, d, ed)