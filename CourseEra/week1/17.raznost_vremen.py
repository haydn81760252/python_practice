hr1 = int(input())
min1 = int(input())
sec1 = int(input())
hr2 = int(input())
min2 = int(input())
sec2 = int(input())

hr1 *= 3600
min1 *= 60
hr2 *= 3600
min2 *= 60
print((hr2+min2+sec2) - (hr1+min1+sec1))

# print((hr1+min1+sec1))
# print((hr2+min2+sec2))
