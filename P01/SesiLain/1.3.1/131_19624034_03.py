"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 14/10/2024
DESKRIPSI : 
"""

#KAMUS
# o, h, u, ukur_o, ukur_h, ukur_u : integer

#ALGORITMA
##input
o = int(input("Banyak barang oranye: ")) # 
h = int(input("Banyak barang hijau: "))  # 
u = int(input("Banyak barang ungu: "))   # 
ukur_o = int(input("Ukuran barang oranye (unit): ")) # 
ukur_h = int(input("Ukuran barang hijau (unit): "))  # 
ukur_u = int(input("Ukuran barang ungu (unit): "))   # 

##proses
total_o = o * ukur_o
total_h = h * ukur_h
total_u = u * ukur_u

if (totalO > 30):
  o = o % 2 + o // 2
  total_o = o * ukur_o

if (total_o > 30): 
  print("Barang oranye tidak cukup untuk disimpan")
  
elif (total_o > 20):
  print("Barang oranye disimpan di Container Kuning")
  if(total_h < 35):
    print("Barang oranye disimpan di Container Biru")
    if(total_u <= 20):
      print("Barang oranye disimpan di Container Merah")
    else:
      u = u % 2 + u // 2
      total_u = u * ukur_u
      if total_u <= 20: 
        print("Barang oranye disimpan di Container Merah")
      else: 
        print("Barang hijau tidak cukup untuk disimpan")
  else:
     h = h % 2 + h // 2
     total_h = h * ukur_h
    if (total_h < 35):
     print("Barang oranye disimpan di Container Biru")
else:
print("Barang oranye disimpan di Container Merah")
 
# Nanti di update yaw :D
