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
n = int(input("Jumlah perangkat Tuan Mik dan teman-temannya: ")) # banyak perangkat
tv = input("Apakah ingin akses ke TV Channel?(Ya atau Tidak): ") 

##proses
# Paket C lebih murah dari 2 Paket B dan lebih murah dari 4 Paket A
if (n>=7): # Jika perangkat >= 7 
   if(n<= 12 or n % 12 == 0):
      if (n <= 12): # Jika >= 7 namun < 13
         print(f"Tuan Mik akan memesan 1 Paket C dengan total harga 600 ribu")
      else: # jika kelipatan 12 
         print(f"Tuan Mik akan memesan {int(n//12)} Paket C dengan total harga {int((n//12)*600)} ribu")
   elif(n % 12 <= 3): # jika jumlah perangkat 12 + 1/2/3
      print(f"Tuan Mik akan memesan 1 Paket A dan {int(n//12)} Paket C dengan total harga {int((n//12)*600+250)} ribu")
   else: # jika jumlah perangkat 12, 4++ 
      print(f"Tuan Mik akan memesan 1 Paket B dan {int(n//12)} Paket C dengan total harga {int((n//12)*600+375)} ribu")
elif (n <= 3) and (tv == "Tidak"): # Perangkat <= 3 dan tanpa akses TV
  print("Tuan Mik akan memesan 1 Paket A dengan total harga 250 ribu")
else: # (n > 3 and n < 7) or (n<= 3 and tv =="Ya")
  print("Tuan Mik akan memesan 1 Paket B dengan total harga 375 ribu")

#Selesai :D
