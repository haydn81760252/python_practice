n = int(input())

for i in range(2, n):
    if n % i == 0:
        break
    i += 1
print(i)
