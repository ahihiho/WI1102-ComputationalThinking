#DESKRIPSI : Menentukan banyaknya lompatan katak berdasarkan koordinat awal

#KAMUS
# n, a, b : integer

#ALGORITMA
##input
n = int(input("Masukkan koordinat katak: ")) # nilai awal koordinat
a = int(input("Masukkan panjang lompatan katak ke kanan: ")) # jumlah lompatan ke kanan
b = int(input("Masukkan panjang lompatan katak ke kiri: "))  # jumlah lompatan ke kiri

##proses
if (n < 0 and n % 3 == 0): # koordinat negatif dan kelipatan tiga
    n = n + (a - b) * b
    print(n)
elif(n%2 == 1): # koordinat awal ganji
    n = n + (a - b) * a
    print(n)
else: # koordinat genap atau negatif selain kelipatan tiga
    k = a * b
    if (k%2 == 0):
        n = n + (a - b) * k/2
    else:
         n = n + ((a - b) * (k//2)) + a
    print(n)

#Selesai :D
