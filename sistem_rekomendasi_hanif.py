# -*- coding: utf-8 -*-
"""Sistem_Rekomendasi_Hanif

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qlx_fy4VI0VhfwfELFpjRJ54B5mn8OaJ
"""

!pip install -q kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 /root/.kaggle/kaggle.json

!kaggle datasets download -d mirajshah07/netflix-dataset

!unzip /content/netflix-dataset.zip

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

netflix_data = pd.read_csv('/content/netflix_dataset.csv')
netflix_data.head()

netflix_data.info()

imdb_data = pd.read_csv('/content/IMDb movies.csv')
imdb_data.head()

imdb_data.info()

imdb_rating = pd.read_csv('/content/IMDb ratings.csv')
imdb_rating.head()

imdb_rating.info()

netflix_data.info()

dict = {}
for i in list(netflix_data.columns):
    dict[i] = netflix_data[i].value_counts().shape[0]
    
print(pd.DataFrame(dict,index = ["unique count"]).transpose())

"""show_id memang mewakili kunci utama dari dataset. Hanya ada dua jenis jenis konten Netflix, sedangkan jenis konten lain yang didistribusikan dalam rentang yang luas akan membutuhkan analisis lebih lanjut dengan grafik.

# **Missing Values**
"""

print('Table of missing values: ')
print(netflix_data.isnull().sum())



"""# **Exploratory Data Analysis**

**Analysis of Movies vs TV Shows**
"""

movies_data=netflix_data[netflix_data['type']=='Movie']
tvshows_data=netflix_data[netflix_data['type']=='TV Show']

plt.figure(figsize=(10,7))
sns.set(style="whitegrid")
ax = sns.countplot(x="type", data=netflix_data, palette="Set1")
ax.set_title("Movies VS TV Shows")

"""Terlihat pada grafik diatas, bahwa Movie lebih banyak di Netflix daripada TV Shows.

# **Heatmap for Analysis**

**Membuat Heatmap untuk Melihat pada bulan apa saja, seorang produsen merilis filmnya.**
"""

netflix_date = tvshows_data[['date_added']].dropna()
netflix_date['year'] = netflix_date['date_added'].apply(lambda x : x.split(', ')[-1])
netflix_date['month'] = netflix_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][::-1]
df = netflix_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order].T
plt.figure(figsize=(10, 7), dpi=200)
plt.pcolor(df, cmap='afmhot_r', edgecolors='white', linewidths=2)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, fontsize=7, fontfamily='serif')
plt.yticks(np.arange(0.5, len(df.index), 1), df.index, fontsize=7, fontfamily='serif')

plt.title('Netflix Contents Update', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))
cbar = plt.colorbar()

cbar.ax.tick_params(labelsize=8) 
cbar.ax.minorticks_on()
plt.show()

"""Terlihat pada tahun 2020, bulan Februari dan Juni adalah bulan ketika konten yang dirilis relatif lebih sedikit.

# **Movie Ratings Analysis**
"""

plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
ax = sns.countplot(x="rating", data=netflix_data, palette="Set1", order=netflix_data['rating'].value_counts().index[0:15])

"""Terlihat pada grafik diatas TV-MA memiliki rating paling tinggi. TV-MA adalah peringkat yang diberikan oleh Pedoman Orang Tua TV untuk program televisi yang dirancang hanya untuk dewasa.

Rating tertinggi kedua adalah TV-14 (konten yang mungkin tidak pantas untuk anak-anak di bawah usia 14 tahun.)

Rating tertinggi ketiga adalah TV-PG (berisi beberapa materi yang mungkin dianggap tidak pantas oleh orang tua atau wali untuk anak-anak yang lebih muda. )

# **Analysis IMDB Ratings Top Rated Movies on Netflix**
"""

