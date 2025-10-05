"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 21/11/2024
DESKRIPSI  : Mencari sisa digit terkecil dari mesin ganjil - genap 
"""

#KAMUS
# n, proses, operasi : integer
# ganjil, genap : prosedur

#ALGORITMA
operasi = 0

##prosedur bilangan ganjil
def ganjil(x):
    global operasi
    operasi += 1
    n = str(x)[::-1]
    total = 0

    for i in range (len(n)): # proses menjumlahkan digit2 ganjil
        posisi = i + 1
        if posisi % 2 == 1:
            total += int(n[i])
        
    if total < 10:
        print(f"Mesin berhenti setelah {operasi} operasi, mengeluarkan angka {total}")
    else:
        genap(total)

##prosedur bilangan genap
def genap(x): 
    global operasi
    operasi += 1
    n = str(x)[::-1]
    total = 0

    for i in range (len(n)): # proses menjumlahkan digit2 genap
        posisi = i + 1
        if posisi % 2 == 0:
            total += int(n[i])
    
    if total < 10: 
        print(f"Mesin berhenti setelah {operasi} operasi, mengeluarkan angka {total}")
    else:
        ganjil(total)

##input
n = int(input("Masukkan biangan: "))
if n % 2 == 0:
    genap(n)
else:
    ganjil(n)

#Selesai :D
