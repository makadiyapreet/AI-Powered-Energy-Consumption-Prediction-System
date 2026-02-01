# ⚡ Project Execution Guide

Follow these steps in order to set up, train, and run the Enterprise Energy Prediction System.

---

## 1. Environment Setup

First, create a virtual environment to keep your project clean.

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

> **Note:** If on Mac, also run `brew install libomp` for XGBoost support.

---

## 2. Initialize System *(Important)*

You must run these scripts **once** before starting the app to create the dataset and the AI model.

**Step A — Generate Synthetic Data**
Creates the `energy_dataset.csv` file.
```bash
python generate_data.py
```

**Step B — Train the AI Model**
Reads the data, trains the XGBoost/RandomForest model, and saves `energy_model.pkl`.
```bash
python train_model.py
```

---

## 3. Run the Application

You need **two separate terminals** open to run the full system.

**Terminal 1 — Start the Backend API**
This runs the FastAPI server that handles predictions.
```bash
uvicorn main:app --reload
```
Wait until you see:
> `Uvicorn running on http://127.0.0.1:8000`

**Terminal 2 — Start the Dashboard**
This launches the visual interface in your browser.
```bash
streamlit run dashboard.py
```
Your browser should automatically open `http://localhost:8501`