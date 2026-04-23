from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "xgb_model.pkl")

model = joblib.load(model_path)

# ✅ Expected columns (VERY IMPORTANT)
expected_columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds','is_host_login',
'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate'
]

class InputData(BaseModel):
    data: List[dict]

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def predict(input_data: InputData):
    try:
        df = pd.DataFrame(input_data.data)

        # ✅ Ensure correct column order
        df = df[expected_columns]

        # ✅ Encode categorical
        encoder = LabelEncoder()
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = encoder.fit_transform(df[col])

        predictions = model.predict(df)

        return {"predictions": predictions.tolist()}

    except Exception as e:
        return {"error": str(e)}