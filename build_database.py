from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / 'census_data'
CSV_FILE = DATA_DIR / 'mah_vill_census_data.csv'
DB_FILE = DATA_DIR / 'census.db'

CHUNK_SIZE = 5000


def main():
    if DB_FILE.exists():
        DB_FILE.unlink()

    conn = sqlite3.connect(DB_FILE)
    try:
        first = True
        total = 0
        for chunk in pd.read_csv(CSV_FILE, low_memory=False, chunksize=CHUNK_SIZE):
            chunk.to_sql('villages', conn, if_exists='replace' if first else 'append', index=False)
            total += len(chunk)
            first = False
            print(f'Imported {total:,} rows')

        conn.execute('CREATE INDEX IF NOT EXISTS idx_villages_district ON villages("District Name")')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_villages_district_taluka ON villages("District Name", "Sub District Name")')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_villages_lookup ON villages("District Name", "Sub District Name", "Village Name")')
        conn.commit()
        print(f'Database created: {DB_FILE}')
        print(f'Rows: {total:,}')
    finally:
        conn.close()


if __name__ == '__main__':
    main()
