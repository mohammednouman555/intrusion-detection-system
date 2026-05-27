import pandas as pd
import os
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from imblearn.over_sampling import SMOTE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "KDDTrain+.txt")

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

data = pd.read_csv(data_path, names=column_names)

# ---------------- ATTACK MAPPING ----------------
attack_mapping = {
'normal':'normal',
'neptune':'DoS','smurf':'DoS','back':'DoS','teardrop':'DoS','pod':'DoS','land':'DoS',
'satan':'Probe','ipsweep':'Probe','portsweep':'Probe','nmap':'Probe',
'guess_passwd':'R2L','ftp_write':'R2L','imap':'R2L','phf':'R2L',
'multihop':'R2L','warezclient':'R2L','warezmaster':'R2L','spy':'R2L',
'buffer_overflow':'U2R','rootkit':'U2R','perl':'U2R','loadmodule':'U2R'
}

data['label'] = data['label'].map(attack_mapping)

# ---------------- FEATURES & LABELS ----------------
X = data.drop(['label', 'difficulty'], axis=1)
y = data['label']

# ---------------- ENCODE FEATURES ----------------
encoder = LabelEncoder()

for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = encoder.fit_transform(X[col])

# ---------------- ENCODE LABELS ----------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# ---------------- SMOTE ----------------
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# ---------------- MODELS ----------------
dt_model = DecisionTreeClassifier(random_state=42)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    eval_metric='mlogloss'
)

# ---------------- TRAIN ----------------
print("Training Decision Tree...")
dt_model.fit(X_resampled, y_resampled)

print("Training Random Forest...")
rf_model.fit(X_resampled, y_resampled)

print("Training XGBoost...")
xgb_model.fit(X_resampled, y_resampled)

# ---------------- ACCURACY ----------------
dt_acc = accuracy_score(y_test, dt_model.predict(X_test))
rf_acc = accuracy_score(y_test, rf_model.predict(X_test))
xgb_acc = accuracy_score(y_test, xgb_model.predict(X_test))

print("\nMODEL ACCURACY COMPARISON")
print("--------------------------------")
print(f"Decision Tree Accuracy : {dt_acc:.4f}")
print(f"Random Forest Accuracy: {rf_acc:.4f}")
print(f"XGBoost Accuracy      : {xgb_acc:.4f}")

# ---------------- SAVE MODELS ----------------
models_dir = os.path.join(BASE_DIR, "models")
os.makedirs(models_dir, exist_ok=True)

joblib.dump(dt_model, os.path.join(models_dir, "decision_tree.pkl"))
joblib.dump(rf_model, os.path.join(models_dir, "random_forest.pkl"))
joblib.dump(xgb_model, os.path.join(models_dir, "xgb_model.pkl"))

print("\nModels saved successfully!")