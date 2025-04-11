"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 17/10/2024
DESKRIPSI  : Program menentukan banyak pelari yang terkualifikasi dan hadiah yang diperoleh
"""

#KAMUS
# n, t, leo, sal, deb : integer

#ALGORITMA
##input
# soal hanya meminta input bilangan bulat
n   = int(input("Masukkan nilai N: ")) # total hadiah yang ada
t   = int(input("Masukkan nilai T: ")) # total waktu maksimum kualifikasi
leo = int(input("Masukkan waktu lari Tuan Leo: ")) # waktu lari Tuan Leo
sal = int(input("Masukkan waktu lari Nona Deb: ")) # waktu lari Nona Deb
deb = int(input("Masukkan waktu lari Nona Sal: ")) # waktu lari Nona Sal

##proses + output
if (leo <= t and sal <= t and deb <= t): # jika semua memenuhi waktu yang ditentukan
    hadiah = n / 3
    print(f"Terdapat 3 peserta yang terkualifikasi dan masing-masing akan mendapatkan {hadiah} dollar kompeng.")
elif (leo <= t and (sal <= t or deb <= t) or sal <= t and deb <= t): # jika hanya dua yang berhasil menenmpuh sesuai/kurang dari waktu
    hadiah = n / 2
    print(f"Terdapt 2 peserta yang terkualifikasi dan masing-masing mendapatkan {hadiah} dollar kompeng.")
elif (leo <= t or sal <= t or deb <= t): # jika hanya satu yang terkualifikasi
    print(f"Terdapt 1 peserta yang terkualifikasi dan masing-masing mendapatkan {n} dollar kompeng.")
else: # tidak ada yang lolos
    print(f"Tidak ada peserta yang terkualifikasi.")

#Selesai:D
