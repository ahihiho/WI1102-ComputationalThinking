"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 17/10/2024
DESKRIPSI  : program menentukan nilai tukar terbesar
"""

#KAMUS
# peng, kom : float

#ALGORITMA
##input
peng  = float(input('Banyak uang Peng yang ditawarkan: '))
kom   = float(input('Banyak uang Kom yang ditawarkan: '))
peng *= float(input('Konversi mata uang Peng ke rupiah: ')) 
kom  *= float(input('Konversi mata uang Kom ke rupiah: '))

##proses + output
if peng > kom:
  print('Adik Tuan Leo memilih uang Peng.')
else: # uang Kom > uang Peng
  print('Adik Tuan Leo memilih uang Kom.')


#SEMANGAT 
