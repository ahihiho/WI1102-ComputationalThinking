#DESKRIPSI : Program yang menghasilkan output 10^x terkecil yang lebih besar dari nilai input

#KAMUS
# n, x : integer

#ALGORITMA
##input
n = int(input("Masukkan N: "))
x = 10

##proses
while x < n:
  x *= 10

print(x)

#Selesai :D
