"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 21/11/2024
DESKRIPSI  : Program yang menentukan jenis persamaan kuadrat berdasarkan nilai diskriminan
"""

#KAMUS
# diskriminan : fungsi
# persamaan_kuadrat : prosedur
# a, b, c : integer
# d : float

#ALGORITMA
##fungsi diskriminan
def diskriminan(a, b, c):
    return float (b * b) - (4 * a * c) # mengembalikan nilai diskriminan
     
##prosedur menentukan persamaan kuadrat
def persamaan_kuadrat(nilai_diskriminan):
    print("Persamaan kuadrat ", end="")
    if (nilai_diskriminan > 0): # jika diskriminan lebih dari nol
        print("memiliki akar berbeda")
    elif (nilai_diskriminan < 0): # jika diskriminan kurang dari nol
        print("tidak memiliki akar real")
    else: # jika diskriminan = nol
        print("memiliki akar kembar")
        
##input
# masukkan nilai koefisien fungsi
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

##proses 
d = diskriminan(a, b, c) # memanggil fungsi diskriminan dan menyimpan nilai di d

##output
print(f"Nilai diskriminan: {d:.2f}") 
persamaan_kuadrat(d)  # memanggil prosedur menentukan jenis persamaan kuadrat

#Selesai :D
