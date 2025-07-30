print("""********************
Çarpim Tablosu 
********************
""")
for i in range(1,11):
    for y in range(1,11):
        i*y
        print("{} x {} = {}".format(i,y,i*y))