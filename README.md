# Spark Mood Movie Recommender

A small Flask web app that uses PySpark to recommend movies based on the user's mood and preferred language. The application reads `movies.csv`, filters movies by mood and language using a Spark DataFrame, and renders results with Jinja2 templates.

**Project structure**
- `app.py`: Flask application and PySpark setup.
- `movies.csv`: Movie dataset used for recommendations.
- `templates/`: HTML templates (`welcome.html`, `mood_select.html`, `movies.html`, `result.html`, `base.html`).
- `static/`: Static assets (`script.js`, `style.css`).

## Prerequisites
- Python 3.8 or newer
- Java JDK 8 or 11 (required by Spark)
- pip (Python package installer)

Note: PySpark bundles Spark but requires Java. Ensure `java -version` works in your shell before running the app.

## Install dependencies
Open a PowerShell terminal and run:

```powershell
python -m pip install --upgrade pip
pip install flask pyspark
```

If you prefer a `requirements.txt`, create one with these lines:

```
flask
pyspark
```
and run `pip install -r requirements.txt`.

## Running the app
From the project root (where `app.py` and `movies.csv` are located) run:

```powershell
# start the app
python app.py
```

Then open your browser at: `http://localhost:8000/`

## How it works (brief)
- `app.py` creates a SparkSession and loads `movies.csv` into a Spark DataFrame.
- The `/mood_select` page presents mood and language options.
- Form submission to `/recommend` filters the Spark DataFrame by `mood` and `language`, collects matching rows, and renders `movies.html`.

## `movies.csv` format
The CSV should include at least the following columns (case-sensitive as used by the app):

- `title` — movie title
- `mood` — mood label (e.g., `happy`, `sad`, `excited`, `funny`, `emotional`, `scared`)
- `language` — language string (e.g., `English`, `Hindi`)

If your CSV contains additional columns (year, genre, rating), they will be available in templates if used.

## Development notes & troubleshooting
- If Spark fails to start, confirm Java is installed and `JAVA_HOME` is set (PowerShell example):

```powershell
# Example (adjust path to your JDK)
$env:JAVA_HOME = 'C:\\Program Files\\Java\\jdk-11.0.XX'
$env:PATH = $env:JAVA_HOME + '\\bin;' + $env:PATH
java -version
```

- On Windows, PySpark can be memory hungry. If you see out-of-memory errors, consider limiting driver/executor memory in Spark config or running on a machine with more RAM.
- If you add new rows to `movies.csv`, restart the Flask app so Spark reloads the file.

## Next steps / ideas
- Add a `requirements.txt` and a `venv`/virtualenv setup guide.
- Add unit tests for the recommendation filtering logic (mock Spark or use small test CSV).
- Add Dockerfile to containerize the app with a preinstalled JDK.

---

If you'd like, I can also add a `requirements.txt`, a quick `README` badge, or a Dockerfile next. Which would you prefer?
