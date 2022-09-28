rubl = int(input())
kop = int(input())
kolVo = int(input())

cost = (rubl * 100) + kop
print(cost * kolVo // 100, cost * kolVo % 100)
