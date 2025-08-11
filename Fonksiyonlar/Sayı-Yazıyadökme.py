birler = ["", "bir","iki","üç","dört","beş","alti","yedi","sekiz","dokuz"]
onlar = ["", "on","yirmi","otuz","kirk","elli","atmiş","yetmiş","seksen","doksan"]

def sayiYazi(a):
    birler1 = a%10
    onlar1 = a//10
    return onlar[onlar1]+ " " +birler[birler1]

b = int(input("İki basamakli bir sayi giriniz: "))
print(sayiYazi(b)) 