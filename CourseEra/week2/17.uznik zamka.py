a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)


if (d >= a and e >= b) or (d >= b and e >= a):
    print("YES")
elif (d >= a and e >= c) or (d >= c and e >= a):
    print("YES")
elif (d >= b and e >= c) or (d >= c and e >= b):
    print("YES")
else:
    print('NO')
