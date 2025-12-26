# Data Workflow Pipeline
A modular data processing pipeline designed to load raw data, perform quality checks, transform datasets, and generate visual insights. Built as part of the **AI Professionals Bootcamp**.

## Project Overview
This pipeline follows a sequential ETL (Extract, Transform, Load) process:
1. **Load:** Converts raw CSV files to efficient Parquet format.
2. **Clean:** Handles missing values, text normalization, and deduplication.
3. **Transform:** Builds an analytics-ready table by joining datasets and handling outliers.
4. **Analyze:** Exploratory Data Analysis (EDA) and Bootstrap uncertainty quantification.

## Project Structure
```text
Pipeline/
├── data/               # Raw and processed datasets
├── notebooks/          # EDA notebooks (eda.ipynb)
├── scripts/            # Pipeline execution scripts (Day 1-3)
├── src/data_workflow/  # Core library modules
│   ├── config.py       # Path management
│   ├── io.py           # Data I/O helpers
│   ├── quality.py      # Quality & Fail-fast checks
│   ├── transformers.py # Cleaning & logic
│   ├── joins.py        # Safe join utilities
│   ├── viz.py          # Plotly visualization helpers
│   └── utils.py        # Statistical utilities
└── reports/            # Generated figures and audit reports
```

## Requirements
* **Python 3.13**
* **Virtual Environment (venv)**
* **Dependencies:** pandas, pyarrow, plotly, kaleido, numpy.

## Clone and Install
1. **Clone the repository:**
   ```bash
   git clone https://github.com/NAlfassal/Pipeline.git 
   cd Pipeline
   ```

2. **Setup Virtual Environment:**

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   pip install .
   ```

   **Linux / macOS:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install .
   ```

   *Note for `uv` users: You can simply run `uv sync` to set up the environment.*

##  How to Run
Run the pipeline scripts in order to process the data:

```powershell
python scripts/run_day1_load.py
python scripts/run_day2_clean.py
python scripts/run_day3_build_analytics.py
```

### Exploratory Data Analysis
To view charts and reports, open the notebook:
```bash
# Install jupyter if not present
pip install jupyter
# Run the notebook
jupyter notebook notebooks/eda.ipynb
```

## Key Features
* **Modular Code:** Separation of concerns between I/O, quality checks, and transformations.
* **Fail-Fast Checks:** Validates column existence, uniqueness, and value ranges early in the process.
* **Safe Joins:** Validates cardinality (many-to-one) to prevent data duplication.
* **Automated Viz:** Includes helpers to generate and export publication-ready Plotly charts.
* **Statistical Rigor:** Includes a Bootstrap function to compute confidence intervals for group comparisons.
