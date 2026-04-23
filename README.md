
# Intrusion Detection System using Machine Learning and Explainable AI

This project implements an AI-based Intrusion Detection System using the NSL-KDD dataset.

Features:
- Data preprocessing and encoding
- SMOTE class imbalance handling
- XGBoost intrusion detection model
- Explainable AI using SHAP
- Web dashboard using Streamlit

Run Instructions:

1. Install dependencies
pip install -r requirements.txt

2. Train the model
python src/train_model.py

3. Run the web dashboard
streamlit run app/app.py
