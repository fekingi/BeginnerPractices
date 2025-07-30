print("""****************************************
Girilen sayilari toplama

çikip sonucu görmek için "q"ya basin
****************************************
""")
toplam = 0
while True: 
    sayi = input("toplanacak sayilari girin: ")
    if(sayi == "q"):
        print("Sayilarin toplami: {}".format(toplam))
        break
    else:
        sayi = int(sayi)
        toplam += sayi