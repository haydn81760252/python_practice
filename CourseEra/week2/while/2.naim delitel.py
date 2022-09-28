a = int(input())
i = a
naim = 0
while i != 1:
    if not a % i:
        naim = i
    i -= 1
print(naim)
