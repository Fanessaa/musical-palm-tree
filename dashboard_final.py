#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json, tweepy, requests, re
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# In[4]:


st.title("Sentiment Analisis terhadap kata 'BUMN'")

st.header('Business Understanding')
st.text("Dengan maraknya berita mengenai isu ekonomi dalam negeri dan di luar negeri. Banyak sekali orang-orang, terlebih mereka yang memiliki usaha khawatir dengan nasib bisnis mereka Pada kesempatan kali ini, saya ingin menganalisa bagaimana sentimen publik terhadap isu ini. Pertama-tama, kata kunci yang akan digunakan adalah “BUMN” atau Badan usaha milik negara, alasan dibalik ini karena BUMN sebagai badan yang mengatur hal-hal bersangkutan dengan bisnis, merekalah yang memiliki peran penting.  Maka, pada kali ini, sentimen publik terhadap kinerja pemerinatah kan di cari. Sosial media, Twitter juga akan digunakan sebagai platform untuk mendapatkan informasi terhadap reaksi, perasaan dan pendapat rakyat terhadap BUMN. ")


# In[8]:


st.header('Data understanding')
st.subheader('Data collection')
st.text("Untuk mencari tahu mengenai kejadian-kejadian yang baru-baru ini terjadi yang berkaitan dengan kata kunci 'BUMN', salah satu berita terbaru mengenai BUMN akan dipilih dan isinya kan dianalisa. Kali ini, berita berasal dari sumber kompas.com dengan judul ‘Erick Thohir: Folus Bakti BUMN Perkuat Ekonomi Kerakyataan’. Dengan menggunakan artikel tersebut, gambaran terhadap situasi yang sedang terjadi dapat didapatkan.")

alamat = "https://money.kompas.com/read/2022/11/12/130000026/erick-thohir--fokus-bakti-bumn-perkuat-ekonomi-kerakyatan"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

articles = data.find_all("p")
info = []

for p in articles:
    info.append(p.get_text())

df_article = pd.DataFrame (info, columns = ['Artikel'])
st.dataframe(df_article)


st.text("Opini publik terhadap isu ini akan diperoleh dari sosial media Twitter menggunakan kata ‘BUMN’ untuk melihat sentimen publik. ")
df = pd.read_csv('tweets.csv')
st.dataframe(df)


# In[10]:


st.text("Sebelum analisa dilakukan, data yang didapatkan dibersihkan terlebih dahulu, seperti menghapus tanda baca, angka, emotikon, dan lin-lain yang kurang berpengaruh di analisa kali ini. Data dari sosial media yang duplikat juga dihapus untuk mengurangi bias dan kata-kata slang diganti. Dan hasilnya dapat dilihat dibawah ini: ")




#case folding
tweets = list(map(lambda x: x.lower(),df['tweets']))
tweets = list(map(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^A-Za-z \t])|(\w+:\/\/\S+)|(\d+)", " ", x).split()),tweets))
df['clean_tweets'] = tweets

# stopword 
def remove_words(x):
    all_stopwords = stopwords.words('indonesian')
    return ' '.join([word for word in x.split() if word not in (all_stopwords)])

df['clean_tweets'] = df['clean_tweets'].apply(lambda x: remove_words(x))
st.dataframe(df)

