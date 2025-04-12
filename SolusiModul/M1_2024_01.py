#DESKRIPSI : Menentukan bilangan positif ganjil/genap, negatif, atau nol

#KAMUS
# n : integer

#ALGORITMA
##input
n = int(input("Masukkan nilai N: ")) # berdasarkan contoh sebelumnya input adalah bilangan integer

##proses + output
if (n>0): # apakah bilangan positif?
  if(n%2 == 0):
    print(n, "bilangan positif genap")
  else: # n mod 2 = 1
    print(n, "bilangan positif ganjil")
elif (n == 0): 
  print(n, "bilangan nol")
else: # bukan bilangan positif dan tidak sama dengan nol
  print(n, "bilangan negatif")

#Selesai :D