imdb_ratings=pd.read_csv('/content/IMDb ratings.csv', usecols=['weighted_average_vote'])
imdb_titles=pd.read_csv('/content/IMDb movies.csv', usecols=['title','year','genre'])
ratings=pd.DataFrame({'Title':imdb_titles.title,
                      'Release Year':imdb_titles.year,
                      'Rating':imdb_ratings.weighted_average_vote,
                      'Genre':imdb_titles.genre})
ratings.drop_duplicates(subset=['Title','Release Year','Rating'], inplace=True)
ratings.shape

"""Melakukan inner join pada dataset peringkat dan dataset netflix untuk mendapatkan konten yang memiliki peringkat di IMDB dan tersedia di Netflix."""

ratings.dropna()
joint_data=ratings.merge(netflix_data,left_on='Title', right_on='title', how='inner')
joint_data=joint_data.sort_values(by='Rating', ascending=False)

"""# **Top Rated 10 Movies in Netflix**"""

import plotly.express as px
top_rated=joint_data[0:10]
fig =px.sunburst(
    top_rated,
    path=['title','country'],
    values='Rating',
    color='Rating')
fig.show()

"""# **Top countries creating contents**"""

country_count=joint_data['country'].value_counts().sort_values(ascending=False)
country_count=pd.DataFrame(country_count)
topcountries=country_count[0:11]
topcountries

"""# **Year wise analysis**"""

last_years = netflix_data[netflix_data['release_year']>2005 ]
last_years.head()

plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
ax = sns.countplot(y="release_year", 
                   data=last_years, 
                   palette="Set1", 
                   order=netflix_data['release_year'].value_counts().index[0:15])

"""Terlihat pada grafik diatas, tahun 2018 adalah paling banyak konten dirilis

# **TV Shows Analysis**
"""

countries={}
tvshows_data['country']=tvshows_data['country'].fillna('Unknown')
cou=list(tvshows_data['country'])
for i in cou:
    #print(i)
    i=list(i.split(','))
    if len(i)==1:
        if i in list(countries.keys()):
            countries[i]+=1
        else:
            countries[i[0]]=1
    else:
        for j in i:
            if j in list(countries.keys()):
                countries[j]+=1
            else:
                countries[j]=1

countries_fin={}
for country,no in countries.items():
    country=country.replace(' ','')
    if country in list(countries_fin.keys()):
        countries_fin[country]+=no
    else:
        countries_fin[country]=no
        
countries_fin={k: v for k, v in sorted(countries_fin.items(), key=lambda item: item[1], reverse= True)}

plt.figure(figsize=(8,8))
ax = sns.barplot(x=list(countries_fin.keys())[0:10],y=list(countries_fin.values())[0:10])
ax.set_xticklabels(list(countries_fin.keys())[0:10],rotation = 90)

"""Amerika Serikat memiliki konten acara TV terbanyak yang dibuat di netflix.

# **Analysis of duration of movies**
"""

movies_data['duration']=movies_data['duration'].str.replace(' min','')
movies_data['duration']=movies_data['duration'].astype(str).astype(int)
movies_data['duration']

sns.set(style="darkgrid")
ax=sns.kdeplot(data=movies_data['duration'], shade=True)

"""Dari grafik diatas terlihat bahwa film di netflix garis besar berdurasi 75-120 Menit. Hal ini dapat di validasi dengan fakta bahwa cukup banyak penonton yang tidak dapat menonton film berdurasi 3 jam dalam sekali tonton.

# **Analysis of duration of TV Shows**
"""

features=['title','duration']
durations= tvshows_data[features]

durations['no_of_seasons']=durations['duration'].str.replace(' Season','')

durations['no_of_seasons']=durations['no_of_seasons'].str.replace('s','')

durations['no_of_seasons']=durations['no_of_seasons'].astype(str).astype(int)

t=['title','no_of_seasons']
top=durations[t]

top=top.sort_values(by='no_of_seasons', ascending=False)

top20=top[0:20]
top20.plot(kind='bar',x='title',y='no_of_seasons', color='blue')

