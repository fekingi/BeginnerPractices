def mükemmel(sayi):
    toplam = 0
    for i in range(1,sayi):
        if sayi%i == 0:
            toplam+=i
    return toplam == sayi

for i in range(1,1001):
    if(mükemmel(i)):
        print("Mükemmel sayi: ", i)