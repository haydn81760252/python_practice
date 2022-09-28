n = int(input())

t = n // 1000
sot = n // 100 % 10
des = n // 10 % 10
ed = n % 10

if t + ed == sot - des:
    print('ДА')
else:
    print('НЕТ')
№ print(t, sot, des, ed)