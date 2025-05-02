"""
NIM/NAMA  : 19624034/GN
TANGGAL   : 17/10/2024
DESKRIPSI : Menentukan bilangan yang mengandung lingkaran pada digitnya
"""

#KAMUS
# n, d1, d2, d3, d4, jmlh, d1J, d2J : integer

#ALGORITMA
##input
n = int(input("Masukkan sebuah bilangan: "))

##proses
d1 = n // 1000       # digit pertama n
d2 = n // 100 % 10   # digit kedua n
d3 = n // 10 % 10    # digit ketiga n
d4 = n % 10          # digit keempat n

jmlh = d1 + d2 + d3 + d4 # jumlah keempat digit
d1J = jmlh // 10 # digit pertama dari jummlah n
d2J = jmlh % 10  # digit kedua dari jumlah n

if (d1 == 0 or d1 == 6 or d1 == 8 or d1 == 9) or (d2 == 0 or d2 == 6 or d2 == 8 or d2 == 9) or (d3 == 0 or d3 == 6 or d3 == 8 or d3 == 9) or (d4 == 0 or d4 == 6 or d4 == 8 or d4 == 9): # Apakah digit mengandung bilangan lingkar
  if (d1J == 0 or d1J == 6 or d1J == 8 or d1J == 9) or (d2J == 0 or d2J == 6 or d2J == 8 or d2J == 9): # Apakah digit jumlah mengandung bilangan lingkar
    print("Bilangan tersebut adalah bilangan Rizz.")
  else:
    print("Bilangan tersebut adalah bilangan Sigma.")
else: # Tidak mengandung bilangan lingkar
  if (d1J == 0 or d1J == 6 or d1J == 8 or d1J == 9) or (d2J == 0 or d2J == 6 or d2J == 8 or d2J == 9): # Apakah digit jumlah mengandung bilangan lingkar
    print("Bilangan tersebut adalah bilangan Ohio.")
  else:
    print("Bilangan tersebut adalah bilangan Skibidi.")

#Selesai :D
