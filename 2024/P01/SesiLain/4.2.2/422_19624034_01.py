"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 17/10/2024
DESKRIPSI  : program menentukan status nilai akhir
"""

#KAMUS
# n1, n2, n3, rata : float

#ALGORITMA
##input
n1    = float(input("Masukkan nilai kuis pertama: "))
n2    = float(input("Masukkan nilai kuis kedua: "))
n3    = float(input("Masukkan nilai kuis ketiga: ")) 
rata  = float((n1 + n2 + n3) / 3) # rata-rata ketiga nilai

##proses + output
if (rata >=  80):
  print('Tuan Leo mendapatkan nilai Lulus Memuaskan.')
elif (rata >= 70):
  print('Tuan Leo mendapatkan nilai Lulus.')
else: # rata2 < 70
  print('Tuan Leo mendapatkan nilai Tidak Lulus.')

#Selesai :D
