#DESKRIPSI : Program menentukan bilangan bravo atau biasa

#KAMUS
# n, d1, d2, d3, d4 : integer

#ALGORITMA
##input
n = int(input("Masukkan sebuah bilangan: "))

##proses
d1 = n // 1000      # digit pertama
d2 = n // 100 % 10  # digit kedua 
d3 = n // 10 % 10   # digit ketiga
d4 = n % 10         # digit keempat
sum = d1 + d2 + d3 + d4

if (sum % d1 == 0 and sum % d2 == 0 and sum % d3 == 0 and sum % d4 == 0 ):
  print("Bilangan tersebut adalah bilangan Bravo.")
else:
  print("Bilangan tersebut adalah bilangan Biasa.")

#Selesai :D
