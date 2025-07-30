print(""" 
*********************
Hesaba Giriş Programi
*********************
""")

sys_Kullaniciadi = "fekingi"
sys_Parola = "12345678"
giriş_hakki = 3

while True:
    kullaniciAdi = input("Kullanici adi: ")
    parola = input("parola: ")
    if(kullaniciAdi != sys_Kullaniciadi and parola != sys_Parola):
        print("Kullaniciadi ve parola yanliş...")
        giriş_hakki -= 1
    elif(kullaniciAdi == sys_Kullaniciadi and parola != sys_Parola):
        print("parola yanliş...")
        giriş_hakki -= 1
    elif(kullaniciAdi != sys_Kullaniciadi and parola == sys_Parola):
        print("kullaniciadi yanliş...")
        giriş_hakki -= 1
    else: 
        print("sisteme giriş yapiliyor")
        break
    if(giriş_hakki == 0):
        print("giriş hakkiniz bitti...")
        break 