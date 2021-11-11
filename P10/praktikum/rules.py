import os

def logika(spektrum, usia, gejala):
    gejalaArray = ['G1','G2','G3','G4','G13','G19','G25','G26','G28','G36']
    terapi = ['T1']
    if spektrum == 'S1' :
        if usia == 'U1' :
            if gejala == gejalaArray : # jika sudah terpenuhi semua maka akan menghasilkan sebuah keputusan
                print("Terapi yang dapat dilakukan", terapi)
                return terapi
