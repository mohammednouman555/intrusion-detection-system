# 🔐 AI-Driven Intrusion Detection System for Network Security with Explainable Intelligence and Real-Time Analytics

## 📌 Overview

This project is an AI-powered Intrusion Detection System (IDS) designed to monitor and analyze network traffic to detect malicious activities and cyber attacks in real-time.

The system uses Machine Learning algorithms such as:

* Decision Tree
* Random Forest
* XGBoost

to classify network traffic into:

* Normal
* DoS
* Probe
* R2L
* U2R

The project integrates:

* FastAPI backend for prediction
* Streamlit dashboard for visualization
* SMOTE for handling imbalanced datasets
* SHAP for Explainable AI

---

# 🚀 Features

✅ Real-time intrusion detection
✅ Multiple ML model comparison
✅ XGBoost-based high accuracy detection
✅ FastAPI backend integration
✅ Interactive Streamlit dashboard
✅ Attack visualization using charts
✅ Explainable AI using SHAP
✅ User-friendly UI
✅ Threat monitoring and analytics

---

# 🧠 Technologies Used

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* XGBoost
* SMOTE (Imbalanced-learn)

## Backend

* FastAPI
* Uvicorn

## Frontend

* Streamlit

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib

## Explainable AI

* SHAP

## Model Saving

* Joblib

---

# 📂 Project Structure

```text id="mznp7z"
IDS_Project_AI/
│
├── app/
│   └── app.py
│
├── src/
│   ├── api.py
│   └── train_model.py
│
├── data/
│   ├── KDDTrain+.txt
│   └── KDDTest+.csv
│
├── models/
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   └── xgb_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The project uses the **NSL-KDD Dataset**, a benchmark dataset widely used for intrusion detection research.

## Attack Categories

* Normal
* DoS
* Probe
* R2L
* U2R

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash id="ax0lr9"
git clone https://github.com/mohammednouman555/intrusion-detection-system.git
```

```bash id="0t2iwy"
cd intrusion-detection-system
```

---

## 2️⃣ Create Virtual Environment

```bash id="svv3xq"
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash id="5r4jkq"
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash id="k74db5"
pip install -r requirements.txt
```

---

# 🏋️ Train Machine Learning Models

Run:

```bash id="s6e70u"
python src/train_model.py
```

This will:

* Load dataset
* Preprocess data
* Apply SMOTE
* Train multiple ML models
* Compare accuracies
* Save trained models

---

# 📈 Model Accuracy Comparison

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | 99.70%   |
| Random Forest | 99.88%   |
| XGBoost       | 99.90%   |

---

# 🌐 Run FastAPI Backend

```bash id="d0rn5e"
uvicorn src.api:app --reload
```

Backend URL:

```text id="q63upz"
http://127.0.0.1:8000
```

Swagger Documentation:

```text id="ujpmz9"
http://127.0.0.1:8000/docs
```

---

# 🖥️ Run Streamlit Dashboard

```bash id="vow26z"
streamlit run app/app.py
```

Dashboard URL:

```text id="jlwmz"
http://localhost:8501
```

---

# 🔐 Login Credentials

```text id="kxtswt"
Password: admin123
```

---

# 📤 Usage

1. Run FastAPI server
2. Run Streamlit dashboard
3. Login using password
4. Upload `KDDTest+.csv` dataset
5. View:

   * Attack predictions
   * Threat analytics
   * Pie charts
   * Bar charts
   * Accuracy comparison
   * SHAP explanations

---

# 🔁 System Workflow

```text id="v7wt9j"
Dataset
→ Data Preprocessing
→ SMOTE Balancing
→ ML Model Training
→ Accuracy Comparison
→ FastAPI Backend
→ Streamlit Dashboard
→ Prediction & Visualization
```

---

# 🧠 Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) is used to explain model predictions and identify which features contribute most to attack detection.

Benefits:

* Transparency
* Better understanding of predictions
* Improved trust in AI decisions

---

# 📊 Dashboard Features

✅ File Upload System
✅ Attack Detection
✅ Bar Charts
✅ Pie Charts
✅ Accuracy Comparison Graph
✅ Threat Monitoring
✅ Real-time Prediction

---

# 🏆 Project Highlights

* AI-powered cybersecurity solution
* Real-time intrusion monitoring
* High detection accuracy
* Multiple ML algorithm comparison
* Explainable AI integration
* Professional dashboard interface

---

# 🔮 Future Enhancements

* Real-time packet sniffing
* Deep learning integration
* Cloud deployment
* SIEM integration
* Automated threat response
* Live network traffic analysis

---

# 👨‍💻 Authors

* Mohammed Nouman
* Mohammed Mudassir
* Uzair Ali Hashmi

Department of Computer Science Engineering
Deccan College of Engineering and Technology

---

# 📜 License

This project is developed for academic and educational purposes.

---

# ⭐ Conclusion

This project demonstrates how Artificial Intelligence and Machine Learning can be effectively integrated with cybersecurity systems to build a powerful, intelligent, and real-time intrusion detection solution with high accuracy and explainability.
