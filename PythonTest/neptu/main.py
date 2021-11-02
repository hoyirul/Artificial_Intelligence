import os
import numpy as np

tanggal = int(input("Masukkan tanggal Jawa : "))
hari = int(input("Masukkan Hari : "))
pasaran = input("Masukkan Pasaran Jawa : ")

# urutan senin-mingu
hari_array = [5, 4, 3, 7, 8, 6, 9]
# urutan paeng, pon, begin, kliwon, manis
pasaran_array = [9, 7, 4, 8, 5]

if(i % 4 == 1):
    print(i, " : Kertah")
elif(i % 4 == 2):
    print(i, " : Jeksah")
elif(i % 4 == 3):
    print(i, " : Rage")
else:
    print(i, " : Regu")
