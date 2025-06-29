

## 🚀 Revenue Forecasting + API Deployment

This project presents a complete pipeline to **predict daily revenue** based on marketing and sales features using **machine learning**, and exposes predictions via a **FastAPI-powered REST API**.

---

### 📊 Problem Statement

You are given historical data across:

* 📅 **Date**
* 📦 **Product Category**
* 🌍 **Region**
* 👤 **Agent ID**
* 💰 **Marketing Spend**
* 🎯 **Lead Count**

Your task is to forecast revenue for the next 90 days and deploy the model via an API.

---

## ✅ Project Highlights

* 🔍 **Data Preprocessing:** Cleaned and transformed date features, handled categorical data with one-hot encoding, and removed noise (nulls).
* 🤖 **Model Used:** `RandomForestRegressor` trained on over 500,000 rows for accurate revenue prediction.
* 🧠 **Feature Engineering:** Extracted `day`, `month`, and `weekday` from the date; one-hot encoded all categorical features.
* 🌐 **Deployment:** Created a **FastAPI** server with a `/predict` endpoint accepting JSON and returning forecasted revenue.
* 📦 **Pickled Artifacts:** Trained model (`model.pkl`) and feature schema (`model_columns.pkl`) saved for deployment.

---

## 📁 Files Included

| File                        | Description                                        |
| --------------------------- | -------------------------------------------------- |
| `revenue_forecasting.ipynb` | Complete training + preprocessing notebook         |
| `model.pkl`                 | Trained RandomForest model                         |
| `model_columns.pkl`         | List of feature columns used during model training |
| `api.py`                    | FastAPI script exposing the `/predict` endpoint    |


---

## 🛠️ How to Run Locally

### 1. Install Requirements

```bash
pip install fastapi uvicorn joblib pandas scikit-learn
```

### 2. Run the API Server

```bash
uvicorn api:app --reload
```

### 3. Test on Swagger UI

Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Try the `/predict` endpoint with input, you will see the response.

## 💡 Learnings and Impact

* Understood end-to-end ML lifecycle: data → model → API
* Explored feature engineering & encoding strategies
* Deployed ML model with industry-standard FastAPI

---

## 👨‍💻 Author

**Nikunja Sonawane**
B.Tech AI & DS | VESIT
Passionate about building impactful ML & AI solutions.

---


