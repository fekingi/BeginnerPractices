def ekok(a,b):
    i = 2
    ekok = 1
    while True:
        if a%i == 0 and b%i == 0:
            ekok *= i
            a //=i
            b //=i
        elif a%i== 0 and b%i != 0: 
            ekok *= i
            a //=i
        elif a%i != 0 and b%i == 0:
            ekok *= i
            b //=i
        else: 
            i += 1
        if a == 1 and b == 1:
            break
    return ekok 
sayi1 = int(input("1.sayiyi girin: "))
sayi2 = int(input("2.sayiyi girin: "))
print("İki sayinin ekoku: ", ekok(sayi1,sayi2))



"""def ekok(a,b):
    okek = 1
    i = 1
    j = 1
    while (i*a!=j*b):
        if i*a < j*b:
            i+=1 
        elif j*b < i*a:
            j+=1
    else: 
        okek = a*i
    return okek 

sayi1 = int(input("birinci sayiyi giriniz: "))
sayi2 = int(input("ikinci sayiyi giriniz: "))

print("iki sayinin ekoku: ", ekok(sayi1, sayi2))"""