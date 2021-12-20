url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
from sre_constants import IN_LOC_IGNORE
import requests
r = requests.get(url)
type(r)
requests?
html = r.text
print(html)
#Menginport BeautifulSoup dari bs4
from bs4 import BeautifulStoneSoup
# Membuat objek BeautifulSoup dari HTML
soup = BeautifulStoneSoup(html, "htm5lib")
type(soup)
soup.tilte
soup.title.string
soup.findAll('a')[:8]
text = soup.get_text()
print(text)
# pip install -U nltk
import nltk
nltk.download()
# import paket regex
import re
#Definisikan setence
sentence = 'peter piper pick a peck of pickled peppers'
#Definisikan regex
ps = 'p\wt'
# Mencarikan semua kata di sentence yang cocok dengan regex kemudian cetal
re.findall(ps, sentence)
re.findall('\w+', sentence)
tokens = re.findall('\w+', text)
tokens [:8]
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
tokens[:8]
words = []
for word in tokens:
    words.append(word.lower())
words[:8]

words_ns = []

for word in words:
    if word not in sw:
        words_ns.append(word)
words_ns[:5]

import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sns.set()

freqdist1 = nltk.FreqDist(word_ns)
freqdist1.plot(25)