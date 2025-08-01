def TamBölenler(sayi):
    sayi = int(sayi)
    for i in range(1,sayi+1):
        if sayi%i == 0:
            print("Bu sayinin tam bölenleri: ", i)
        else:
            False

while True:
    a = input("bir sayi giriniz: ")
    if a =="q":
        break
    else:   
        TamBölenler(a)