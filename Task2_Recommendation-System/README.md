# 🎬 Movie Recommendation System

A Machine Learning based movie recommendation system that suggests similar movies using **Content-Based Filtering**. The system uses movie genres and ratings to recommend movies through an interactive **Streamlit** web application.

## 🚀 Features

- Select a movie and get similar movie recommendations
- Genre-based similarity analysis
- Displays average movie ratings
- Interactive Streamlit UI

## 🧠 How It Works

1. Load MovieLens movie and ratings dataset
2. Preprocess movie genres and ratings
3. Convert genres into numerical features using **CountVectorizer**
4. Calculate similarity using **Cosine Similarity**
5. Recommend top similar movies

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── data
│   ├── movies.csv
│   └── ratings.csv
├── notebooks
│   └── EDA.ipynb
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🔮 Future Improvements

- Add collaborative filtering
- Improve recommendation accuracy
- Deploy using Streamlit Cloud
- Add personalized recommendations

## 👩‍💻 Author

**Pooja Tarale**