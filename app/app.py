import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import time
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cyber IDS Pro", layout="wide")

# ---------------- CYBER STYLE ----------------
st.markdown("""
<style>
body {background-color: #0e1117; color: #e6edf3;}
h1, h2, h3 {color: #58a6ff;}
.block-container {padding-top: 1rem;}
.alert {color:red; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN SYSTEM ----------------
USERNAME = "admin"
PASSWORD = "admin123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Secure Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == USERNAME and pwd == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

    st.stop()

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Upload & Predict",
    "Live Monitoring",
    "System Info"
])

st.sidebar.success("🟢 System Active")

# ---------------- TITLE ----------------
st.title("🛡️ AI Cybersecurity IDS Pro")
st.caption("Real-Time Intrusion Detection & Monitoring System")

# ---------------- SOUND FUNCTION ----------------
def play_alert():
    st.audio("https://www.soundjay.com/buttons/sounds/beep-07.mp3")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "txt"])

if uploaded_file:

    column_names = [
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
    'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty'
    ]

    data = pd.read_csv(uploaded_file, names=column_names)

    st.subheader("📊 Data Preview")
    st.dataframe(data.head())

    # ---------------- CLEAN ----------------
    data = data.drop(["label", "difficulty"], axis=1)
    data = data.dropna()

    # ---------------- ENCODE ----------------
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()

    for col in data.columns:
        if data[col].dtype == "object":
            data[col] = encoder.fit_transform(data[col].astype(str))

    # ---------------- API ----------------
    with st.spinner("Analyzing traffic..."):
        time.sleep(1)

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"data": data.to_dict(orient="records")}
    )

    result = response.json()
    predictions = result["predictions"]

    label_map = {
        0: "DoS",
        1: "Probe",
        2: "R2L",
        3: "U2R",
        4: "Normal"
    }

    predictions_named = [label_map[p] for p in predictions]

    # ---------------- METRICS ----------------
    total = len(predictions_named)
    attacks = sum(1 for p in predictions_named if p != "Normal")
    normal = total - attacks

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Traffic", total)
    col2.metric("Normal", normal)
    col3.metric("Attacks", attacks)

    attack_ratio = attacks / total

    st.subheader("Threat Level")
    st.progress(attack_ratio)

    if attack_ratio > 0.5:
        st.error("🔴 HIGH THREAT")
        play_alert()
    elif attack_ratio > 0.2:
        st.warning("🟡 MEDIUM THREAT")
    else:
        st.success("🟢 LOW THREAT")

    # ---------------- CHARTS ----------------
    summary = pd.Series(predictions_named).value_counts()

    st.subheader("Attack Distribution")

    # 👇 Create 2 columns (clean layout)
    col1, col2 = st.columns([1, 1])

    # ----------------------
    # BAR CHART (LEFT)
    # ----------------------
    with col1:
        st.markdown("**Bar Chart**")
        st.bar_chart(summary)

    # ----------------------
    # PIE CHART (RIGHT)
    # ----------------------
    with col2:
        st.markdown("**Pie Chart**")

        fig, ax = plt.subplots(figsize=(3, 3))  # 👈 balanced small size

        wedges, _, _ = ax.pie(
            summary,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 8}  # 👈 smaller text
        )

        ax.legend(
            wedges,
            summary.index,
            title="Types",
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=8
        )

        ax.set_ylabel("")

        st.pyplot(fig)

    # ---------------- REAL-TIME SIMULATION ----------------
    st.subheader("📡 Live Traffic Simulation")

    if st.button("Start Simulation"):
        for i in range(10):
            st.write(f"Packet {i} → {predictions_named[i]}")
            time.sleep(0.3)

    # ---------------- ALERT PANEL ----------------
    st.subheader("🚨 Live Alerts")

    for p in predictions_named[:10]:
        if p != "Normal":
            st.error(f"⚠️ Attack: {p}")
        else:
            st.success("✔ Normal")

    # ---------------- DOWNLOAD ----------------
    report = pd.DataFrame({"Prediction": predictions_named})

    st.download_button(
        "Download Report",
        report.to_csv(index=False),
        "IDS_Report.csv"
    )

# ---------------- SYSTEM INFO ----------------
if menu == "System Info":
    st.subheader("System Details")
    st.write("""
    - Model: XGBoost
    - Backend: FastAPI
    - Frontend: Streamlit
    - Dataset: NSL-KDD
    - Features: Real-time monitoring, Explainable AI
    """)