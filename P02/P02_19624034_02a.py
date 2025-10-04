"""
NIM/Nama   : 19624034/GN
Tanggal    : 31/10/2024
Deskripsi  : Mengubah pesan biasa menjadi rahasia
"""

#KAMUS
# n  : integer
# biasa, rahasia : array of character
# pesan, pesan_rahasia : string

#ALGORITMA
##input
n       = int (input("Masukkan jumlah huruf pada kamus rahasia: ")) # input banyaknya huruf yang ingin diubah
biasa   = [""] * n # array yang akan menyimpan huruf biasa (berukuran n)
rahasia = [""] * n # array yang akan menyimpan huruf rahasia (berukuran n)

##proses 
for i in range(n):
    biasa[i] = input(f"Masukkan huruf biasa ke-{i+1}: ")
    rahasia[i] = input(f"Masukkan huruf rahasia ke-{i+1}: ")
    

    
pesan = input("Masukkan pesan yang ingin diubah: ") # input pesan

## proses enkripsi pesan
pesan_rahasia = "" # variable string kosong untuk menampung hasil pesan rahasia
for huruf in pesan: # loop yang membaca tiap character dalam string pesan
    for i in range(n):
        if huruf == biasa[i]: # jika char sama dengan huruf biasa
            pesan_rahasia += rahasia[i] # huruf rahasia akan ditambah ke string pesanRahasia
            break # exit loop
    else: # huruf not equal dengan array huruf biasa
        pesan_rahasia += huruf

##output
print(f"Pesan rahasia Nona Sal: \n{pesan_rahasia}")

#Selesai :D
