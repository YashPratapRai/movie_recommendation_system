# 🎬 Movie Recommendation System

A full-stack Movie Recommendation System built using **TF-IDF based content filtering**, integrated with **TMDB API** for real-time movie metadata, and deployed using **FastAPI (backend)** and **Streamlit (frontend)**.

The system processes a dataset of **45,466 movies** and generates intelligent recommendations based on movie overview, genres, and tagline.

---

## 🚀 Live Demo
https://movierecommendationsystem-yashprataprai.streamlit.app/

---

## 📌 Project Overview

This project implements a **Content-Based Recommendation System** using:

- TF-IDF Vectorization (Unigram + Bigram)
- Cosine Similarity
- Text preprocessing with NLTK (Stopword removal + Lemmatization)
- FastAPI backend for scalable API architecture
- TMDB API integration for posters, metadata, and details
- Streamlit frontend for interactive UI

---

## 🗂 Dataset

- Source: `movies_metadata.csv`
- Total Movies: **45,466**
- Features Used:
  - Title
  - Overview
  - Genres
  - Tagline
  - Vote Average
  - Popularity

---

## ⚙️ Data Processing Pipeline

1. Removed duplicates
2. Handled missing values
3. Parsed genres using `ast.literal_eval`
4. Combined overview + genres + tagline into `tags`
5. Text preprocessing:
   - Lowercasing
   - Punctuation removal
   - Stopword removal
   - Lemmatization (WordNet)
6. Vectorization using:

---

## 🤖 Recommendation Logic

- Convert movie tags into TF-IDF vectors
- Compute cosine similarity between selected movie and all others
- Sort similarity scores
- Return top N similar movies

Additionally:
- Genre-based recommendations (via TMDB)
- Fallback logic if TF-IDF results unavailable

---

## 🏗 Architecture
User → Streamlit UI → FastAPI Backend →TF-IDF Model + TMDB API → Recommendations

---

## 🌐 TMDB API Integration

Used TMDB API to:

- Fetch real-time posters
- Retrieve movie details (release date, genres, overview)
- Provide trending / popular / top-rated sections
- Improve user experience beyond static dataset

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy

### NLP
- TF-IDF Vectorizer
- Cosine Similarity
- NLTK (Stopwords + Lemmatization)

### Frontend
- Streamlit
- Requests

### External API
- TMDB API

---

## 📦 Project Structure
movie-recommendation-system/
│
├── backend/
│ ├── main.py
│ ├── tfidf_matrix.pkl
│ ├── df.pkl
│ └── indices.pkl
│
├── app.py (Streamlit UI)
├── requirements.txt
└── README.md


---

## 🎯 Key Features

- 🔎 Smart search with autocomplete
- 🎬 Similar movie recommendations (TF-IDF)
- 🎭 Genre-based recommendations
- 📄 Detailed movie information page
- 🖼 Poster and backdrop display
- 🌍 Integrated with live TMDB data

---

## 📈 Future Improvements

- Collaborative filtering integration
- Hybrid recommendation system
- User rating-based personalization
- Model optimization for faster inference

---

## 👨‍💻 Author

Yash Pratap Rai  
Aspiring Data Scientist | Machine Learning Enthusiast
