from flask import Flask, render_template, request
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

app = Flask(__name__)

# Initialize Spark session
spark = SparkSession.builder.appName("MoodMovieSpark").getOrCreate()

# Load movies CSV into Spark DataFrame
movies_df = spark.read.csv("movies.csv", header=True, inferSchema=True)

# Debug: check CSV columns
print("Columns in movies CSV:", movies_df.columns)

# Emoji mapping for moods
emojis = {
    "happy": "😄",
    "sad": "😢",
    "excited": "🤩",
    "funny": "😂",
    "emotional": "😭",
    "scared": "😱"
}

# Supported languages
languages = ["English", "Hindi", "Spanish", "French", "Japanese", "Korean"]

# -------------------------------
# HOME / WELCOME PAGE
# -------------------------------
@app.route("/")
def home():
    return render_template("welcome.html")  # Welcome page

# -------------------------------
# MOOD SELECTION PAGE
# -------------------------------
@app.route("/mood_select")
def mood_select():
    return render_template(
        "mood_select.html",
        moods=list(emojis.keys()),
        emojis=emojis,
        languages=languages
    )

# -------------------------------
# RECOMMENDATION PAGE
# -------------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    selected_mood = request.form.get("mood")
    language = request.form.get("language")  # Single language

    # Filter movies based on mood and language
    filtered = movies_df.filter(
        (col("mood") == selected_mood) & (col("language") == language)
    )

    # Convert Spark DataFrame rows to list of dicts
    movies = [row.asDict() for row in filtered.collect()]

    return render_template(
        "movies.html",
        mood=selected_mood,
        language=language,
        movies=movies,
        emojis=emojis
    )

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
