# program cari inputan terbesar

#ambil inputan
num1 = float(input("masukan nilai pertama: "))
num2 = float(input("masukan nilai kedua: "))
num3 = float(input("masukan nilai ketiga: "))

if (num1 >= num2) and (num1 >= num3):
    besar = num1
elif (num2 >= num1) and (num2 >= num3):
    besar = num2
else:
    besar = num3

print("bilangan terbesar dari",num1,num2,"dan",num3,"adalah: ",besar)


