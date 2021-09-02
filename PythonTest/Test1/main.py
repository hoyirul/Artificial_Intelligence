import os
from fungsi import *

# IF Else
x = perkalian(3, 3)
if x == 9:
    print("Benar")
else:
    print("Salah")

# Looping
num = 1
while num <= 5:
    if num % 2 == 1:
        print(num, "Ganjil")
    else:
        print(num, "Genap")
    num += 1

datas = ["Indonesia", "Thailand", "Malaysia", "Singapore"]
no = 1
for row in datas:
    print(row)
