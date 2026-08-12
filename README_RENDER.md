# Maharashtra Census Wiki – Render Deployment

This package converts the original command-line Census_Wiki_Vill.py application into a Flask web application.

## Local test

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/`.

## Render

Create a **Web Service** from the GitHub repository.

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

Use the Free instance if available.

## Project structure

- `app.py` – Flask web application
- `Census_Wiki_Vill.py` – original article-generation logic
- `templates/index.html` – Marathi user interface
- `templates/about.html` – source/disclaimer page
- `census_data/mah_vill_census_data.csv` – Census 2011 data
- `census_data/e_m_list_*.pkl` – district-wise English-to-Marathi mappings

## Notes

The public UI displays Marathi district/taluka/village names where mappings are available and falls back to Census spellings where they are not. The selected place names are also normalized in the generated article. The underlying Census figures are not changed.
