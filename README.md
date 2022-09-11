# Laporan Proyek Machine Learning - Hanif Al Irsyad

## Project Overview
---
Sistem Rekomendasi Film, merupakan Sistem yang digunakan untuk merekomendasikan sebuah film/konten yang biasanya digunakan pada platform seperti Netflix. Sistem rekomendasi yang saya buat ini didasarkan dengan peferensi kesukaan pengguna pada tahun lalu, serta rating dari movie tersebut.

Sistem Rekomendasi telah menjadi lazim dalam beberapa tahun terakhir karena mereka menangani masalah kelebihan informasi dengan menyarankan pengguna sebuah produk yang paling relevan dari sejumlah besar data. Untuk produk media, Sistem Rekomendasi film berupaya membantu pengguna mengakses film pilihan mereka dengan menangkap tetangga yang persis sama di antara pengguna atau film dari peringkat umum historis mereka. Namun, karena data yang jarang, pemilihan tetangga menjadi lebih sulit dengan meningkatnya film dan pengguna dengan cepat.

## Business Understanding
---

### Problem Statement
Berdasarkan pada latar belakang di atas, permasalahan yang dapat diselesaikan pada proyek ini adalah sebagai berikut :
* Bagaimana cara merekomendasikan movie yang disukai pengguna lain dapat direkomendasikan kepada pengguna lainnya juga ?

### Goals
* Dapat membuat sistem rekomendasi yang akurat berdasarkan ratings dan aktivitas pengguna pada masa lalu.

### Solution approach
Solusi yang dapat dilakukan agar goals terpenuhi adalah sebagai berikut :
* Melakukan analisa, eksplorasi, pemrosesan pada data dengan memvisualisasikan data agar mendapat gambaran bagaimana data tersebut. Berikut adalah analisa yang dapat dilakukan :
    * Membuat sebuah Analysis terkait jumlah film dan tv show yang ada pada Data.
    * Membuat heatmap yang digunakan untuk melihat kapan saja produser membuat konten.
    * Membuat Analysis dari rating sebuah konten.
    * Membuat grafik dari Top 10 Rated Film di Netflix.
    
* Berikut beberapa algoritma yang digunakan pada proyek ini :
    *Content Based Filtering** adalah algoritma yang merekomendasikan film serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit.

Algoritma Content Based Filtering digunakan untuk merekemondesikan film berdasarkan aktivitas pengguna pada masa lalu. 

## Data Understanding

