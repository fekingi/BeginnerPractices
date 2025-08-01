def ebob(a,b):
    i = 1
    obeb = 1

    while i <= a and i <= b:
        if not (a%i) and not (b%i):
            obeb = i
        i+=1
    return obeb
    
sayi1 = int(input("bir sayi girin: ")) 
sayi2 = int(input("bir sayi girin: "))

print("2 sayinin obebi:", ebob(sayi1,sayi2))

"""def ebob(a,b):
    abölen = []
    bbölen = []
    for i in range(1,a+1):
        if ( a%i == 0):
            abölen.append(i)
    
    for j in range(1, b+1):
        if( b%j == 0):
            bbölen.append(j)
    
    ortakbölen = []
    for eşya in abölen:
        if eşya in bbölen:
            ortakbölen.append(eşya)
            ortakbölen.sort()
    
    obeb = ortakbölen[-1]
    return obeb

sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))

print(ebob(sayi1,sayi2))"""
