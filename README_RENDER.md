# Render Deployment — Maharashtra Census Wiki

## Purpose

This version is optimized for Render's limited-memory environment.

The previous version could load the complete Maharashtra Census CSV into Pandas at application startup. That could consume enough memory for Render to terminate the process with **Exit status 137**.

This version uses:

```text
SQLite database → query required village → Pandas DataFrame for that village only
```

## Render settings

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

The `render.yaml` file contains the deployment configuration.

## Database

The deployed application uses:

```text
census_data/census.db
```

The application should not load the complete `mah_vill_census_data.csv` into memory during normal web requests.

## Before pushing to GitHub

Make sure `census.db` is included in the repository. The large CSV should not be committed as an ordinary Git blob.

If Git LFS is used for the source CSV in your development copy, that is separate from the SQLite database required by the deployed application.

## Troubleshooting Exit status 137

If Render again reports:

```text
Exited with status 137
```

check the application logs for any code that reads the entire CSV with `pandas.read_csv()` at startup. The deployed application should use the SQLite database instead.

## Deployment sequence

1. Replace the old application files with this corrected version.
2. Confirm `census_data/census.db` exists.
3. Commit and push the changes to GitHub.
4. In Render, deploy the latest commit.
5. Check the deployment logs.
6. Test the village search and article generation.
