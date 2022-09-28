n1 = input()
n2 = input()
n3 = input()

l1 = len(n1)
l2 = len(n2)
l3 = len(n3)

maximum = max(l1, l2, l3)
minimum = min(l1, l2, l3)

if minimum == l1:
    print(n1)
elif minimum == l2:
    print(n2)
else:
    print(n3)
if maximum == l1:
    print(n1)
elif maximum == l2:
    print(n2)
else:
    print(n3)

