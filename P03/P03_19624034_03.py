"""
NIM/NAMA   : 19624034/GN
TANGGAL    : 21/11/2024
DESKRIPSI  : Program menentukan siapa yang akan lebih dahulu mencapai target kartu
"""
#KAMUS
# n, deb, sal, i, y : integer
# buat_arr : prosedur
# jumlah_arr : fungsi
# array_deb, array_sal : array of integer

#ALGORITMA
#prosedur buat array kartu
def buat_arr(x):
    return [ x//1000, (x//100)%10, (x//10)%10, x%10 ]

#fungsi menghasilkan jumlah array
def jumlah_arr(arr):
   total = 0
   for i in range (4):
       total += arr[i]
   return total

##input
n = int(input("Masukkan Target Poin: ")) # masukkan target poin
deb = int(input("Kartu Nona Deb: ")) # masukkan nilai kartu
sal = int(input("Kartu Nona Sal: ")) # masukkan nilai kartu
# membuat array kartu
array_deb = buat_arr(deb)
array_sal = buat_arr(sal)
i = 0 # inisialisasi nilai putaran

##proses
# loop selama jumlah array != nilai target
while jumlah_arr(array_deb) != n and jumlah_arr(array_sal) != n:
    i += 1
    x = input(f"Giliran {i} (tambah / tukar): ")
    y = int(input("Pada posisi kartu ke: "))
    if(x == "tambah"): # jika input tambah
        if(i % 2 == 0): # jika giliran kelipatan dua (giliran Nona Sal)
            array_sal[y] += 1
        else: # giliran Nona Deb
            array_deb[y] += 1
    elif(x == "tukar"): # jika input tukar
        temp_arr = array_deb[y]
        array_deb[y] = array_sal[y]
        array_sal[y] = temp_arr
        
##output
if jumlah_arr(array_deb) == n: # jika Nona Deb mencapai target
    print("Nona Deb Memenangkan permainan.")
else: # jika Nona Sal mencapai target
    print("Nona Sal Memenangkan permainan.")
    
#Selesai :D
