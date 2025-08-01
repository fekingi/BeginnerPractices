def asalSayi(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return False
    else:
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
        return True
    
while True:
    sayi = input("bir sayi giriniz")
    if(sayi == "q"):
        break
    sayi = int(sayi)
    if(asalSayi(sayi)):
        print(sayi, "bir asal sayidir.")
    