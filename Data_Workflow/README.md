# مشروع Data Workflow

وصف المشروع:
- هذا مشروع بسيط لأنشاء سير عمل معالجة بيانات: تحميل البيانات، تنظيفها، بناء جداول تحليليّة، وإنتاج تقارير ومرئيات.
- يتضمّن ملفات سكربتات للتشغيل المتسلسل في المجلد `scripts/`، ومكتبة داخل `src/data_workflow` مع وظائف للقراءة، التحويل، والجودة، ومرئيات.

المتطلبات:
- Python 3.13 أو أحدث
- بيئة افتراضية (venv) موصى بها

طريقة تنزيل المشروع من GitHub:
1. انسخ المستودع محلياً:

```bash
git clone https://github.com/<your-username>/data-workflow.git
cd data-workflow
```

2. إنشئ وفعّل بيئة افتراضية ثم ثبّت التبعيات:

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
python -m pip install .
```

Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
```

ملاحظة: التثبيت بـ `python -m pip install .` يقرأ `pyproject.toml` ويثبت التبعيات المحدّدة. إذا تفضّل ملف `requirements.txt`، يمكن إنشاؤه يدويًا أو استخدام أداة لإصداره.

ميزات المشروع (Features):
- تحميل بيانات من `data/raw` وتجهيزها في `data/processed`.
- أنابيب تنظيف وتحويل ضمن `src/data_workflow/transformers.py`.
- فحص جودة البيانات في `src/data_workflow/quality.py`.
- وظائف إدخال/إخراج في `src/data_workflow/io.py` (قراءة/كتابة parquet، csv).
- مرئيات جاهزة في `src/data_workflow/viz.py` ونوتبوك استكشافي في `notebooks/eda.ipynb`.

كيفية التشغيل (Run):
- لتشغيل سكربتات التحضير والتدفقات اليومية:

```powershell
python scripts/run_day1_load.py
python scripts/run_day2_clean.py
python scripts/run_day3_build_analytics.py
```

- لتشغيل الـ notebook استكشافي (بعد تثبيت Jupyter):

```bash
python -m pip install jupyter
jupyter notebook notebooks/eda.ipynb
```

- لتشغيل اختبار سريع لملف `main.py` إن وُجد:

```bash
python main.py
```

اقتراحات إضافية:
- احتفظ بنسخة من البيانات الحسّاسة خارج المستودع (مثلاً في `data/external`).
- إذا أردت نشر الحزمة استخدم `pip install .` أو أدوات مثل `poetry`/`flit` حسب سير العمل.

إذا تحب، أعد صياغة README بالإنجليزية أو أضيف مثال تشغيل مفصّل لكل سكربت.

---

# English README

Project description:
- Data Workflow: a small project for building a simple data processing pipeline — load raw data, clean and transform it, build analytics tables, and produce reports/figures.

Quick overview:
- Scripts for sequential runs are in `scripts/`.
- Reusable library code is in `src/data_workflow/` with modules for IO, transforms, quality checks, and visualization.

Requirements:
- Python 3.13 or newer
- A virtual environment (venv) is recommended

Clone and install:
1. Clone the repository:

```bash
git clone https://github.com/<your-username>/data-workflow.git
cd data-workflow
```

2. Create and activate a virtual environment, then install dependencies (reads `pyproject.toml`):

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
python -m pip install .
```

Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
```

Features:
- Load raw CSV/parquet from `data/raw` and write processed outputs to `data/processed`.
- Cleaning and transformation utilities in `src/data_workflow/transformers.py`.
- Data quality checks in `src/data_workflow/quality.py`.
- IO helpers in `src/data_workflow/io.py` (read/write parquet, csv).
- Visualization helpers and example notebook in `src/data_workflow/viz.py` and `notebooks/eda.ipynb`.

How to run:
- Run the pipeline scripts in order:

```powershell
python scripts/run_day1_load.py
python scripts/run_day2_clean.py
python scripts/run_day3_build_analytics.py
```

- Open the exploratory notebook (install Jupyter if needed):

```bash
python -m pip install jupyter
jupyter notebook notebooks/eda.ipynb
```

- Quick run for `main.py` if present:

```bash
python main.py
```

Notes & recommendations:
- Keep sensitive or large external data out of the repo (use `data/external/`).
- For packaging or deployment use `pip install .` or tools like `poetry`/`flit` if you prefer.

If you want, I can:
- Create a separate `README_en.md` instead of appending here.
- Add detailed examples for each script or CI steps.

Notes for `uv` users:
- If you use `uv` as a shortcut for `uvicorn`, you can run the app server with either `uv` or `uvicorn` depending on your setup.

Examples (replace `main:app` with your module:app if different):

```powershell
# using uv (if installed as a cli alias)
uv main:app --reload --host 0.0.0.0 --port 8000

# or using uvicorn explicitly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Arabic note for `uv`:
- إذا كنت تستخدم أمر `uv` (مُختصر لـ `uvicorn`) لتشغيل تطبيق ويب، فيمكنك تشغيله كما في المثال أعلاه مع استبدال `main:app` بمسار التطبيق لديك.

