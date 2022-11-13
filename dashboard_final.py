#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Sentiment Analisis terhadap kata 'BUMN'")

# Business understanding
st.header('Business Understanding')
st.text('''Dengan maraknya berita mengenai isu ekonomi dalam negeri dan di luar negeri. Banyak sekali orang-orang, terlebih mereka yang memiliki usaha 
khawatir dengan nasib bisnis mereka Pada kesempatan kali ini, saya ingin menganalisa bagaimana sentimen publik terhadap isu ini. 
Pertama-tama, kata kunci yang akan digunakan adalah “BUMN” atau Badan usaha milik negara, alasan dibalik ini karena BUMN sebagai badan 
yang mengatur hal-hal bersangkutan dengan bisnis, merekalah yang memiliki peran penting.  Maka, pada kali ini, sentimen publik terhadap 
kinerja pemerinatah kan di cari. Sosial media, Twitter juga akan digunakan sebagai platform untuk mendapatkan informasi terhadap reaksi, 
perasaan dan pendapat rakyat terhadap BUMN.''')

# Data understanding
st.header('Data understanding')
st.subheader('Data collection')
st.text('''Untuk mencari tahu mengenai kejadian-kejadian yang baru-baru ini terjadi yang berkaitan dengan kata kunci 'BUMN', salah satu berita terbaru 
mengenai BUMN akan dipilih dan isinya kan dianalisa. Kali ini, berita berasal dari sumber kompas.com dengan judul ‘Erick Thohir: Folus 
Bakti BUMN Perkuat Ekonomi Kerakyataan’. Dengan menggunakan artikel tersebut, gambaran terhadap situasi yang sedang terjadi dapat didapatkan.''')

df_article = pd.read_csv('article.csv')
st.dataframe(df_article)

st.text("Opini publik terhadap isu ini akan diperoleh dari sosial media Twitter menggunakan kata ‘BUMN’ untuk melihat sentimen publik. Seperti dibawah ini:")
df_tweets = pd.read_csv('tweets.csv')
st.dataframe(df_tweets)

# Data preprocessing
st.subheader('Data preprocessing')
st.text('''Sebelum analisa dilakukan, data yang didapatkan dibersihkan terlebih dahulu, seperti melakukan casefolding untuk mengubah semua kata menjadi huruf kecil, 
menghapus tanda baca, angka, emotikon, dan lin-lain yang kurang berpengaruh di analisa kali ini. Data dari sosial media yang duplikat juga dihapus untuk mengurangi 
bias dan kata-kata slang diganti. Dan hasilnya dapat dilihat dibawah ini: ''')

df_article_clean = pd.read_csv('article_clean.csv')
st.dataframe(df_article_clean)
st.caption("dataframe berisi artikel setelah cleaning")

df_tweets_clean = pd.read_csv('tweets_clean.csv')
st.dataframe(df_tweets_clean)
st.caption("dataframe berisi tweets setelah cleaning")

# Data Analisis
st.subheader('Data Analisis')
st.text('''Dari grafik dibawah, dapat terliahat frekeunsi kata yang terdapat dalam artikel. Dapat dilihat bahwa kata-kata yang dominan atau seringkali muncul dalam 
artikel adalah “BUMN”, “Erick”, “Thohrir”, “Program” dan “Ekonomi”. Dari kelimat kata tersebut, dapat disimpulkan bahwa menteri BUMN ingin melaksanakan sebuah program 
untuk bisnis-bisinis untuk perkembangan eonomi Indonesia.''')


