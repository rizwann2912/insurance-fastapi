# 🛡️ Insurance Premium Category Prediction API

A FastAPI + Streamlit-based machine learning project to predict a customer's **insurance premium category** (Low, Medium, High) based on various factors such as age, income, BMI, occupation, etc.

---

## 🚀 Features

- 📦 Trained ML model (pickle-based)
- 🔮 Predict insurance premium category
- 📊 Displays class probabilities and confidence score
- 🔗 REST API (FastAPI) + UI (Streamlit)
- 🐳 Dockerized deployment

---
<details> <summary><strong>Click to Expand Markdown</strong></summary>
## 📁 Project Structure

insurance-fastapi/
├── app.py # FastAPI backend
├── frontend.py # Streamlit frontend
├── requirements.txt
├── Dockerfile
├── README.md

├── model/
│ └── predict.py # Model prediction logic

├── config/
│ └── city_tier.py # City tier configuration

├── schema/
│ ├── prediction_response.py
│ └── user_input.py

---
</details>
## 🐳 Run using Docker

You can run the FastAPI backend using Docker in just 2 steps:

### 1️⃣ Pull the image from Docker Hub
```bash
docker pull rizwan2912/insurance-premium-api
```

### 2️⃣ Run the container
```bash
docker run -d -p 8000:8000 rizwan2912/insurance-premium-api
```

✅ The FastAPI server will now be running at:
http://localhost:8000

---

## 🧪 API Usage

- **Endpoint:** `/predict` (POST)
- **URL:** http://localhost:8000/predict
- **Method:** POST
- **Request body:**

```json
{
  "bmi": 22.5,
  "age_group": "30-40",
  "lifestyle_risk": "moderate",
  "city_tier": "tier_1",
  "income_lpa": 12.0,
  "occupation": "private_job"
}
```

- **Response:**

```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.48,
    "class_probabilities": {
      "Low": 0.46,
      "Medium": 0.48,
      "High": 0.06
    }
  }
}
```

---

## 🌐 Run Frontend (Streamlit)

Make sure the FastAPI backend is running first. Then in another terminal:

```bash
streamlit run frontend.py
```

Visit the app at:
👉 http://localhost:8501

You'll see a simple UI to enter customer data and view predictions.

---

## 🔧 Dev Setup (Optional - Without Docker)

If you want to run the project manually:

1. **Create a virtual environment**
    ```bash
    python -m venv venv
    # On Unix/Mac
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Start FastAPI server**
    ```bash
    uvicorn app:app --reload
    ```
4. **Launch frontend**
    ```bash
    streamlit run frontend.py
    ```

---

## 📦 Requirements

- Python 3.8+
- Docker (optional)
- Streamlit
- FastAPI
- Scikit-learn
- Pandas
