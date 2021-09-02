import os
import speech_recognition as sr
from googletrans import Translator
import simpleaudio as sa

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
    wave_obj = sa.WaveObject.from_wave_file("F:/MUSIC/voi1.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    # print("Silahkan mulai berbicara")
    rekaman = engine.listen(source)
    wave_obj2 = sa.WaveObject.from_wave_file("F:/MUSIC/voi2.wav")
    play_obj2 = wave_obj2.play()
    play_obj2.wait_done()
    # print("Waktu habis")

    try:
        hasil = engine.recognize_google(rekaman, language="id-ID")
        print("ID : ", hasil)
    except engine.UnknownValueError:
        print("Maaf tidak dideteksi")
    except Exception as e:
        print(e)

trans = Translator()
translation = trans.translate(hasil)
print(f"({translation.src}) --> {translation.text} ({translation.dest})")

# Pengalaman pengguna adalah bagaimana cara seseorang merasakan ketika menggunakan sebuah produk, sistem, atau jasa
