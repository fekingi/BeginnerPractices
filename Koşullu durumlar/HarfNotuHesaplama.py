a = float(input("vize1 notunuzu giriniz: "))
b = float(input("vize2 notunuzu giriniz: "))
c = float(input("final notunuzu giriniz: "))

ortalama = 0.3*a + 0.3*b + 0.4*c

if( ortalama >= 90):
    print("AA")
elif(ortalama >= 85):
    print("BA")
elif(ortalama >= 80):
    print("BB")
elif(ortalama >= 75):
    print("CB")
elif(ortalama >= 70):
    print("CC")
elif(ortalama >= 65):
    print("DC")
elif(ortalama >= 60):
    print("DD")
elif(ortalama >= 55):
    print("FD")
else:
    print("FF")