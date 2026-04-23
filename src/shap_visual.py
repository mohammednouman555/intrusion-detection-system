import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("../models/xgb_model.pkl")

# Load dataset
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

data = pd.read_csv("../data/KDDTest+.csv", names=column_names, low_memory=False)

# Drop unwanted columns
data = data.drop(["label", "difficulty"], axis=1)

# Encode categorical data
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

for col in data.columns:
    data[col] = data[col].astype(str)
    data[col] = encoder.fit_transform(data[col])

# Take sample
X_sample = data[:100]

# SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_sample)

# Plot
shap.summary_plot(shap_values, X_sample)

plt.show()