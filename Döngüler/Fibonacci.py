print("""********************
Fibonacci serisi
*******************
""")
a = 1
b = 1
fibonacci = [a,b]
sayi = int(input("fibonacci serisi için uzunluk giriniz: "))

for i in range(sayi):
    a,b = b,a+b
    print("a: {}, b: {}".format(a,b))
    fibonacci.append(b)
print(fibonacci)
    
    
    
