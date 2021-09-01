import os

var = int(input("Masukkan bilangan desimal : "))

# Nomor 1
print("\nNomor 1")
desimal = int(var)
oktal = oct(desimal).replace("0o", "")  # desimal -> oktal
print("Desimal : ", desimal, "- Oktal   : ", oktal)
print("Oktal   : ", oktal, "- Desimal : ", int(oktal, 8))

# Nomor 2
print("\nNomor 2")
hexa = hex(desimal).replace("0x", "")  # desimal -> hexa
print("Desimal : ", desimal, "- Hexa    : ", hexa.upper())
print("Hexa    : ", hexa.upper(), "- Desimal : ", int(hexa, 16))

# Konversi desimal -> Binner
binner = bin(desimal).replace("0b", "")  # desimal -> binner

# Nomor 3
print("\nNomor 3")
bin_oct = int(binner, 2)  # binner -> oktal
oct_bin = int(oct(bin_oct).replace("0o", ""), 8)  # oktal -> binner
print("Binner : ", binner, "- Oktal  : ", oct(bin_oct).replace("0o", ""))
print("Oktal  : ", oct(bin_oct).replace("0o", ""),
      "- Binner : ", bin(oct_bin).replace("0b", ""))

# Nomor 4 a
print("\nNomor 4")
bin_hex = int(binner, 2)  # binner -> hexa
hex_bin = int(hex(bin_hex).replace("0x", ""), 16)  # hexa -> binner
print("Binner : ", binner, "- Hexa   : ",
      hex(bin_hex).replace("0x", "").upper())
print("Hexa   : ", hex(bin_hex).replace("0x", "").upper(),
      "- Binner : ", bin(hex_bin).replace("0b", ""))

# Nomor 5
print("\nNomor 5")
des_oct = oct(desimal).replace("0o", "")  # desimal -> oktal
oct_hex = int(des_oct, 8)  # oktal -> desimal
hex_oct = int(hex(oct_hex).replace("0x", ""), 16)  # hexa -> oktal
print("Oktal : ", des_oct, "- Hexa : ", hex(oct_hex).replace("0x", "").upper())
print("Hexa  : ", hex(oct_hex).replace("0x", "").upper(),
      "- Hexa : ", oct(hex_oct).replace("0o", ""))
