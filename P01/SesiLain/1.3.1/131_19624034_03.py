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
  o = o % 2 + o // 2
  totalO = o * ukurO

if (totalO > 30): 
  print("Barang oranye tidak cukup untuk disimpan")
  
elif (totalO > 20):
  print("Barang oranye disimpan di Container Kuning")
  if(totalH < 35):
    print("Barang oranye disimpan di Container Biru")
    if(totalU <= 20):
      print("Barang oranye disimpan di Container Merah")
    else:
      u = u % 2 + u // 2
      totoalU = u * ukurU
      if totalU <= 20: 
        print("Barang oranye disimpan di Container Merah")
      else: 
        print("Barang hijau tidak cukup untuk disimpan")
  else:
     h = h % 2 + h // 2
     totalH = h * ukurH
    if (totalH < 35):
     print("Barang oranye disimpan di Container Biru")
else:
print("Barang oranye disimpan di Container Merah")
 
# Nanti di update yaw :D
