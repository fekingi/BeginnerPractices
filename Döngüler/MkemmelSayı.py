print("""******************************
Mükemmel sayi bulma programi

Çikiş yapmak için 0'i tuşlayin
******************************
""")
sayı1 = int(input("Sayı1:"))

i = 1
toplam = 0
while (i < sayı1):
    if (sayı1 % i == 0):
        toplam += i
    i += 1

if (toplam == sayı1):
    print(sayı1, "mükemmel bir sayıdır.")
else:
    print(sayı1, "mükemmel bir sayı değildir.")

"""   
while True: 
    a = int(input("bir sayi giriniz: "))
    toplam = 0 
    
    if (a == 0):
        break 

    for i in range(1, a):
        if (a%i == 0):
            toplam += i
            if(toplam == a):
                print("{} sayisi mükemmel bir sayidir.".format(a))
"""