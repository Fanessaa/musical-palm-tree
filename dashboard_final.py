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
st.text('''Sebelum analisa dilakukan, data yang didapatkan dibersihkan terlebih dahulu, seperti melakukan casefolding untuk mengubah semua 
kata menjadi huruf kecil, menghapus tanda baca, angka, emotikon, dan lin-lain yang kurang berpengaruh di analisa kali ini. Data dari sosial 
media yang duplikat juga dihapus untuk mengurangi bias dan kata-kata slang diganti. Dan hasilnya dapat dilihat dibawah ini: ''')

df_article_clean = pd.read_csv('article_clean.csv')
st.dataframe(df_article_clean)
st.caption("dataframe berisi artikel setelah cleaning")

df_tweets_clean = pd.read_csv('tweets_clean.csv')
st.dataframe(df_tweets_clean)
st.caption("dataframe berisi tweets setelah cleaning")

# Data Analisis
st.subheader('Data Analisis')
st.text('''Dari grafik dibawah, dapat terliahat frekeunsi kata yang terdapat dalam artikel. Dapat dilihat bahwa kata-kata yang dominan atau seringkali muncul 
dalam artikel adalah “BUMN”, “Erick”, “Thohrir”, “Program” dan “Ekonomi”. Dari kelimat kata tersebut, dapat disimpulkan bahwa menteri BUMN ingin 
melaksanakan sebuah program untuk bisnis-bisinis untuk perkembangan eonomi Indonesia.''')

df_common_artikel = pd.read_csv('common_words_artikel.csv')
st.line_chart(data=ommon_artikel, *, x='Kata', y='Counts', width=0, height=0, use_container_width=True)


st.text('''Dari grafil frekuensi kata dari tweets, dapat dilihat bahwa publik sedangan membahas Erick Thonir, yang mereupakan menteri BUMN di Indonesia. Publik 
sedang melihat apa yang dilakukan dan kinerja menteri twehadap masalah ini. Tidak hanya BUMN, publik juga membahas mengenai UMKM, Usaha Mikro Kecil 
dan Menengah, yang tidak mungkin saja memiliki sangkut paut di dalam masalah ini. Publik juga membahas mengenai ekonomi negara dan kondisi keuangan 
yang bisa jadi alasan dari perbuatan BUMN. ''')

# grafik frekuensi kata tweets

st.text('''Sentimen analisis juga dilakukan terhadap tweets, dan dari hasil penemuan, dapat disumpulakn bahwa kebanyakn dari publik memiliki reaksi positif 
terhadap BUMN seperti yang terlihat di grafik bawah.''')

# grafik sentimen

# Data processing
st.header('Data Processing')
st.subheader('Modeling')
st.text('''Naive Bayes digunakan untuk mengkonstruksi sebuah prediction model untuk memprediksi apakah sebuah kalimat memiliki maksud positif atau negatif 
atau netral. Data yang digunakan adakah tweet yang didapatk dengan kata kunci “BUMN”.''')

# 

st.subheader('Evaluation')
st.text('''Dari confusion matrix terhadap prediction model yang dibuat, model memiliki nilai akuransi yang cukup tinggi, yaitu 0.833. Tidak hanya itu, model 
juga dapat memprediksi dengan benar dengan nilai yang tinggi seperti yang terlihat dari hasil precision.''')

# accuracy table

st.subheader('Prediction')

# percentage 

st.header('Reporting')
st.title('''Dari hasil penemuan, ditemukan bahwa publik memiliki sentimen positif terhadap keputusan yang diambil oleh menteri BUMN terhadap masalah. Dari 
hasil analisa text berita, dapat diketahui beberapa tindakan yang diambil oleh menteri untuk memperkuat ekonomi. Dan dari hasil analisa sentimen publik dari 
Twitter, dapat disimpulkan bahwa kebanyakan dari publik senang atau bependapat positif terhadap keputusan menteri.''') 



