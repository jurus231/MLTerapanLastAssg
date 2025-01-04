
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

# Memuat Dataset
game_df = pd.read_csv("https://raw.githubusercontent.com/jurus231/MLTerapanLastAssg/refs/heads/main/games.csv")
print(game_df)

# Deskripsi Data
print(game_df.describe())

# Mengecek Missing Values dan Tipe Data
print(game_df.isna().sum())
print(game_df.dtypes)

# Exploratory Data Analysis
# Visualisasi distribusi rating
plt.figure(figsize=(8, 5))
sns.countplot(data=game_df, x='rating', order=game_df['rating'].value_counts().index)
plt.title('Distribusi Rating Game')
plt.xlabel('Rating')
plt.ylabel('Jumlah Game')
plt.xticks(rotation=90)  # Rotate x-axis labels to vertical
plt.show()

# Visualisasi distribusi harga menggunakan scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x=game_df.index, y=game_df['price_final'], alpha=0.7, color='b')
plt.title('Distribusi Harga Game')
plt.xlabel('Index Game')
plt.ylabel('Harga (USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Top 10 game dengan ulasan terbanyak
top_reviewed_games = game_df[['title', 'user_reviews']].sort_values(by='user_reviews', ascending=False).head(10)
print("Top 10 game dengan jumlah ulasan terbanyak:", top_reviewed_games)

# Visualisasi
plt.figure(figsize=(10, 5))
sns.barplot(data=top_reviewed_games, y='title', x='user_reviews', palette='viridis')
plt.title('Top 10 Game Berdasarkan Jumlah Ulasan')
plt.xlabel('Jumlah Ulasan')
plt.ylabel('Judul Game')
plt.show()

# Visualisasi distribusi rasio ulasan positif
plt.figure(figsize=(8, 5))
sns.histplot(data=game_df, x='positive_ratio', bins=30, kde=True)
plt.title('Distribusi Rasio Ulasan Positif')
plt.xlabel('Rasio Ulasan Positif (%)')
plt.ylabel('Jumlah Game')
plt.show()

# Content-Based Filtering
# Konversi kolom rating ke skor numerik
rating_map = {
    'Very Positive': 5,
    'Positive': 4,
    'Mixed': 3,
    'Negative': 2,
    'Very Negative': 1
}
game_df['rating_score'] = game_df['rating'].map(rating_map)

# Normalisasi kolom positive_ratio dan user_reviews
scaler = MinMaxScaler()
game_df['positive_ratio_scaled'] = scaler.fit_transform(game_df[['positive_ratio']])
game_df['user_reviews_scaled'] = scaler.fit_transform(game_df[['user_reviews']])

# Menyiapkan fitur
features = game_df[['positive_ratio_scaled', 'user_reviews_scaled', 'rating_score']]

# Mengisi NaN dengan rata-rata kolom
features = features.fillna(features.mean())

# Membangun model KNN
knn = NearestNeighbors(n_neighbors=10)  # 10 tetangga terdekat
knn.fit(features)

# Menemukan rekomendasi untuk game tertentu
def recommend_games_knn(game_title, dataset, knn_model):
    game = dataset[dataset['title'] == game_title]
    
    if game.empty:
        return "Game tidak ditemukan."
    
    # Menemukan tetangga terdekat
    distances, indices = knn_model.kneighbors(game[['positive_ratio_scaled', 'user_reviews_scaled', 'rating_score']])
    
    # Mendapatkan rekomendasi game berdasarkan index
    recommended_titles = dataset.iloc[indices[0]]['title']
    return recommended_titles

# Contoh rekomendasi
game_title = "ELDEN RING"
recommended_games = recommend_games_knn(game_title, game_df, knn)
print("Rekomendasi untuk game:", game_title)
print(recommended_games)
