a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if d > e:
    (d, e) = (e, d)

if b > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)


if d >= a and e >= b:
    print("YES")
elif (d >= b and e >= c) or (d >= c and e >= b):
    print("YES")
else:
    print('NO')
