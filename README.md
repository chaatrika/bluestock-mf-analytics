# Bluestock MF Analytics

Project repository for internship tasks — building a mutual fund analytics pipeline covering data ingestion, database design, and reporting.

## 📁 Folder Structure

```
bluestock-mf-analytics/
├── data/          # Raw and cleaned data files (CSV, etc.)
│   ├── raw/       # Original, unmodified source data
│   └── cleaned/   # Processed/cleaned data ready for loading
├── notebooks/     # Jupyter notebooks for data exploration, cleaning, and loading
├── sql/           # Database schema and SQL scripts
├── dashboard/     # Dashboard files and visualizations
└── reports/       # Generated reports and analysis summaries
```

## 🗄️ Database

This project uses **SQLite** as the working database, built from the schema defined in `sql/schema.sql`. Key tables include:

| Table | Description |
|---|---|
| `dim_fund` | Fund master data (dimension table) |
| `fact_nav` | Historical NAV (Net Asset Value) records |
| `fact_transactions` | Investor transaction records |

## 🚀 Getting Started

1. Clone the repository.
2. Set up a Python environment with the required packages:
   ```bash
   pip install pandas sqlalchemy
   ```
3. Run the notebooks in `notebooks/` in order to:
   - Create the database schema (`sql/schema.sql`)
   - Load raw data from `data/raw/`
   - Clean and transform data into `data/cleaned/`
   - Load cleaned data into the SQLite database

## 📊 Data Pipeline

```
data/raw/ → cleaning (notebooks) → data/cleaned/ → SQLite DB → dashboard/reports
```

## 📝 Notes

- Schema changes should be made in `sql/schema.sql` and use `CREATE TABLE IF NOT EXISTS` to keep re-runs safe.
- Update this README as the project structure evolves.

## 👤 Author

Internship project — Bluestock MF Analytics
