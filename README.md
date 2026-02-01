# 🏭 Enterprise Energy Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange?style=flat-square)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-Educational-gray?style=flat-square)

<br/>

> An AI-powered application that forecasts energy consumption for commercial buildings — helping facility managers optimize usage, reduce electricity bills, and plan daily operations using predictive analytics.

</div>

---

## 📌 Table of Contents

- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [How to Run](#-how-to-run)
- [API Reference](#-api-reference)
- [Development Team](#-development-team)
- [License](#-license)

---

## 🌟 Key Features

| Feature | Description |
|---|---|
| **🚀 Precision Predictor** | Real-time prediction of Energy Load (kWh) and Cost (₹/\$) based on adjustable environmental factors. |
| **📅 24-Hour Day Planner** | Generates a full daily schedule graph showing how energy usage fluctuates with temperature and occupancy. |
| **🧠 AI Insights** | Explains *why* the model made a specific prediction (e.g., *"High temperature is contributing 40% to your bill"*). |
| **⚡ High-Performance Backend** | Built on FastAPI for sub-millisecond response times. |
| **📊 Interactive Dashboard** | A clean, professional UI built with Streamlit and Plotly for visual exploration. |

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.9+ |
| **Machine Learning** | XGBoost, Random Forest (Scikit-Learn) |
| **Data Processing** | Pandas, NumPy |
| **Backend API** | FastAPI, Uvicorn |
| **Frontend UI** | Streamlit |
| **Visualization** | Plotly Express / Graph Objects |
| **Model Persistence** | Joblib |

---

## 📂 Project Structure

```
ENERGY-PREDICTION-SYSTEM/
│
├── main.py                 # FastAPI backend — serves prediction endpoints
├── dashboard.py            # Streamlit frontend — interactive dashboard UI
├── train_model.py          # ML model training script (saves energy_model.pkl)
├── generate_data.py        # Synthetic dataset generator (saves energy_dataset.csv)
│
├── energy_dataset.csv      # Generated training dataset
├── energy_model.pkl        # Serialized ML model (created after training)
│
├── requirements.txt        # Python dependency list
└── README.md               # Project documentation (this file)
```

---

## ⚙️ Installation & Setup

### Prerequisites

- **Python 3.9+** installed on your machine
- **pip** package manager

> **Note for macOS users:** XGBoost may require OpenMP. Install it first:
> ```bash
> brew install libomp
> ```

### Step 1 — Clone the Repository

```bash
git clone https://github.com/makadiyapreet/energy-prediction.git
cd energy-prediction
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `fastapi`, `uvicorn`, `streamlit`, `plotly`, `requests`, and `joblib`.

### Step 3 — Generate Data & Train the Model

These two steps build the "brain" of the system. Run them **once** before launching the app.

```bash
# A) Generate the synthetic training dataset
python generate_data.py

# B) Train the ML model and save it
python train_model.py
```

✅ A file named `energy_model.pkl` will appear in your project folder — this confirms the model trained successfully.

---

## 🚀 How to Run

The application has two independent services. Open **two separate terminal windows** and run one command in each.

### Terminal 1 — Start the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

The server will start at:
> 🔗 `http://127.0.0.1:8000`

The `--reload` flag auto-restarts the server on code changes during development.

### Terminal 2 — Start the Frontend (Streamlit)

```bash
streamlit run dashboard.py
```

A browser window will open automatically at:
> 🔗 `http://localhost:8501`

---

## 📡 API Reference

The FastAPI backend exposes the following endpoints (accessible at `http://127.0.0.1:8000`):

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — confirms the API is running |
| `POST` | `/predict` | Accepts environmental parameters and returns predicted energy load (kWh) and cost |
| `GET` | `/predict-day` | Generates a full 24-hour energy consumption forecast |
| `GET` | `/docs` | Auto-generated interactive API documentation (Swagger UI) |

> **Tip:** Open `http://127.0.0.1:8000/docs` in your browser to explore and test all endpoints interactively.

---

## 👥 Development Team

This project was developed by a team of 7 members as a Final Year Project.

| Role | Name | Roll No. |
|---|---|---|
| 🏆 Team Lead | Preet Makadiya | 23BCP414 |
| 💻 Developer | Himadri Patel | 23BCP359 |
| 💻 Developer | Om Kathiriya | 23BCP417 |
| 💻 Developer | Yana Vaghani | 23BCP411 |
| 💻 Developer | Vansh Paun | 23BCP413 |
| 💻 Developer | Rahul Pal | 23BCP379 |
| 💻 Developer | Yash Agarawal | 23BCP351 |

---

## 📜 License

This project was created for **educational purposes** as a Third Year Project (TYP) submission. It is not intended for commercial use.

---

*Built with ❤️ by the Enterprise Energy Prediction System team.*
