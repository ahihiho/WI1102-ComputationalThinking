"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 17/10/2024
DESKRIPSI  : program memperbaiki posisi digit harga 
"""

#KAMUS
# d, p1, p2 : integer
# harga, hargaBaru : string

#ALGORITMA
##input
d     = int(input("Masukkan jumlah digit harga: "))
harga = input("Masukkan harga: ") 
p1    = int(input("Masukkan posisi angka pertama yang akan ditukar: "))
p2    = int(input("Masukkan posisi angka kedua yang akan ditukar: "))

##proses + output
#  tanpa menggunakan len
if (int(harga) * 10 // 10**d <= 10) and (int(harga) * 10 // 10**d >= 1 ): # memastikan digit = harga (digit nol yang mendahului angka bukan nol = tidak dianggap)
    if p1 > p2: # memastikan bahwa p1 selalu lebih kecil dari p2 
        p1, p2 = p2, p1
    a = harga[p1-1]
    b = harga[p2-1] 
    hargaBaru = (harga[:p1-1] + b + harga[p1:p2-1] + a + harga[p2:]) 
    print("Harga setelah diperbaiki: " + hargaBaru)

else: # harga != digit
    print("Masukan harga tidak valid")

#Selesai :D

#NB : codingan ini dibuat sebisa mungkin menyesuaikan materi modul 1
