import math
"""*************************
Hesap Makinesi

1. Toplama
2. Çikarma
3. Çarpma
4. Bölme
5. Üs alma 
6. Karekök
7. faktöriyel bulma
8. kalan bulma
9. Mutlak değer
10. Logaritma ve Üstel İşlemler
11. Trigonometri fonksiyonlari
12. Sabitler

Çikiş yapmak için "q" basiniz. 
*************************
"""

a = input("Yapmak istediğiniz işlemi giriniz: ")

while True:
    if a == "1":
        b = []
        while True:
            c = input("Toplamak istediğiniz sayilari girin: ")
            print("sonucu görmek için t'ye basin")
            if c == "t":
                break
            c = int(c)
            b.append(c)
        print("sayilarin toplami: ", sum(b))
    elif a == "2":
        sayi1 = int(input("İlk sayi: "))
        sayi2 = int(input("ikinci sayi: "))
        sonuc = sayi1 - sayi2 
        print("Çikarma işleminin sonucu: ", sonuc)
    elif a == "3":
        sayi1 = int(input("İlk sayi: "))
        sayi2 = int(input("ikinci sayi: "))
        sonuc = sayi1 * sayi2 
        print("çarpma işleminin sonucu: ", sonuc)
    elif a == "4":
        sayi1 = int(input("pay: "))
        sayi2 = int(input("payda: "))
        sonuc = sayi1 / sayi2 
        print("bölme işleminin sonucu: ", sonuc)
    elif a =="5":
        print("üs alma işlemi için değerleri girin.")
        sayi1 = int(input("üssü alinacak sayi: "))
        sayi2 = int(input("üs: "))
        print("sonuç: ", math.pow(sayi1,sayi2))
    elif a == "6":
        sayi1 = int(input("karekökü alinacak sayi: "))
        print("karekökün sonucu: ", math.sqrt(sayi1))
    elif a == "7":
        sayi1 = int(input("hangi sayinin faktöriyelini bulmak istiyorsunuz: "))
        print("{}'nin faktöriyeli: ".format(sayi1), math.factorial(sayi1) )
    elif a == "8":
        print("hangi iki sayidan kalani bulmak istiyorsunuz?")
        sayi1 = int(input("bölünen : "))
        sayi2 = int(input("bölen : "))
        print("bölümden kalan: ", math.fmod(sayi1, sayi2))
    elif a == "9":
        sayi1 = int(input("mutlak değerini bulmak istediğiniz sayi: "))
        print("sayinin mutlak değeri: ", math.fabs(sayi1))
    elif a == "10":
        print("""hangi işlem
              1. Doğal logaritma (e tabanli)
              2. Belirtilen tabanda logaritma
              3. 10 tabaninda logaritma
              4. e^x hesabi
              
              çikiş için k""")
        islem = input("yapmak istediğiniz islem: ")
        if islem == "1":
            sayi1 = int(input("logaritmasi alinacak sayi: "))
            print("sonuç: ", math.log(sayi1))
        elif islem == "2":
            sayi1 = int(input("verilecek tabana göre logaritmasi alinacak sayi:")) 
        elif islem == "3":
            sayi1 = int(input("10 taban'na göre logaritmasi alinacak sayi:"))
            print("sonuç: ", math.log10(sayi1))
        elif islem == "4":
            sayi1 = int(input("e'nin kaçinci üssünü bulmak istiyorsun: "))
            print("sonuç: ", math.exp(sayi1))
        elif islem == "k":
            break