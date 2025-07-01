from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model.predict import load_model,predict_output
import pandas as pd

from schema.user_input import Customer
from schema.prediction_response import PredictionResponse

app = FastAPI()

model = load_model('model/model.pkl')

@app.get('/')
def home():
    return {"message":"Insurance Prediction"}

@app.get('/health')
def health_check():
    return {
        "status":"ok"
    }
@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: Customer):
    input_df = pd.DataFrame([{
        "bmi":data.bmi,
        "age_group" : data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    try:
        prediction = predict_output(input_df)

        return JSONResponse(status_code=200, content={'Result':prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))