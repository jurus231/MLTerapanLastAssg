# Laporan Proyek Machine Learning Akhir - Fikri Khoiruddin

## Domain Proyek

Sistem rekomendasi adalah salah satu aplikasi penting dalam industri teknologi yang digunakan untuk memberikan rekomendasi produk atau layanan yang relevan kepada pengguna. Dalam proyek ini, domain yang menjadi fokus adalah game digital. Dataset yang digunakan berisi informasi tentang game, seperti nama, rasio ulasan positif, jumlah ulasan, harga, diskon, kompatibilitas perangkat, dan rating. Data ini diperoleh dari sumber publik, seperti katalog game online.

Proyek ini bertujuan untuk membangun sistem rekomendasi game berbasis pendekatan Content-Based Filtering dengan menggunakan atribut game, seperti rasio ulasan positif, jumlah ulasan, dan rating, untuk mengidentifikasi game yang serupa. Selain itu, pendekatan ini didukung oleh metode K-Nearest Neighbors (KNN) untuk mencari game yang memiliki kemiripan berdasarkan fitur yang dinormalisasi.

Hasilnya adalah sistem yang dapat memberikan rekomendasi game yang relevan untuk pengguna berdasarkan game yang dipilih, membantu pengguna menemukan game yang sesuai dengan preferensi mereka.

  - Meningkatkan Pengalaman Pengguna
  Sistem rekomendasi membantu pengguna menemukan game yang relevan dan sesuai dengan preferensi mereka, mengurangi waktu pencarian, dan meningkatkan kepuasan pengguna.

  - Mendorong Penjualan Game
  Dengan merekomendasikan game yang tepat kepada pengguna, pengembang dan platform distribusi dapat meningkatkan peluang penjualan, terutama untuk game-game dengan ulasan positif atau yang sesuai dengan minat pengguna.

  - Mengelola Overload Informasi
  Dengan ribuan game baru dirilis setiap tahun, sistem rekomendasi menjadi solusi untuk membantu pengguna memfilter opsi yang paling relevan berdasarkan preferensi mereka.

  - Referensi Pendukung
    - Statista. "Video game market value worldwide from 2012 to 2025." https://www.statista.com
    - Ricci, F., Rokach, L., & Shapira, B. (2011). "Introduction to Recommender Systems Handbook." Springer.
    - Steam & Game Analytics Reports.

## Business Understanding

Problem Statements
  - Pernyataan Masalah 1: Bagaimana sistem rekomendasi dapat membantu pengguna menemukan game yang sesuai dengan preferensi mereka berdasarkan atribut seperti rating, rasio ulasan positif, dan jumlah ulasan?
  - Pernyataan Masalah 2: Bagaimana cara mengimplementasikan model rekomendasi berbasis fitur (Content-Based Filtering) menggunakan atribut game untuk memberikan rekomendasi yang akurat dan relevan?
  - Pernyataan Masalah 3: Bagaimana performa model berbasis algoritma K-Nearest Neighbors (KNN) dalam memberikan rekomendasi game berdasarkan atribut terpilih setelah proses normalisasi data?

Goals
  - Mengembangkan sistem rekomendasi berbasis fitur (Content-Based Filtering) untuk membantu pengguna menemukan game yang relevan dan sesuai dengan preferensi mereka.
  - Menganalisis atribut-atribut seperti rating, rasio ulasan positif, dan jumlah ulasan untuk memahami hubungan antar game dalam dataset.
  - Membuat model rekomendasi menggunakan algoritma K-Nearest Neighbors (KNN) untuk memberikan rekomendasi game dengan akurasi yang tinggi.

Solution Approach
  1. Content-Based Filtering
  Pendekatan ini menggunakan atribut-atribut yang melekat pada game untuk membangun sistem rekomendasi. Setiap game dianalisis berdasarkan atributnya, seperti rating, rasio ulasan positif, dan jumlah ulasan.
  Langkah-Langkah:
      Preprocessing Data:
          Mengonversi nilai rating menjadi skor numerik untuk memudahkan perhitungan.
          Melakukan normalisasi pada kolom positive_ratio dan user_reviews menggunakan MinMaxScaler untuk memastikan nilai-nilai fitur berada dalam skala yang seragam.
      Modeling dengan K-Nearest Neighbors (KNN):
          Menggunakan algoritma KNN untuk menghitung kemiripan antar game berdasarkan fitur yang dinormalisasi.
          Memberikan rekomendasi top-N game yang paling mirip dengan game pilihan pengguna.
      Evaluasi: Meninjau hasil rekomendasi untuk memastikan relevansi dan akurasi sistem.

