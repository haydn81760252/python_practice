n = int(input())
flag = True
#last_d = n % 10
while n != 0:
  last_d = n % 10
  pred_d = n % 100 //10
  if pred_d <= last_d:
      flag = False
  n //= 10
print(flag)
