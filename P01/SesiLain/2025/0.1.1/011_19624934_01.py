"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 29/09/2026
DESKRIPSI  : menghitung ukuran hasil kompresi gambar 
"""

#KAMUS
# l, t, dalam, rasio : integer

#ALGORITMA
##input
l     = int(input("Masukkan lebar gambar (pixel): "))
t     = int(input("Masukkan tinggi gambar (pixel): "))
dalam = int(input("Masukkan kedalaman warna (bit): "))
rasio = int(input("Masukkan rasio kompresi (persen): "))

##proses
ukuran_bit = l * t * dalam   # menghitung ukuran bit
ukuran_byte = ukuran_bit / 8 # konversi nilai bit ke byte
hasil_kompres = ukuran_byte * ((100-rasio)/100) # sisa akhir kompresi gambar
ukuran_mb = hasil_kompres / 1000000             # menghitung hasil akhir kompresi dalam Mb

##output
print("ukuran file gambar setelah kompresi adalah %.2f MB" % ukuran_mb)
# ALT1: print(f"ukuran file gambar setelah kompresi adalah {ukuran_mb : .2f} MB")
# ALT2: print("ukuran file gambar setelah kompresi adalah " + str(round(ukuran_mb, 2)) + " MB")

#Selesai :D
