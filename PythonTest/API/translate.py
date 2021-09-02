from googletrans import Translator

trans = Translator()
translation = trans.translate("Halo Dunia")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
