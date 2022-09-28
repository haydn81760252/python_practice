kol_vo = int(input())
ostatok = kol_vo % 10

if 10 < kol_vo < 20:
    okoncanie = 'korov'
elif 5 <= ostatok <= 9:
    okoncanie = 'korov'
elif ostatok == 0:
    okoncanie = 'korov'
elif ostatok == 1:
    okoncanie = 'korova'
else:
    okoncanie = 'korovy'
print(kol_vo, okoncanie)
