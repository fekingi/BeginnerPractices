sayi = input("sayi: ")
basamaksayisi = len(sayi)
basamak = 0
toplam = 0
sayi = int(sayi)

gecicisayi = sayi

while (gecicisayi > 0):
    basamak = gecicisayi % 10
    toplam += basamak**basamaksayisi
    gecicisayi //= 10

if(toplam == sayi):
    print("{} armstrong sayisidir.".format(sayi))
else:
    print("{} Armstrong sayisi degildir.".format(sayi))


""" a = input("bir sayi giriniz: ")
basamak = len(a)
toplam = 0 
for i in a:
    i = int(i)    
    toplam += i**basamak
if(toplam == int(a)):
    print("bu sayi armstrong sayisidir.")
else:
    print("normal bir sayi girdiniz")
"""    