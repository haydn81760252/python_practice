n = int(input())
total = 0
ostatok = n
while ostatok != 0:

    if ostatok >= 25:
        total += 1
        ostatok -= 25
    elif ostatok >= 10:
        total += 1
        ostatok -= 10
    elif ostatok >= 5:
        total += 1
        ostatok -= 5
    elif ostatok >= 1:
        total += 1
        ostatok -= 1
print(total)
