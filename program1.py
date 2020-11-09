a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a > b and a > c:
 print("Bilangan terbesar adalah ", a)
elif b > a and b > c:
    print("Bilangan terbesar adalah ", b)
elif c > a and c > b:
    print("Bilangan terbesar adalah ", c)
else:
 print("Bilangan nya setara")
