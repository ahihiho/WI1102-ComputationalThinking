#DESKRIPSI : Program mmenentukan apakah Tuan Riz berhasil menyelesaikan soal atau tidak

#KAMUS
# isian, esai, sisaIsian, sisaEsai, total : integer

#ALGORITMA
##input
isian  = int(input("Masukkan banyak soal isian singkat yang sudah diselesaikan: ")) 
esai   = int(input("Masukkan banyak soal esai yang sudah diselesaikan: "))
sisaIsian  = (14 - isian) * 10
sisaEsai   = (2 - esai) * 20
total  = sisaIsian + sisaEsai 

##proses + output
if (total <= 60):
  print("Tuan Riz akan berhasil mengerjakan semua soal")
else:
  print("Tuan Riz tidak berhasil mengerjakan semua soal tepat waktu")

#Selesai :D
