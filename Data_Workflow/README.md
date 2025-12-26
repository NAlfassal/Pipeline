Project description:
- Data Workflow: a small project for building a simple data processing pipeline — load raw data, clean and transform it, build analytics tables, and produce reports/figures.

Requirements:
- Python 3.13 
- A virtual environment (venv) 

Clone and install:
1. Clone the repository:

git clone https://github.com/NAlfassal/Pipeline.git
cd Pipeline
2. Create and activate a virtual environment, then install dependencies (reads `pyproject.toml`):

Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate

Linux / macOS:
python -m venv .venv
source .venv/bin/activate
python -m pip install .

Features:
- Load raw CSV/parquet from `data/raw` and write processed outputs to `data/processed`.
- Cleaning and transformation utilities in `src/data_workflow/transformers.py`.
- Data quality checks in `src/data_workflow/quality.py`.
- IO helpers in `src/data_workflow/io.py` (read/write parquet, csv).
- Visualization helpers and example notebook in `src/data_workflow/viz.py` and `notebooks/eda.ipynb`.
overview:
- Scripts for sequential runs are in `scripts/`.
- Reusable library code is in `src/data_workflow/` with modules for IO, transforms, quality checks, and visualization.

How to run:
- Run the pipeline scripts in order:

powershell:
python scripts/run_day1_load.py
python scripts/run_day2_clean.py
python scripts/run_day3_build_analytics.py

- Open the exploratory notebook (install Jupyter if needed):
python -m pip install jupyter

Notes for `uv` users:
you can directly write : uv sync 
to create venv with the dependencies .