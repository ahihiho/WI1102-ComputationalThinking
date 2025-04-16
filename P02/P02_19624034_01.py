"""
NIM/Nama   : 19624034/Ghaisan Nufail
Tanggal    : 31/10/2024
Deskripsi  : Mencari banyak angka yang dapat dibagi oleh satuannya
"""

#KAMUS
# a, b, count  : integer

#ALGORITMA
##input
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))

##proses
count = 0 # inisialisasi counter 
for i in range (a, b+1): # loop dari nilai a hingga nilai b
    if i % 10 != 0:      # syarat : digit terakhir bukan nol
        if i %(i%10)==0: # sifat  : bilangan habis dibagi digit akhir
         count +=1 

##output
print(f"Terdapat {count} angka yang memenuhi sifat tersebut. ")

#Selesai :D
