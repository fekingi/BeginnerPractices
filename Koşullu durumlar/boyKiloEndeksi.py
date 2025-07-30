print("""**********
Boy Kilo Endeksi
**********
""")

a = float(input("Kilo: "))
b = float(input("Boy: "))
bki = a / b**2
if (bki < 18.5):
    print("Zayıf")
elif(18.5 < bki < 25):
    print("normal")
elif(25 <bki < 30):
    print("Fazla kilolu")
else: 
    print("obez")