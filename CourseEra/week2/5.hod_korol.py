stlb1 = int(input())
str1 = int(input())
stlb2 = int(input())
str2 = int(input())
if stlb1 == stlb2 and str1 == str2:
    print('NO')
elif str1 == str2 and (stlb1 - 1 == stlb2 or stlb1 + 1 == stlb2):
    print('YES')
elif str1 + 1 == str2 and (stlb1 - 1 == stlb2 or stlb1 + 1 == stlb2):
    print('YES')
elif str1 - 1 == str2 and (stlb1 - 1 == stlb2 or stlb1 + 1 == stlb2):
    print('YES')
else:
    print('NO')

