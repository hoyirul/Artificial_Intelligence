import os

# Cara compile(running) program ini adalah per nomor, jadi jika mau compile Nomor 1 a maka nomor lain dijadikan komen
# Nomor 1 a
print("Desimal - Oktal")
desimal = int(input("Masukkan bilangan desimal : "))
oktal = oct(desimal).replace("0o", "")
print(oktal)

# Nomor 1 b
print("Oktal - Desimal")
oktal = int(input("Masukkan bilangan oktal : "), 8)
print(oktal)

# Nomor 2 a
print("Desimal - Hexa")
desimal = int(input("Masukkan bilangan desimal : "))
hexa = hex(desimal).replace("0x", "")
print(hexa.upper())

# Nomor 2 b
print("Hexa - Desimal")
hexa = int(input("Masukkan bilangan hexa : "), 16)
print(hexa)

# Nomor 3 a
print("Binner - Oktal")
binner = int(input("Masukkan bilangan binner : "), 2)
print(oct(binner).replace("0o", ""))

# Nomor 3 b
print("Oktal - Binner")
oktal = int(input("Masukkan bilangan oktal : "), 8)
print(bin(oktal).replace("0b", ""))

# Nomor 4 a
print("Binner - Hexa")
binner = int(input("Masukkan bilangan binner : "), 2)
print(hex(binner).replace("0x", "").upper())

# Nomor 4 b
print("Hexa - Binnner")
hexa = int(input("Masukkan Bilangan hexa : "), 16)
print(bin(hexa).replace("0b", ""))

# Nomor 5 a
print("Hexa - Oktal")
hexa = int(input("Masukkan bilangan hexa : "), 16)
print(oct(hexa).replace("0o", ""))

# Nomor 5 b
print("Oktal - Hexa")
oktal = int(input("Masukkan bilangan oktal : "), 8)
print(hex(oktal).replace("0x", "").upper())
