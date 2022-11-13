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
st.text('''Dari grafik dibawah, dapat terliahat frekeunsi kata yang terdapat dalam artikel. Dapat dilihat bahwa kata-kata yang dominan atau 
seringkali muncul dalam artikel adalah “BUMN”, “Erick”, “Thohrir”, “Program” dan “Ekonomi”. Dari kelimat kata tersebut, dapat disimpulkan 
bahwa menteri BUMN ingin melaksanakan sebuah program untuk bisnis-bisinis untuk perkembangan eonomi Indonesia.''')

df_common_artikel = pd.read_csv('common_words_artikel.csv')
st.line_chart(data=df_common_artikel, x='Kata', y='Counts', width=0, height=0, use_container_width=True)

st.text('''Dari grafik frekuensi kata dari tweets di bawah, dapat dilihat bahwa publik sedangan membahas Erick Thonir, yang mereupakan menteri 
BUMN di Indonesia. Publik sedang melihat apa yang dilakukan dan kinerja menteri twehadap masalah ini. Tidak hanya BUMN, publik juga membahas 
mengenai UMKM, Usaha Mikro Kecil dan Menengah, yang tidak mungkin saja memiliki sangkut paut di dalam masalah ini. Publik juga membahas mengenai 
ekonomi negara dan kondisi keuangan yang bisa jadi alasan dari perbuatan BUMN. ''')

df_common_tweets = pd.read_csv('common_words_tweets.csv')
st.line_chart(data=df_common_tweets, x='Kata', y='Counts', width=0, height=0, use_container_width=True)

st.text('''Sentimen analisis juga dilakukan terhadap tweets, pertama-pertama, hasil tweets yang ditemukan akan dibandingkan dengan list kata-kata 
yang memiliki arti positif dan negatif. Dalam satu tweet, akan dihitung seberapa banyak kata positif dan negatif, jika lebih banyak nilai positif, 
maka akan diberi label 1, jika lebih banyak nilai negatif, akan diberi label 0, jika tidak perbedaan akan diberi nilai 0 dan. Dari hasil penemuan, 
dapat disumpulakn bahwa kebanyakn dari publik memiliki reaksi positif terhadap BUMN seperti yang terlihat di hasil analisa di bawah.''')

# statistics
df_stat = pd.read_csv('statistics.csv')
st.dataframe(df_stat)

# grafik sentimen

df_sentimen = pd.read_csv('sentimen_labels.csv')
df_sentimen = df_sentimen.set_index('Counts')
st.bar_chart(df_sentimen)

st.text(''' Seperti yang dilihat dari hasil statistika yang di dapatkan dari prediction model, nilai mean dan nilai median tidak beda jauh, dan nilai 
mean lebih rendah dari nilai median, dapat disimpulkan bahwa model hampir memiliki bilai distribusi normal. Hal ini didukung dengan grafik distribusi 
label-label.''')

df_count_sentimen = pd.read_csv('count_sentiment.csv')
st.bar_chart(df_count_sentimen)

st.text(''' Dari bar chart di atas, dapat dilihat bahwa kebanyakan dari pengguna Twitter memiliki reaksi positif terhadap tindakan yang diambil 
pemerintah, nilai pengguna Twitter dan memiliki reaksi negatif tidak sebanyak mereka yang bereaksi positif''')

# Data processing
st.header('Data Processing')
st.subheader('Modeling')
st.text('''Naive Bayes digunakan untuk mengkonstruksi sebuah prediction model untuk memprediksi apakah sebuah kalimat memiliki maksud positif atau 
negatif atau netral. Data yang digunakan adakah tweet yang didapatkan dengan kata kunci “BUMN”. Kategori sentiment juga diganti dengan angka numerik, 
dimana 0 adalah negatif,1 adalah positif dan 2 adalah neutral''')

df_sentimen_ml = pd.read_csv('sentiment_ml.csv')
st.caption(''' Data setelah nilai kategori sentimen diberikan nilai numerik''')
st.dataframe(df_sentimen_ml)

st.subheader('Evaluation')
# accuracy table
df_classif_report = pd.read_csv('classification_report.csv')
st.dataframe(df_classif_report)
st.text('''Dari confusion matrix terhadap prediction model yang dibuat, model memiliki nilai akuransi yang cukup tinggi, yaitu 0.833. Tidak hanya itu, 
model juga dapat memprediksi dengan benar dengan nilai yang tinggi seperti yang terlihat dari hasil precision.''')

st.subheader('Prediction')
# Preditction percentage 
df_predict_percent = pd.read_csv('df_predict_count.csv')
st.dataframe(df_predict_percent)
st.text('''Prediction model memprediksi bahwa terdapat hampir 60% orang yang memiliki reaksi positif''')

st.header('Reporting')
st.text('''Dari hasil penemuan, ditemukan bahwa publik memiliki sentimen positif terhadap keputusan yang diambil oleh menteri BUMN terhadap masalah. Dari 
hasil analisa text berita, dapat diketahui beberapa tindakan yang diambil oleh menteri untuk memperkuat ekonomi. Dan dari hasil analisa sentimen publik 
dari Twitter, dapat disimpulkan bahwa kebanyakan dari publik senang atau bependapat positif terhadap keputusan menteri.''') 

