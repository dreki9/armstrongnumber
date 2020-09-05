sayi = input('Sayı giriniz: ')
liste = []
basamak_sayisi = 0
temp = sayi
toplam = 0
while True:
    temp = int(temp)
    temp //= 10
    basamak_sayisi += 1
    if temp < 1 :
        break
sayi = str(sayi)
for x in sayi:
    liste.append(x)
for i in liste:
    toplam += pow(int(i), basamak_sayisi)
if int(toplam) == int(sayi):
    print('Sayı Armstrong sayıdır.')
else:
    print('Sayı Armstrong değildir.')
