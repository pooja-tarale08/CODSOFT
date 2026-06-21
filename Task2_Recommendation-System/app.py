import pandas as pd
import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)
# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Average ratings
movie_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
movie_ratings.rename(columns={"rating": "avg_rating"}, inplace=True)

movies_with_ratings = movies.merge(
    movie_ratings,
    on="movieId",
    how="left"
)

# Feature extraction
movies["genres"] = movies["genres"].fillna("")

cv = CountVectorizer()
genre_matrix = cv.fit_transform(movies["genres"])

similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_name):

    movie_index = movies[movies["title"] == movie_name].index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie in similarity_scores[1:6]:

        movie_data = movies_with_ratings.iloc[movie[0]]

        recommendations.append({
            "title": movie_data["title"],
            "rating": round(movie_data["avg_rating"],2),
            "genre": movie_data["genres"]
        })

    return recommendations

# Streamlit UI
# UI

st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies similar to your favourite movie using Machine Learning"
)


selected_movie = st.selectbox(
    "🔍 Select a Movie",
    movies["title"].values
)


if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader(
        f"Movies similar to {selected_movie}"
    )

    cols = st.columns(5)

    for index, movie in enumerate(recommendations):

        with cols[index]:

            st.markdown(
                f"""
                ### 🎥 {movie['title']}

                ⭐ Rating: {movie['rating']}

                🎭 Genre:
                {movie['genre']}
                """
            )