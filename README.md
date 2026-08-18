# Bluestock Mutual Fund Data Analysis & Visualisation Capstone

## Project Overview
This project delivers an end-to-end data engineering and analytics solution for Bluestock's Mutual Fund dataset. It encompasses pipeline automation (ETL), exploratory data analysis (EDA), portfolio performance evaluation, and interactive dashboarding.

---

## Setup Instructions

### 1. Prerequisites
* Python 3.9+
* Power BI Desktop / Tableau Desktop

### 2. Installation
```bash
git clone [https://github.com/your-username/Bluestock-MF-Capstone.git](https://github.com/your-username/Bluestock-MF-Capstone.git)
cd Bluestock-MF-Capstone
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

## Folder structure
```
mf-analytics/
├── data/
│   ├── raw/          # source CSVs + fetched NAV CSVs (gitignored by default)
│   └── processed/    # cleaned/derived data
├── notebooks/         # exploration notebooks
├── sql/                # SQL scripts / schema
├── dashboard/          # dashboard app code
├── reports/            # generated reports (data_quality_summary.txt lands here)
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── .gitignore
```

## Setup

```bash
cd mf-analytics
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 3 — Load your 10 CSVs

1. Copy your 10 provided CSV files into `data/raw/`.
2. Open `data_ingestion.py` and edit the `RAW_FILES` dict at the top so the
   keys/filenames match your actual files. The two keys `fund_master` and
   `nav_history` are used later for the AMFI code validation — rename them
   to whichever of your 10 files actually hold that data.
3. Run:
   ```bash
   python data_ingestion.py
   ```
   This prints `.shape`, `.dtypes`, `.head()`, and a basic anomaly check
   (nulls, duplicates, negative numeric values, constant columns) for
   every dataset. It then explores the fund master (unique fund houses /
   categories / sub-categories / risk grades, AMFI code structure) and
   writes `reports/data_quality_summary.txt` validating every fund_master
   code exists in nav_history.

## Steps 4–5 — Live NAV fetch

```bash
python live_nav_fetch.py
```

This hits `https://api.mfapi.in/mf/{scheme_code}` for:

| Scheme | Code |
|---|---|
| HDFC Top 100 Direct | 125497 |
| SBI Bluechip | 119551 |
| ICICI Bluechip | 120503 |
| Nippon Large Cap | 118632 |
| Axis Bluechip | 119092 |
| Kotak Bluechip | 120841 |

Each scheme's full NAV history is saved to
`data/raw/nav_{code}_{name}.csv` with columns `date, nav` plus the
scheme's meta fields (fund house, category, etc.) attached to every row.

> mfapi.in is a free, unauthenticated, community-run API — no key needed,
> but it can rate-limit or time out under heavy use. The script sleeps
> briefly between calls and will report per-scheme failures without
> stopping the whole run.

## Git / GitHub

Run these from the project root (needs your own GitHub account + a
network connection, since this can't be done from a sandbox):

```bash
git init
git add .
git commit -m "Day 1: Data ingestion complete"

# create an empty repo on GitHub first (via github.com or `gh repo create`), then:
git branch -M main
git remote add origin https://github.com/<your-username>/mf-analytics.git
git push -u origin main
```

If you'd rather version the fetched NAV CSVs too (not just code), remove
the `data/raw/*.csv` line from `.gitignore` before committing.

## Deliverables checklist
- [x] `data_ingestion.py`
- [x] `live_nav_fetch.py`
- [x] `requirements.txt`
- [ ] GitHub repo with "Day 1: Data ingestion complete" commit — push from
      your machine using the commands above