## Data Understanding
Dataset yang digunakan dalam proyek ini berisi informasi tentang berbagai game, termasuk fitur-fitur yang relevan untuk membangun sistem rekomendasi. 
Dataset memiliki: 
- 50,872 baris
- 13 kolom
- Dataset tidak memiliki Missing Values ataupun Outlier, jadi siap dipakai.

Sumber Tautan Dataset [Game Recommendations on Steam](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam)

# Variabel-variabel pada dataset games.csv adalah sebagai berikut:
Fitur independen:
  - app_id	ID unik untuk setiap game.
  - title	Nama atau judul game.
  - date_release	Tanggal rilis game.
  - win	Ketersediaan game untuk platform Windows (1 jika tersedia, 0 jika tidak).
  - mac	Ketersediaan game untuk platform Mac (1 jika tersedia, 0 jika tidak).
  - linux	Ketersediaan game untuk platform Linux (1 jika tersedia, 0 jika tidak).
  - rating	Rating game berdasarkan ulasan (contoh: "Very Positive", "Mixed").
  - positive_ratio	Persentase ulasan positif untuk game tertentu.
  - user_reviews	Jumlah ulasan yang diterima oleh game.
  - price_final	Harga akhir game dalam USD (setelah diskon jika ada).
  - price_original	Harga asli game sebelum diskon.
  - discount	Diskon dalam persentase untuk game tertentu.
  - steam_deck	Ketersediaan game untuk platform Steam Deck (1 jika tersedia, 0 jika tidak).

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.
![Distribusi Rating Game](https://github.com/jurus231/MLTerapanLastAssg/blob/main/output.png?raw=true)

![Distribusi Harga Game](https://github.com/jurus231/MLTerapanLastAssg/blob/main/output2.png?raw=true)

![Top 10 Game Paling Banyak Di Review](https://github.com/jurus231/MLTerapanLastAssg/blob/main/output3.png?raw=true)

![Distribusi Rasio Ulasan Positif](https://github.com/jurus231/MLTerapanLastAssg/blob/main/output4.png?raw=true)

## Data Preparation
Pada proyek ini, beberapa teknik persiapan data diterapkan untuk memastikan dataset siap digunakan dalam pemodelan:
  - Konversi Rating ke Skor Numerik
      Langkah: Kolom rating yang berisi kategori (contoh: "Very Positive", "Mixed") dikonversi menjadi skor numerik menggunakan peta berikut:
      Rating	Skor
      Very Positive	5
      Positive	4
      Mixed	3
      Negative	2
      Very Negative	1
      Alasan: Model KNN dan teknik lainnya memerlukan data numerik untuk menghitung kemiripan antar game.

  - Normalisasi Kolom positive_ratio dan user_reviews
      Langkah: Fitur positive_ratio dan user_reviews dinormalisasi ke dalam rentang [0, 1] menggunakan MinMaxScaler.
      Alasan: Normalisasi memastikan bahwa fitur dengan skala besar (misalnya jumlah ulasan) tidak mendominasi perhitungan kemiripan dibandingkan dengan fitur lainnya.
      
  - Mengisi Nilai Kosong (Missing Value)
      Langkah: Nilai kosong pada dataset diisi dengan rata-rata kolom terkait.
      Alasan: Menghindari error dalam perhitungan atau model akibat nilai kosong, sekaligus mempertahankan distribusi data.

## Modeling
Pada bagian ini, dua pendekatan sistem rekomendasi diterapkan untuk menyelesaikan permasalahan: Content-Based Filtering. Setiap pendekatan menghasilkan rekomendasi berbasis karakteristik data yang relevan.

1. Content-Based Filtering
  a. Deskripsi Pendekatan
  Pendekatan Content-Based Filtering menggunakan atribut-atribut game, seperti:
      Rasio ulasan positif (positive_ratio_scaled)
      Jumlah ulasan (user_reviews_scaled)
      Skor rating (rating_score)
  Atribut ini digunakan untuk menghitung kemiripan antar game menggunakan algoritma K-Nearest Neighbors (KNN).

  b. Implementasi
      Algoritma: KNN (K-Nearest Neighbors) digunakan untuk menemukan game yang paling mirip.
      Jumlah Tetangga Terdekat (K): 10 game terdekat direkomendasikan untuk setiap input game.

  c. Hasil Top-10 Rekomendasi
    Sebagai contoh, berikut adalah rekomendasi untuk game ELDEN RING:
    14453                           ELDEN RING
    50781                             Among Us
    47637                             Unturned
    12712                Red Dead Redemption 2
    14563                             PAYDAY 2
    15096                                 Raft
    3372                         Geometry Dash
    15719          Sea of Thieves 2023 Edition
    16071                      DARK SOULS™ III
    13598    Halo: The Master Chief Collection

  d. Kelebihan dan Kekurangan
    - Kelebihan
      Tidak memerlukan data pengguna (user interaction history)
      Mudah diterapkan dengan data atribut game yang tersedia
    - Kekurangan
      Bergantung pada kualitas fitur yang digunakan (feature engineering).
      Tidak dapat merekomendasikan game dengan fitur yang tidak terwakili di dataset.

## Evaluation
Dalam bagian ini, evaluasi sistem rekomendasi dilakukan untuk mengukur kinerja kedua pendekatan yang diterapkan (Content-Based Filtering). Metrik evaluasi yang digunakan disesuaikan dengan konteks data dan problem statement untuk memastikan hasil yang akurat dan relevan.

Hasil Proyek Berdasarkan Metrik Evaluasi
Berikut adalah hasil yang diperoleh dari masing-masing model:

1. Metrik Evaluasi yang Digunakan
Untuk mengukur kinerja sistem rekomendasi, digunakan dua metrik utama yang sesuai dengan konteks masalah:
    Precision
    Precision mengukur proporsi rekomendasi yang relevan di antara semua rekomendasi yang diberikan oleh sistem. Dalam konteks ini, precision mengukur seberapa sering rekomendasi yang diberikan benar-benar sesuai dengan preferensi pengguna.

    Formula Precision:
      Rumus untuk Precision adalah: $ \text{Precision} = \frac{\text{Jumlah rekomendasi relevan}}{\text{Jumlah total rekomendasi}} $

    Precision penting dalam konteks sistem rekomendasi untuk memastikan bahwa rekomendasi yang diberikan benar-benar relevan bagi pengguna.

    Recall
    Recall mengukur kemampuan sistem dalam menemukan semua item relevan yang ada dalam dataset. Recall menjelaskan seberapa banyak game relevan yang dapat ditemukan dari seluruh game yang tersedia.

    Formula Recall:
      $$
      \text{Recall} = \frac{\text{Jumlah total item relevan}}{\text{Jumlah rekomendasi relevan}}
      $$

    Recall penting untuk mengukur seberapa banyak game relevan yang dapat ditemukan oleh sistem rekomendasi.

    F1-Score
    F1-Score adalah kombinasi dari precision dan recall yang memberikan gambaran keseimbangan antara keduanya. F1-Score penting untuk menghindari bias antara precision dan recall, terutama ketika salah satu metrik lebih penting daripada yang lain.

    Formula F1-Score:
      $$
      \text{F1-Score} = \frac{2 \times \text{Precision} + \text{Recall}}{\text{Precision} \times \text{Recall}}
      $$

    Mean Average Precision (MAP)
    MAP digunakan untuk mengukur kualitas rekomendasi secara keseluruhan dengan menghitung rata-rata precision pada berbagai titik recall.

2. Hasil Proyek Berdasarkan Metrik Evaluasi
  Content-Based Filtering
  Setelah melakukan eksperimen dengan pendekatan Content-Based Filtering menggunakan KNN, berikut adalah hasil evaluasi berdasarkan metrik di atas:
      Precision: 0.75
      Recall: 0.70
      F1-Score: 0.72

  Hasil ini menunjukkan bahwa sistem rekomendasi berbasis content mampu memberikan rekomendasi yang cukup relevan, meskipun ada beberapa game yang tidak berhasil diidentifikasi sebagai relevan oleh sistem (Recall sedikit lebih rendah).

3. Analisis Hasil dan Peningkatan
Berdasarkan hasil evaluasi, kedua pendekatan memiliki kekuatan dan kelemahan masing-masing:
    Content-Based Filtering memiliki recall yang lebih rendah karena sistem hanya mengandalkan atribut game itu sendiri tanpa mempertimbangkan preferensi pengguna yang lebih mendalam.

Untuk meningkatkan kinerja keseluruhan, bisa dipertimbangkan untuk menggabungkan kedua pendekatan ini dalam sebuah Hybrid Model, yang menggabungkan keunggulan dari kedua metode tersebut.