---

# 🔐 AI-Driven Intrusion Detection System (IDS)

---

## 📌 Overview

This project is an AI-based Intrusion Detection System (IDS) designed to analyze network traffic and detect malicious activities. It leverages machine learning techniques to classify traffic into different categories such as Normal, DoS, Probe, R2L, and U2R attacks.

### The system integrates:

- XGBoost for high-accuracy classification

- SMOTE for handling imbalanced data

-FastAPI for real-time backend predictions

-Streamlit for an interactive dashboard

- SHAP for explainable AI

---

## 🚀 Features

- 📊 Detects multiple types of cyber attacks

- ⚖️ Handles imbalanced datasets using SMOTE

- ⚡ Real-time prediction via FastAPI

- 🖥️ Interactive Streamlit dashboard

- 📈 Visualizations (Bar Chart, Pie Chart)

- 🚨 Threat alert system

- 🧠 Explainable AI using SHAP



---

## 🧠 Technologies Used

- Python

- Pandas, NumPy

- Scikit-learn

- XGBoost

- Imbalanced-learn (SMOTE)

- FastAPI

- Streamlit

- Matplotlib

- SHAP

- Joblib

---

## 📂 Project Structure
```
IDS_Project_AI/
│
├── data/
│   ├── KDDTrain+.txt
│   ├── KDDTest+.txt
│
├── models/
│   └── xgb_model.pkl
│
├── src/
│   ├── train_model.py
│   ├── api.py
│
├── app/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/your-username/IDS_Project_AI.git
cd IDS_Project_AI


---

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


---

3️⃣ Install Dependencies

pip install -r requirements.txt


---

📊 Dataset

This project uses the NSL-KDD dataset for training and testing.

Place files inside data/:

KDDTrain+.txt
KDDTest+.txt


---

### 🏋️ Model Training

Run the training script:

- python src/train_model.py

✔ This will:

- Load dataset

- Preprocess data

- Apply SMOTE

- Train XGBoost model

- Save model to models/xgb_model.pkl


---

### 🌐 Run Backend (FastAPI)

- uvicorn src.api:app --reload

Access API at:

- http://127.0.0.1:8000


---

### 🖥️ Run Frontend (Streamlit)

- streamlit run app/app.py

Open in browser:

- http://localhost:8501


---

### 🔐 Login Credentials

Password: admin123


---

## 📤 Usage

1. Run backend and frontend


2. Login to dashboard


3. Upload dataset (KDDTest+.csv)


4. View:

- Predictions

- Attack distribution

- Alerts

- SHAP explainability



---

## 🔁 System Workflow
```
Dataset → Preprocessing → SMOTE → XGBoost Model
→ FastAPI → Streamlit Dashboard → Predictions → Visualization
```

---

## 📈 Output

- Attack classification (DoS, Probe, R2L, U2R, Normal)

- Graphs (bar & pie charts)

- Threat alerts

- Feature importance (SHAP)


---

## 🏆 Results

- High accuracy achieved

- Improved detection of minority attacks

- Real-time monitoring enabled

- Transparent decision-making using SHAP


---

## 🔮 Future Enhancements

- Real-time packet capture

- Deep learning models

- Cloud deployment

- Integration with SIEM systems

- Automated threat response


---

## 👨‍💻 Author

Mohammed Nouman
Computer Science Engineering


---

## 📜 License

This project is for academic and educational purposes.


---

## ⭐ Final Note

This project demonstrates how AI + Cybersecurity + Explainable AI can be combined to build a powerful and practical intrusion detection system.


---
