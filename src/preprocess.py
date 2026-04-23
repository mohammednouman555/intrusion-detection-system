import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Drop unnecessary columns
    if "label" in df.columns:
        df = df.drop("label", axis=1)
    if "difficulty" in df.columns:
        df = df.drop("difficulty", axis=1)

    # Encode categorical
    encoder = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = encoder.fit_transform(df[col])

    return df