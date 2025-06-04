# Movie-Recommend-System
🎬 Content-Based Movie Recommendation System with Streamlit

This project is a Content-Based Movie Recommendation System with an interactive Streamlit web interface. It suggests movies based on the content similarity of features like genre, overview, cast, and keywords. The user selects a movie, and the system returns the most similar titles.

🚀 Live Demo (Optional)
You can host this on platforms like Streamlit Cloud or Render for public access.

🔍 How It Works
Feature Engineering:
Combines text features (genres, overview, cast, keywords, etc.) into a single string for each movie.

Vectorization:
Converts combined text into numeric form using CountVectorizer.

Similarity Computation:
Calculates cosine similarity between all movie vectors.

Recommendation Logic:
When a user selects a movie, the top N similar movies are displayed.
🖥️ Streamlit Web Interface
Select a movie from a dropdown
View a list of recommended movies
🛠️ Tech Stack:
Python
numpy
Pandas, Scikit-learn
Streamlit (for UI)
