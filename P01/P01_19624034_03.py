"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 17/10/2024
DESKRIPSI : Program menentukan pesanan yang dapat diterima atau tidak
"""

#KAMUS
# kBe, kAy, kKu, cM, cB, cU, bahanM, bahanB, bahanU : integer

#ALGORITMA
##input
kBe = int(input("Masukkan jumlah pesanan gantungan kunci bebek: "))
kAy = int(input("Masukkan jumlah pesanan gantungan kunci ayam: "))
kKu = int(input("Masukkan jumlah pesanan gantungan kunci kupu-kupu: "))
cM  = int(input("Masukkan jumlah clay merah: "))
cB  = int(input("Masukkan jumlah clay biru: "))
cU  = int(input("Masukkan jumlah clay ungu: "))

##proses 
bahanM = kBe * 2 + kAy * 1 + kKu * 1 # menghitung clay merah yang digunakan
bahanB = kBe * 1 + kAy * 2 + kKu * 1 # menghitung clay biru yang digunakan
bahanU = kKu * 3                     # menghitung clay ungu yang digunakan
cM -= bahanM # menentukan sisa clay merah
cB -= bahanB # menentukan sisa clay biru

# tanpa menggunakan loop hitung jumlah clay ungu yang dapat dibuat
if (cM > cB and bahanU != 0): # jika bahan biru lebih sedikit kurangi dengan biru
  cM -= cB
  cU += cB*2
  cB -= cB
elif (cM < cB and bahanU != 0): # jika bahan merah lebih sedikit kurangi dengan merah
  cB -= cM 
  cU += cM*2
  cM -= cM
else: # tidak mengubah nilai
  cM = cM
  cB = cB
  
if(cM >= 0 and cB >= 0 and cU > bahanU): # Semua bahan cukup
  print("Pesanan dapat diterima oleh Nona Sal")
else:
  print("Pesanan tidak dapat diterima oleh Nona Sal")

#Selesai :D
