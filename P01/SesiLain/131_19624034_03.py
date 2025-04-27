"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 14/10/2024
DESKRIPSI : 
"""

#KAMUS
# o, h, u, ukurO, ukurH, ukurU : integer

#ALGORITMA
##input
o = int(input("Banyak barang oranye: ")) # 
h = int(input("Banyak barang hijau: "))  # 
u = int(input("Banyak barang ungu: "))   # 
ukurO = int(input("Ukuran barang oranye (unit): ")) # 
ukurH = int(input("Ukuran barang hijau (unit): "))  # 
ukurU = int(input("Ukuran barang ungu (unit): "))   # 

##proses
totalO = o * ukurO
totalH = h * ukurH
totalU = u * ukurU

if (totalO > 30):
  o = totalO % 2 + totalO // 2
  totalO = o * ukurO