"""Grey's Anatomy, NCIS dan Supernatural adalah salah satu serial tv yang memiliki jumlah Season terbanyak.

# **Content-Based Recommendation System**

**Plot description based Recommender (Content Based Recommendations)**

Kita akan menghitung skor kemiripan korelasi untuk semua film berdasarkan deskripsi plot dan merekomendasikan film berdasarkan skor kemiripan tersebut. Deskripsi plot diberikan dalam fitur deskripsi dataset kami.
"""

netflix_data['description'].head()

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')

netflix_data['description'] = netflix_data['description'].fillna('')

tfidf_matrix = tfidf.fit_transform(netflix_data['description'])

tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(netflix_data.index, index=netflix_data['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return netflix_data['title'].iloc[movie_indices]

get_recommendations('Welcome')

get_recommendations('Avengers: Infinity War')

get_recommendations('Dil Dhadakne Do')

"""Meskipun sistem telah melakukan pekerjaan yang layak untuk menemukan film dengan deskripsi plot yang serupa, kualitas rekomendasinya tidak terlalu bagus. "Welcome" mengembalikan film dengan deskripsi yang mirip, sementara kemungkinan besar orang-orang yang menyukai film itu lebih cenderung menikmati film Akshay Kumar lainnya. Ini adalah sesuatu yang tidak dapat ditangkap oleh sistem yang ada sekarang.

Oleh karena itu, lebih banyak metrik ditambahkan ke model untuk meningkatkan kinerja.
"""

filledna=netflix_data.fillna('')
filledna.head()

"""Langkah selanjutnya adalah mengubah nama dan contoh kata kunci menjadi huruf kecil dan menghapus semua spasi di antara mereka."""

def clean_data(x):
        return str.lower(x.replace(" ", ""))

features=['title','director','cast','listed_in','description']
filledna=filledna[features]

for feature in features:
    filledna[feature] = filledna[feature].apply(clean_data)
    
filledna.head()

def create_soup(x):
    return x['title']+ ' ' + x['director'] + ' ' + x['cast'] + ' ' +x['listed_in']+' '+ x['description']

filledna['soup'] = filledna.apply(create_soup, axis=1)

"""Langkah-langkah selanjutnya sama dengan apa yang kita lakukan dengan rekomendasi berbasis deskripsi plot kita.

Satu perbedaan penting adalah bahwa kita menggunakan CountVectorizer() bukan TF-IDF.
"""

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(filledna['soup'])

filledna=filledna.reset_index()
indices = pd.Series(filledna.index, index=filledna['title'])

tfid = TfidfVectorizer(stop_words='english')
tfid.fit(netflix_data['listed_in'])
tfid.get_feature_names()

tfidf_matrix = tfid.fit_transform(netflix_data['listed_in']) 
tfidf_matrix.shape

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=netflix_data['title'],
                             columns=netflix_data['title'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(10, axis=1).sample(10, axis=0)

def MovieRecommendations(title, similarity_data=cosine_sim_df, 
                         items=netflix_data[['type','show_id','title','listed_in','rating']], k=10):
    index = similarity_data.loc[:, title].to_numpy().argpartition(
        range(-1, -k, -1)
    )

    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    closest = closest.drop(title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

find_title = netflix_data[netflix_data['title'] == 'Casino Tycoon 2']
find_title

movie_title = 'Casino Tycoon 2'
movie_recomend = MovieRecommendations(movie_title)
movie_recomend.head(10)

find_title = netflix_data[netflix_data['title'] == 'One Strange Rock']
find_title

movie_title = 'One Strange Rock'
movie_recomend = MovieRecommendations(movie_title)
movie_recomend.head(10)

"""Kami melihat rekomendasi telah berhasil menangkap lebih banyak informasi karena lebih banyak data dan telah memberikan bisa dibilang rekomendasi yang lebih baik. Kemungkinan besar penggemar komik Marvel atau DC akan menyukai film dari produksi yang sama. Oleh karena itu, untuk fitur di atas kita dapat menambahkan production_company ."""