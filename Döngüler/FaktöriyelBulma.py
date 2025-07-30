print("""***************
Faktöriyel Bulma 
      
Programdan çikmak için 'q' basiniz
***************
""")



while True:
    sayi = input("bir sayi giriniz: ")
    if ( sayi == "q" ):
        print("programdan çikiliyor...")
        break
    else: 
        faktöriyel = 1
        sayi = int(sayi)
        for i in range(2,sayi +1):
            faktöriyel *= i 
        print("faktöriyel: ", faktöriyel)
        



