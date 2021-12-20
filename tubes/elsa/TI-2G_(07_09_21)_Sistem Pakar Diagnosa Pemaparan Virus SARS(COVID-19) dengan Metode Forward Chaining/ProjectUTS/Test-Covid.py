global facts
global is_changed
global diagnosis
is_changed = True
gejala = [
    ["G01", "Demam Tinggi > 38℃"],["G02", "Batuk Kering"], ["G03", "Kelelahan"],["G04", "Bersin-bersin"],
    ["G05", "Rasa tidak nyaman dan nyeri"],["G06", "Nyeri Tenggorokan"], ["G07", "Diare"],
    ["G08", "Mata Merah"], ["G09", "Sakit Kepala"], ["G10", "Hilang indra penciuman/perasa"],
    ["G11", "Ruam pada kulit/perubahan pada warna jari-jari"], ["G12", "Kesulitan Bernafas/Sesak Nafas"], 
    ["G13", "Nyeri pada dada/Rasa Tertekan Pada Dada"], ["G14", "Kehilangan Kemampuan Berbicara atau Bergerak"], 
    ["G15", "Saturasi oksigen rendah < 90%"]      
    ]

facts = []
diagnosis = []

def addFacts(fact):
    global facts
    if not fact in facts:
        facts += [fact]

