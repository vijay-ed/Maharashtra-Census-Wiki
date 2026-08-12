# Maharashtra Census Wiki

A Flask web application for generating village-level Maharashtra Census information and Wikipedia-style articles.

## Main features

- Searches the Maharashtra Census village database by village code/name.
- Uses SQLite (`census_data/census.db`) so the web application does not load the entire large CSV into memory.
- Generates village information using the existing `Census_Wiki_Vill.py` logic.
- Includes the required district `.pkl` language/translation data.

## Deployment

The application is configured for deployment on Render.

Start command:

```text
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

The large source CSV is not required by the deployed web application. The SQLite database is used instead.

## Important files

- `app.py` — Flask web application
- `Census_Wiki_Vill.py` — village article generation logic
- `build_database.py` — utility for creating the SQLite database from the source CSV
- `census_data/census.db` — SQLite census database
- `render.yaml` — Render deployment configuration
- `requirements.txt` — Python dependencies
- `templates/` — web page templates

## Local use

Install dependencies:

```text
pip install -r requirements.txt
```

Run locally:

```text
python app.py
```

Then open the local address displayed by Flask.
