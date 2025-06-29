from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")

app = FastAPI()

class RevenueInput(BaseModel):
    date: str
    product_category: str
    region: str
    agent_id: str
    marketing_spend: float
    lead_count: int

@app.post("/predict")
def predict(data: RevenueInput):
    try:
        date = pd.to_datetime(data.date)
        
        row = {
            'day': date.day,
            'month': date.month,
            'weekday': date.weekday(),
            'marketing_spend': data.marketing_spend,
            'lead_count': data.lead_count,
        }

        for col in model_columns:
            if col.startswith('product_category_'):
                row[col] = 1 if col == f"product_category_{data.product_category}" else 0
            elif col.startswith('region_'):
                row[col] = 1 if col == f"region_{data.region}" else 0
            elif col.startswith('agent_id_'):
                row[col] = 1 if col == f"agent_id_{data.agent_id}" else 0
            elif col not in row:
                row[col] = 0  

        df_input = pd.DataFrame([row])
        df_input = df_input[model_columns] 

        prediction = model.predict(df_input)[0]

        return {"forecasted_revenue": round(prediction, 2)}
    
    except Exception as e:
        return {"error": str(e)}
