"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 17/10/2024
DESKRIPSI : Menentukan apakah Tuan Leo untung dan dapat membeli barang baru
"""

#KAMUS
# hBeli, hJual, h, tabung : integer

#ALGORITMA
##input
hBeli   = int(input("Masukkan harga beli barang yang akan dijual: "))
hJual   = int(input("Masukkan harga jual barang yang akan dijual: "))
h       = int(input("Masukkan harga barang yang ingin dibeli: "))
tabung  = int(input("Masukkan tabungan Tuan Leo: "))

##proses
if(hBeli < hJual):
  tabung += hJual
  if(tabung > h):
    print("Tuan Leo dapat membeli barang yang diinginkan.")
  else:
    print("Tuan Leo tidak dapat membeli barang yang diinginkan.")
else:
  print("Tuan Leo tidak dapat membeli barang yang diinginkan.")

#Selesai :D
