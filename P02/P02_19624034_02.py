"""
NIM/Nama   : 19624034/GN
Tanggal    : 31/10/2024
Deskripsi  : Mengubah pesan biasa menjadi rahasia *menggunakan append*
"""

#KAMUS
# n  : integer
# biasa, rahasia : list of character
# pesan, pesanRahasia : string

#ALGORITMA
##input
n       = int (input("Masukkan jumlah huruf pada kamus rahasia: ")) # input banyaknya huruf yang ingin diubah
biasa   = [] # list yang akan menyimpan huruf biasa
rahasia = [] # list yang akan menyimpan huruf rahasia

##proses 
for i in range(n):
    b = input(f"Masukkan huruf biasa ke-{i+1}: ")
    r = input(f"Masukkan huruf rahasia ke-{i+1}: ")
    # append: digunakkan untuk memasukkan elemen kedalam list!
    biasa.append(b)   # huruf biasa (b) dimasukkan ke list (biasa) 
    rahasia.append(r) # huruf rahasia (r) dimasukkan ke list (rahasia)

    
pesan = input("Masukkan pesan yang ingin diubah: ") # input pesan

## proses enkripsi pesan
pesanRahasia = "" # variable string kosong untuk menampung hasil pesan rahasia
for huruf in pesan: # loop yang membaca tiap character dalam string pesan
    for i in range(n):
        if huruf == biasa[i]: # jika char sama dengan huruf biasa
            pesanRahasia += rahasia[i] # huruf rahasia akan ditambah ke string pesanRahasia
            break # exit loop
    else: # huruf not equal dengan list huruf biasa
        pesanRahasia += huruf

##output
print(f"Pesan rahasia Nona Sal: \n{pesanRahasia}")

#Selesai :D
