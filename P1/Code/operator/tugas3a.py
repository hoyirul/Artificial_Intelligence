import os

a = int("AF", 16)
b = 91
x = a & b
y = a | b
z = a ^ b
n = ~a
print()
print("AND : ", x, "-> BINNER : ", bin(x).replace("0b", ""))
print("OR  : ", y, "-> BINNER : ", bin(y).replace("0b", ""))
print("XOR : ", z, "-> BINNER : ", bin(z).replace("0b", ""))
print("NOT : ", n, "-> BINNER : ", bin(n).replace("0b", ""))
