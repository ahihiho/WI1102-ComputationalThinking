"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 17/10/2024
DESKRIPSI : Program menentukan bilangan biasa, unik, dan super unik
"""

#KAMUS
# bil, a1, a2, a3, a4 : integer

#ALGORITMA
##input
bil = int(input("Masukkan sebuah bilangan: "))

##proses
# menentukan digit bilangan
a1 = bil // 1000      # digit ke 1 (ribuan)
a2 = bil // 100 % 10  # digit ke-2 (ratusan)
a3 = bil // 10 % 10   # digit ke-3 (puluhan)
a4 = bil % 10         # digit ke-4 (satuan)

# menentukan apakah memenuhi kriteria bilangan unik
if ((a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4) and (a1 + a2 + a3 + a4) % 2 == 1): 
  if (a1 > a4 and bil % 2 == 0) or (a1 > a4 and a2 + a3 > a1) or (bil % 2 == 0 and a2 + a3 > a1): # menentukan apakah memenuhi kriteria super unik
    print("Bilangan tersebut adalah bilangan Super Unik.")
  else: # bilangan unik
    print("Bilangan tersebut adalah bilangan Unik.")
else: # tidak memenuhi kriteria (bilangan biasa)
  print("Bilangan tersebut adalah bilangan Biasa.")
      
#Selesai :D
