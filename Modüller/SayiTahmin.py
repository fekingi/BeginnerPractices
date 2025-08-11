import time
import random

a = random.randint(1,40)
tahminHakki = 7

while True:
    b = int(input("Tahmininiz: "))
    if b < a:
        print("Sorgulama yapiliyor...")
        time.sleep(1)
        print("daha büyük bir sayi giriniz.")
        tahminHakki -=1 
        if tahminHakki == 0:
            print("tahmin hakkiniz bitti.")
            break
    elif b > a:
        print("Sorgulama yapiliyor...")
        time.sleep(1)
        print("daha küçük bir sayi giriniz.")
        tahminHakki -=1
        if tahminHakki == 0:
            print("tahmin hakkiniz bitti.")
            break
    elif a == b:
        print("Sorgulama yapiliyor...")
        time.sleep(1)
        print("Doğru tahmin ettiniz...")
        time.sleep(1)
        print("Programdan çikiliyor.")
        break
    else:
        print("geçersiz input.")
        break