Data atau dataset yang digunakan pada proyek machine learning ini adalah data **Netflix Movies and TV Shows Dataset** yang didapat dari situs kaggle. Link dataset dapat dilihat dari tautan berikut [netflix-dataset](https://www.kaggle.com/datasets/mirajshah07/netflix-dataset)

Variabel-variabel pada movie-recommendation-data adalah sebagai berikut :

  * show_id : ID dari sebuah data film.
  * type : Tipe dari konten yang ada pada data (Movie/Tv-Show)
  * title : Judul dari sebuah konten.
  * director : Director dari konten yang dibuat.
  * cast : Pemain/Pemeran pada konten yang dibuat.
  * country : Negara asal dari konten yang dibuat.
  * date_added : Tanggal perilisan konten.
  * release_year : Tahun perilisan konten.
  * rating : Rating dari konten yang dibuat, seperti (TV-MA,TV-14,TV-PG,R,PG-13,TV-Y,dll.)
  * duration : Durasi dari konten yang dibuat.
  * listed_in : Genre dari konten yang dibuat.
  * description : Deskripsi dari konten.

## Exploratory Data Analysis
* Membuat sebuah Analysis terkait jumlah film dan tv show yang ada pada Data.
<br>
<image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/1.png' width= 500/>
<br> Terlihat pada grafik diatas, bahwa Movie lebih banyak di Netflix daripada TV Shows.<p>

* Membuat heatmap yang digunakan untuk melihat kapan saja produser membuat konten.
<br>
<image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/2.png' width= 500/>
<br> Terlihat pada tahun 2020, bulan Februari dan Juni adalah bulan ketika konten yang dirilis relatif lebih sedikit.<p>

* Membuat Analysis dari rating sebuah konten.
<br>
<image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/3.png' width= 500/>
<br> Terlihat pada grafik diatas TV-MA memiliki rating paling tinggi. TV-MA adalah peringkat yang diberikan oleh Pedoman Orang Tua TV untuk program televisi yang dirancang hanya untuk dewasa.
Rating tertinggi kedua adalah TV-14 (konten yang mungkin tidak pantas untuk anak-anak di bawah usia 14 tahun.)
Rating tertinggi ketiga adalah TV-PG (berisi beberapa materi yang mungkin dianggap tidak pantas oleh orang tua atau wali untuk anak-anak yang lebih muda. ) <p>

* Membuat grafik dari Top 10 Rated Film di Netflix
<br>
<image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/4.png' width= 500/> <p>

## Data Preparation
---

Data preparation yang digunakan oleh saya yaitu :

- Mengatasi missing value : menyeleksi data apakah data tersebut ada yang kosong atau tidak.
- Identifikasi Unique Value : identifikasi ini digunakan untuk mencari ID Unik yang akan menjadi sebuah kata kunci nanti.
- Menggabungkan dataset : Melakukan inner join pada dataset peringkat dan dataset netflix untuk mendapatkan konten yang memiliki peringkat di IMDB dan tersedia di Netflix.
- Normalisasi data : Mengubah data menjadi huruf kecil dan menghapus spasi pada sebuah data.

## Modeling and Result
---

- Proses yang saya lakukan pada data ini adalah dengan membuat Algoritma machine learning, yaitu Content based filtering.
  * Content based filtering pada beberapa metrik.
    - Faktor yang digunakan pada filtering kali ini adalah : Title, Cast, Director, Listed in, Plot.
    - Hasil dari modeling menggunakan Content Based Filtering :
    <br>
    <image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/5.png' width= 500/> <p>
   dari hasil di atas dapat dilihat bahwa ketika memerlukan rekomendasi film yang mirip dengan kata kunci yang kita masukan, maka sistem akan merekomendasikan film yang mirip.

## Evaluation
---
- Hasil Evaluasi Content Based Filtering
Pada evaluasi model ini penulis menggunakan metrik precision content based filtering untuk menghitung precision model sistem telah dibuat sebelumnya. Berikut ini adalah hasil analisisnya:

- Film yang digunakan untuk metrics precision 'Casino Tycoon 2' :
<br>
    <image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/8.png'/> <p>
    
- Hasil 10 film yang direkomendasikan oleh sistem :
<br>
    <image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/9.png'/> <p>

Langkah pertama adalah melakukan pengecekan data film berdasarkan title. Dapat dilihat bahwa judul film Casino Tycoon 2 memiliki 3 genre yaitu Action & Adventure, Dramas, dan International Movies. Lalu memiliki rating film yaitu *TV-MA*, dan memiliki tipe konten adalah *Movie* . Setelah itu dari hasil rekomendasi di atas, diketahui bahwa Casino Tycoon 2 memiliki 3 genre,rating *TV-MA*,tipe konten *Movie*. dan dari 10 film yang direkomendasikan, 10 film memiliki kategori 3 genre,dan tipe konten yang sama (similar). tetapi pada 10 film yang direkomendasikan ada 1 rating film yang berbeda.
Artinya, precision sistem kita sebesar 9/10 atau sebesar 90%.

Metrics Precision Formula :
<br>
    <image src='https://raw.githubusercontent.com/Hanifanta/Recommendation_System_Netflix/main/images/7.png'/> <p>
    
# Referensi :
---

* Munawar, Yosua Riadi Silitonga (2019). SISTEM PENDETEKSI BERITA HOAX DI MEDIA SOSIAL DENGAN TEKNIK DATA MINING SCIKIT LEARN.
* Sounak Bhattacharya, Ankit Lundia  (2019). MOVIE RECOMMENDATION SYSTEM USING BAG OF WORDS AND SCIKIT-LEARN.
