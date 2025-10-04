"""
NIM/Nama   : 19624034/GN
Tanggal    : 31/10/2024
Deskripsi  : Game menentukan pemain dengan jumlah kue terbanyak
"""

#KAMUS
# n, pemain, ditunjuk, pemain_max, kiri, kanan, jarak, maks  : integer
# kue : array of integer
# kesatu : boolean

#ALGORITMA
##input
pemain  = int(input("Banyak pemain: ")) # input banyaknya pemain
n       = int(input("Banyak penunjukan: ")) # input banyaknya penunjukan
kue     = [0] * pemain # dibuat array dengan panjang (jumlah pemain)

##proses 
for i in range(pemain):
    kue[i] = (i % 3) + 1 # mengisi kue berurut [1, 2, 3, 1, ...] sepanjang pemain

# proses penunjukan
for i in range (n):
    ditunjuk = int(input(f"Orang ke-{i+1} yang ditunjuk: ")) - 1 # mengambil input dan menyesuaikan dengan indeks array
    
    jarak = kue[ditunjuk]    # banyaknya kue digunakan sebagai jarak dengan pemain lain
    kiri  = ditunjuk - jarak # posisi pemain kiri
    kanan = ditunjuk + jarak # posisi pemain kanan

    # memastikan indeks kiri >= 0 dan pemain di kiri memiliki kue minimal 1
    if kiri >= 0 and kue[kiri] > 0:
        kue[kiri] -= 1 # jumlah kue pemain di kiri dikurangi

    # memastikan indeks kanan <= pemain dan pemain di kanan memiliki kue minimal 1
    if kanan <= pemain - 1 and kue[kanan] > 0:
        kue[kanan] -= 1 # jumlah kue pemain di kanan dikurangi

    # memastikan kue pemain yang ditunjuk kurang dari 3
    if kue[ditunjuk] < 3:
        kue[ditunjuk] += 1 # Nona Deb memberi kue bonus kepada pemain yang ditunjuk

# cari pemain dengan kue tebanyak
maks = kue[0] # inisialisasi jumlah kue terbanyak ke posisi pemain 1 
for i in range(1, pemain):
    if kue[i] > maks: # jika ada pemain di urutan berikutnya yang memiliki kue lebih banyak
        maks = kue[i] # posisi maks dipindah

##output
# end="" : digunakan untuk menghilangkan new line output 
print(f"Orang yang memiliki kue terbanyak adalah orang ", end="")

# cek pemain yang memiliki jumlah kue = maks
kesatu = True
for i in range (pemain):
    if kue[i] == maks:
        # jika bukan pemain pertama yang disebut, output(", ")
        if not kesatu: 
            print(", ", end="")
        print(i + 1, end="") # mencetak posisi pemain yang memiliki jumlah kue = maks
        kesatu = False

print(".")

#Selesai :D
