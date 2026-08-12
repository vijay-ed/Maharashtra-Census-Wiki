from flask import Flask, render_template, request, jsonify, Response
from pathlib import Path
import importlib.util
import pickle
import codecs
import sys
from decimal import Decimal
from collections import Counter
import pandas as pd

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / "census_data"
CSV_FILE = DATA_DIR / "mah_vill_census_data.csv"

app = Flask(__name__)

# Import the user's existing article-generation program without running its CLI.
spec = importlib.util.spec_from_file_location("census_wiki", BASE / "Census_Wiki_Vill.py")
cw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cw)
cw.pd = pd
cw.pickle = pickle
cw.codecs = codecs
cw.Decimal = Decimal
cw.sys = sys

print("Loading Census India data...")
df = pd.read_csv(CSV_FILE, low_memory=False)
print(f"Loaded {len(df):,} village records.")

# Standard Marathi names for Maharashtra's Census-2011 district names.
# These are used for the public-facing interface and as a reliable fallback
# when a district name is not present in a district's village translation file.
DISTRICT_MARATHI = {
    "Ahmadnagar": "अहमदनगर", "Akola": "अकोला", "Amravati": "अमरावती",
    "Aurangabad": "औरंगाबाद", "Beed": "बीड", "Bhandara": "भंडारा",
    "Buldana": "बुलढाणा", "Chandrapur": "चंद्रपूर", "Dhule": "धुळे",
    "Gadchiroli": "गडचिरोली", "Gondiya": "गोंदिया", "Hingoli": "हिंगोली",
    "Jalgaon": "जळगाव", "Jalna": "जालना", "Kolhapur": "कोल्हापूर",
    "Latur": "लातूर", "Mumbai (Suburban)": "मुंबई उपनगर", "Mumbai": "मुंबई",
    "Nagpur": "नागपूर", "Nanded": "नांदेड", "Nandurbar": "नंदुरबार",
    "Nashik": "नाशिक", "Osmanabad": "उस्मानाबाद", "Parbhani": "परभणी",
    "Pune": "पुणे", "Raigarh": "रायगड", "Ratnagiri": "रत्नागिरी",
    "Sangli": "सांगली", "Satara": "सातारा", "Sindhudurg": "सिंधुदुर्ग",
    "Solapur": "सोलापूर", "Thane": "ठाणे", "Wardha": "वर्धा",
    "Washim": "वाशिम", "Yavatmal": "यवतमाळ",
}

DISTRICTS = sorted(df["District Name"].dropna().astype(str).unique().tolist())
EM_CACHE = {}
DISTRICT_TRANSLATION_CACHE = {}
TALUKA_TRANSLATION_CACHE = {}
VILLAGE_TRANSLATION_CACHE = {}


def normalize_text(value):
    if value is None or pd.isna(value):
        return ""
    return str(value).strip()


def load_em_list(dist_code):
    key = str(int(dist_code)) if str(dist_code).replace('.', '', 1).isdigit() else str(dist_code)
    if key not in EM_CACHE:
        path = DATA_DIR / f"e_m_list_{key}.pkl"
        try:
            with open(path, "rb") as f:
                EM_CACHE[key] = pickle.load(f)
        except FileNotFoundError:
            EM_CACHE[key] = []
    return EM_CACHE[key]


def build_translation_maps(dist_code):
    """Build best-effort English->Marathi maps from the district's pkl file."""
    key = str(int(dist_code)) if str(dist_code).replace('.', '', 1).isdigit() else str(dist_code)
    if key in DISTRICT_TRANSLATION_CACHE:
        return DISTRICT_TRANSLATION_CACHE[key]

    rows = load_em_list(dist_code)
    counts = {}
    for row in rows:
        if len(row) < 4:
            continue
        en, mr = normalize_text(row[2]), normalize_text(row[3])
        if en and mr:
            counts.setdefault(en, Counter())[mr] += 1

    best = {en: counter.most_common(1)[0][0] for en, counter in counts.items()}
    DISTRICT_TRANSLATION_CACHE[key] = best
    return best


def translate_name(name, dist_code):
    name = normalize_text(name)
    if not name:
        return name
    if name in DISTRICT_MARATHI:
        return DISTRICT_MARATHI[name]
    return build_translation_maps(dist_code).get(name, name)


def get_district_code(district):
    rows = df.loc[df["District Name"].astype(str).eq(district), "District Code"]
    if rows.empty:
        return None
    return rows.iloc[0]


