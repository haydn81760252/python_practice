kolvoSekund = int(input())
hr = kolvoSekund % 86400 // 3600
min = (kolvoSekund % 86400) % 100 % 60
sek = kolvoSekund % 86400 % 60
proverka_min = hr % 10



print(hr, min, sek, sep =':')
print(proverka_min)
#print(kolvoSekund % 86400 // 3600, kolvoSekund % 86400 % 60, sep = ':')
# минут в сутках 1440
