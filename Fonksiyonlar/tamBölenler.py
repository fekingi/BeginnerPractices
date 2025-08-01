def tambölenler(sayi):
    Bölenler = []
    sayi = int(sayi)
    for i in range(1, sayi+1):
        if(sayi%i == 0):
            Bölenler.append(i)
    return Bölenler

while True:
    a = input("sayi giriniz: ")
    if (a =="q"):
        print("Programdan çikiliyor...")
        break
    else: 
        print("Tam Bölenler: ", tambölenler(a))