def get_talukas(district):
    x = df.loc[df["District Name"].astype(str) == district, "Sub District Name"]
    return sorted(x.dropna().astype(str).unique().tolist())


def get_villages(district, taluka):
    mask = (df["District Name"].astype(str) == district) & (df["Sub District Name"].astype(str) == taluka)
    x = df.loc[mask, "Village Name"]
    return sorted(x.dropna().astype(str).unique().tolist())


def get_display_talukas(district):
    code = get_district_code(district)
    rows = []
    for name in get_talukas(district):
        rows.append({"value": name, "label": translate_name(name, code) if code is not None else name})
    return rows


def get_display_villages(district, taluka):
    code = get_district_code(district)
    rows = []
    mapping = build_translation_maps(code) if code is not None else {}
    for name in get_villages(district, taluka):
        rows.append({"value": name, "label": mapping.get(name, name)})
    return rows


def generate_article(village, taluka, district):
    mask = (
        df["Village Name"].astype(str).eq(village)
        & df["Sub District Name"].astype(str).eq(taluka)
        & df["District Name"].astype(str).eq(district)
    )
    selected = df.loc[mask].copy()
    if selected.empty:
        raise ValueError("The selected village was not found in the Census data.")

    cw.df = selected
    cw.i = 0
    dist_code = selected.iloc[0, 2]

    # Keep the original program's replacement behavior so its article remains
    # compatible with the user's existing Marathi Wikipedia formatting.
    for x in load_em_list(dist_code):
        if len(x) >= 4:
            e_text, m_text = x[2], x[3]
            if pd.notna(e_text) and pd.notna(m_text):
                cw.df.replace(e_text, m_text, inplace=True)
                cw.df.replace(str(e_text).upper(), m_text, inplace=True)

    if cw.df.iat[0, 25] == 0:
        raise ValueError("Population data are not available for this village; an article cannot be generated.")

    article = cw.main()

    # Guarantee consistent public-facing names for the selected district,
    # taluka and village even when a name was absent from the translation list.
    mr_district = DISTRICT_MARATHI.get(district, district)
    mr_taluka = translate_name(taluka, dist_code)
    mr_village = build_translation_maps(dist_code).get(village, village)

    replacements = [(district, mr_district), (taluka, mr_taluka), (village, mr_village)]
    for en, mr in replacements:
        if en and mr and en != mr:
            article = article.replace(en, mr)

    return article


@app.route("/")
def index():
    district_options = [{"value": d, "label": DISTRICT_MARATHI.get(d, d)} for d in DISTRICTS]
    return render_template("index.html", districts=district_options)


@app.get("/api/talukas")
def api_talukas():
    district = request.args.get("district", "")
    if district not in DISTRICTS:
        return jsonify([])
    return jsonify(get_display_talukas(district))


@app.get("/api/villages")
def api_villages():
    district = request.args.get("district", "")
    taluka = request.args.get("taluka", "")
    if district not in DISTRICTS or not taluka:
        return jsonify([])
    return jsonify(get_display_villages(district, taluka))


@app.post("/generate")
def generate():
    district = request.form.get("district", "").strip()
    taluka = request.form.get("taluka", "").strip()
    village = request.form.get("village", "").strip()
    try:
        if not district or not taluka or not village:
            raise ValueError("कृपया जिल्हा, तालुका आणि गाव निवडा.")
        article = generate_article(village, taluka, district)
        district_label = DISTRICT_MARATHI.get(district, district)
        taluka_label = translate_name(taluka, get_district_code(district))
        village_label = build_translation_maps(get_district_code(district)).get(village, village)
        return render_template(
            "index.html",
            districts=[{"value": d, "label": DISTRICT_MARATHI.get(d, d)} for d in DISTRICTS],
            selected_district=district,
            selected_taluka=taluka,
            selected_village=village,
            selected_district_label=district_label,
            selected_taluka_label=taluka_label,
            selected_village_label=village_label,
            article=article,
        )
    except Exception as exc:
        return render_template(
            "index.html",
            districts=[{"value": d, "label": DISTRICT_MARATHI.get(d, d)} for d in DISTRICTS],
            selected_district=district,
            selected_taluka=taluka,
            selected_village=village,
            error=str(exc),
        ), 400


@app.post("/download")
def download():
    article = request.form.get("article", "")
    if not article:
        return Response("No article supplied.", status=400, mimetype="text/plain; charset=utf-8")
    return Response(
        article,
        mimetype="text/plain; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=marathi_village_wikipedia_article.txt"},
    )


@app.get("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
