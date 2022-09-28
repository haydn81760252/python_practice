a = int(input())
b = int(input())
c = int(input())
d = int(input())
minimum = 0

if a < b:
    minimum = a
else:
    minimum = b
if c < minimum:
    minimum = c
if d < minimum:
    minimum = d
print(minimum)
