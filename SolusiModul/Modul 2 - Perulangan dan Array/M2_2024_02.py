#DESKRIPSI : Program loop membentuk segitiga integer dari 1 hingga n 

#KAMUS
# n : integer

#ALGORITMA
##input
n = int(input("Masukkan N: "))

##proses
for i in range (n):
    for i in range (i+1):
        print(i+1, end=" ")
    print("")

#Selesai :D
