print("******* PROGRAM 1*******")
print("Program menghitung laba dengan modal 100.000.000")
print("")
print("Note:")
print("Bulan pertama dan ke 2 = 0%")
print("Pada bulan ke 3 = 1%")
print("Pada bulan ke 5 = 5%")
print("pada bulan ke 8 = 2%")
print("")

a = 100000000
total = 0
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        total += b
        print("Laba bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        total += c
        print("Laba bulan ke-",x," : ",c)
    if(x>=5 and x<=7):
        d = a*0.5
        total += d
        print("Laba bulan ke-",x," : ",d)
    if(x==8):
        e = a*0.2
        total += e
        print("Laba bulan ke-",x," : ",e)
print("\Total : ",total)