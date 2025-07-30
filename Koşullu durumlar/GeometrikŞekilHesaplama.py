print("""********
Geometrik Şekil Hesaplama
********

Şekiller:

1. Üçgen
2. Dörtgen
""")

şekil = input("Hesaplamak istediğin şeklin numarasi: ")

if( şekil == "1"): 
    a = float(input("Birinci kenar uzunluğu: "))
    b = float(input("ikinci kenar uzunluğu: "))
    c = float(input("üçüncü kenar uzunluğu: "))
    if(abs(b-c) < a < b+c and abs(a-c)< b < a+c and abs(a-b) < c < a+b):
        if( a == b and b == c):
            print("Eşkenar üçgen")
        elif(a == b or b == c or a == c):
            print("ikizkenar üçgen")
        else: 
            print("siradan üçgen")
    else:
        print("Üçgen belirtmiyor")       
elif( şekil == "2"):
    a1 = float(input("Birinci kenar uzunluğu: "))
    b1 = float(input("ikinci kenar uzunluğu: "))
    c1 = float(input("üçüncü kenar uzunluğu: "))
    d1 = float(input("dördüncü kenar uzunluğu gir: "))
    if( a1 == b1 and b1 == c1 and c1 == d1):
        print("dörtgen bir Karedir")
    elif( a1 == c1 and b1 == d1):
        print("dörtgen dikdörtgendir.")
    else:
        print("dörtgen siradan bir dörtgendir.")
else: 
    print(" Geçerli bir sayi giriniz..")