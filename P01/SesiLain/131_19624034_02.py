"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 14/10/2024
DESKRIPSI : 
"""

#KAMUS
# n  : integer
# tv : string

#ALGORITMA
##input
n = int(input("Jumlah perangkat Tuan Mik dan teman-temannya:"))
tv = input("Apakah ingin akses ke TV Channel?(Ya atau Tidak): ")

if (n <= 3) and (tv == "Tidak"):
  print("Tuan Mik akan memesan 1 Paket A dengan total harga 250 ribu")
elif (n > 3 and n < 7) or (tv =="Ya"):
  print("Tuan Mik akan memesan 1 Paket B dengan total harga 375 ribu")
elif ( n >= 7 and n <= 12):
  print("Tuan Mik akan memesan 1 Paket C dengan total harga 600 ribu")
elif (n > 12):
  n = n/12
  if (n > 1 and n % 12 == 0):
    print(f"Tuan Mik akan memesan {n} Paket C dengan total harga", (600*n), "ribu")
  
