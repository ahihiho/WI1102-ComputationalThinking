"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 21/11/2024
DESKRIPSI  : Program yang menentukan jenis persamaan kuadrat berdasarkan nilai diskriminan
"""

#KAMUS
# diskriminan : fungsi
# persamaan_kuadrat : prosedur
# a, b, c, d : integer

#ALGORITMA
##fungsi diskriminan
def diskriminan(a, b, c):
    return float (b * b) - (4 * a * c)
     
##prosedur menentukan persamaan kuadrat
def persamaan_kuadrat(nilai_diskriminan):
    print("Persamaan kuadrat ", end="")
    if (nilai_diskriminan > 0):
        print("memiliki akar berbeda")
    elif (nilai_diskriminan < 0):
        print("tidak memiliki akar real")
    else:
        print("memiliki akar kembar")
        
##input
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

##proses 
d = diskriminan(a, b, c)

##output
print(f"Nilai diskriminan: {d:.2f}")
persamaan_kuadrat(d) 

#Selesai :D
