n1, n2, n3 = int(input()), int(input()), int(input())

maximum = max(n1, n2, n3)
minimem = min(n1, n2, n3)


midd = n1 + n2 +n3 - maximum - minimem
print(maximum)
print(midd)
print(minimem)