def diag() :
    print("\n-----------------------------------")
    print("Hasil Diagnosis "+nama)
    print("-----------------------------------")
    if len(diagnosis) == 0:
        print("Gejala tidak terdeteksi!")
        print("***")
    else :
        diagnosis.sort()
        print(diagnosis)
        print("")

    x = len(diagnosis)
    if x == 3 :
        if  diagnosis[0][0] == "P01" and diagnosis[1][0] == "P02" and diagnosis[2][0] == "P03":
            f = open(file='ProjectUTS\p03.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()        
    elif x == 2:
        # print("do")
        if  diagnosis[0][0] == "P01" and diagnosis[1][0] == "P02":
            f = open(file='ProjectUTS\p02.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()
        elif (diagnosis[0][0] == "P02" and diagnosis[1][0] == "P03") | (diagnosis[0][0] == "P01" and diagnosis[1][0] == "P03") :
            f = open(file='ProjectUTS\p03.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()             
    elif x == 1:
        if diagnosis[0][0] == "P01":
            f = open(file='ProjectUTS\p01.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()
        elif diagnosis[0][0] == "P02":
            f = open(file='ProjectUTS\p02.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()
        elif diagnosis[0][0] == "P03":
            f = open(file='ProjectUTS\p03.txt', mode='r', encoding='utf-8') 
            print(f.read())
            f.close()
    else :
        print("Mohon maaf gejala yang Anda alami tidak sesuai dengan diagnosa COVID-19")
        print("Silahkan menuju ke rumah sakit terdekat untuk pemeriksaan lebih lanjut")
        
def show() :
    print("=======================================================================")
    print("\t\t Gejala Umum Terinfeksi Virus SARS Covid-19")
    print("=======================================================================")
    print("\n Apakah anda merasakan salah satu atau lebih dari gejala berikut ini")
    print("1. Demam tinggi > 38℃")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G01",diag])

    print("2. Batuk Kering")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G02",diag])

    print("3. Kelelahan")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G03",diag])

    print("4. Bersin-bersin")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G04",diag])

    print("=======================================================================")
    print("\t\t Gejala Khusus Terinfeksi Virus SARS Covid-19")
    print("=======================================================================")
    print("\n Apakah anda merasakan salah satu atau lebih dari gejala berikut ini")
    
    print("1. Rasa Tidak Nyaman dan Nyeri")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G05",diag])

    print("2. Nyeri Tenggorokan")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G06",diag])

    print("3. Diare")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G07",diag])

    print("4. Konjungtivis(Mata Merah)")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G08",diag])
    
    print("5. Sakit Kepala")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G09",diag])

    print("6. Hilangnya Indra Perasa atau Penciuman")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G10",diag])

    print("7. Rauam Pada Kulit atau Perubahan Pada Warna Jari-jari")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G11",diag])

    print("=======================================================================")
    print("\t     Gejala Serius Terinfeksi Virus SARS Covid-19")
    print("=======================================================================")
    print("\n Apakah anda merasakan salah satu atau lebih dari gejala berikut ini")
    
    print("1. Kesulitan Bernafas/Sesak Nafas")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G12",diag])

    print("2. Nyeri pada dada/Rasa Tertekan Pada Dada")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G13",diag])

    print("3. Kehilangan Kemampuan Berbicara atau Bergerak")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G14",diag])

    print("4. Saturasi oksigen rendah < 90%")
    diag = input("   Jawab (y/n)? : ")
    addFacts(["G15",diag])

print("+-------------------------------------------------------+")
print("|\tSelamat Datang di Aplikasi Sistem Pakar \t|")
print("|\t\tMendeteksi COVID-19 \t\t\t|")
print("+----------------------------------------------------+")
nama = input("Nama\t : ")
pilihan = input("Hallo "+nama+",\nApakah anda ingin melakukan diagnosa (y/n)? ")

if pilihan == "y" :
    show()    
    def assert_fact(fact):
        global diagnosis
        global is_changed
        if not fact in diagnosis:
            diagnosis += [fact]
            is_changed = True
#---------------------------------------------------------------------------- 
    while is_changed:
        is_changed = False
        for A1 in facts:        
            if A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G03", "y"] and ["G04", "y"] in facts:
                assert_fact(["P01","Terindikasai 30%"])    
            elif A1[0] == "G01" and A1[1] == "y" and ["G06", "y"] and ["G09", "y"] in facts:
                assert_fact(["P01","Terindikasai 30%"])
            elif A1[0] == "G01" and A1[1] == "y" and ["G04", "y"] and ["G06", "y"] in facts:
                assert_fact(["P01","Terindikasai 30%"])
            elif A1[0] == "G04" and A1[1] == "y" and ["G06", "y"] and ["G09", "y"] in facts:
                assert_fact(["P01","Terindikasai 30%"])
            elif A1[0] == "G02" and A1[1] == "y" and ["G04", "y"] and ["G06", "y"] in facts:
                assert_fact(["P01","Terindikasai 30%"])                      
            elif A1[0] == "G05" and A1[1] == "y" and ["G06", "y"] and ["G07", "y"] and ["G08", "y"] and ["G09", "y"] and ["G10", "y"] and ["G11", "y"] in facts:
                assert_fact(["P02","Terindikasi 50%"])
            elif A1[0] == "G02" and A1[1] == "y" and ["G04", "y"] and ["G06", "y"] and ["G09", "y"] in facts:
                assert_fact(["P02","Terindikasi 50"])
            elif A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G04", "y"] and ["G09", "y"] in facts:
                assert_fact(["P02","Terindikasi 50"])                        
            elif A1[0] == "G01" and A1[1] == "y" and ["G04", "y"] and ["G06", "y"] and ["G09", "y"] in facts:
                assert_fact(["P02","Terindikasi 50"])
            elif A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G04", "y"] and ["G06", "y"] in facts:
                assert_fact(["P02","Terindikasi 50"])

            if A1[0] == "G12" and A1[1] == "y" and ["G13", "y"] and  ["G14", "y"] and  ["G15", "y"] in facts:
                assert_fact(["P03","Terindikasi 75%"])          
            if A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G03", "y"] and ["G04", "y"] and ["G13", "y"] in facts:
                assert_fact(["P03","Terindikasi 75%"])
            if A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G03", "y"] and ["G04", "y"] and ["G06", "y"] and ["G13", "y"] in facts:
                assert_fact(["P03","Terindikasi 75%"])
            if A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G03", "y"] and ["G04", "y"] and ["G09", "y"] and ["G13", "y"] in facts:
                assert_fact(["P03","Terindikasi 75%"])
            if A1[0] == "G01" and A1[1] == "y" and ["G02", "y"] and ["G03", "y"] and ["G04", "y"] and ["G06", "y"] and ["G09", "y"] and ["G13", "y"] in facts:
                assert_fact(["P03","Terindikasi 75%"])
    diag()    
else :
    print("Terima Kasih sudah berkunjung")
    print("Jangan bosan untuk menerapkan protokol kesehatan :)")
