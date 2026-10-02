# Customer Churn Analysis using AI & Data Science
# Run: python customer_churn_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# STEP 1: Load dataset
df = pd.read_csv("customer_churn.csv")
print("\nSTEP 1 - DATASET")
print(df.head())

# STEP 2: Basic information
print("\nSTEP 2 - DATA INFORMATION")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# STEP 3: Simple statistics
print("\nSTEP 3 - STATISTICS")
print(df.describe())

# STEP 4: Churn distribution
print("\nSTEP 4 - CHURN COUNT")
print(df["Churn"].value_counts())

plt.figure(figsize=(6,4))
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("01_churn_distribution.png")
plt.show()

# STEP 5: Churn by contract
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
print("\nSTEP 5 - CHURN BY CONTRACT")
print(contract_churn)

contract_churn.plot(kind="bar", figsize=(7,4))
plt.title("Churn by Contract Type")
plt.xlabel("Contract")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig("02_churn_by_contract.png")
plt.show()

# STEP 6: Average charges by churn
print("\nSTEP 6 - AVERAGE MONTHLY CHARGES")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# STEP 7: Encode categorical columns
encoded = df.copy()
encoders = {}

for col in ["Gender", "Contract", "InternetService", "PaymentMethod", "Churn"]:
    le = LabelEncoder()
    encoded[col] = le.fit_transform(encoded[col])
    encoders[col] = le

# Customer_ID is an identifier, so it is not used as a prediction feature
X = encoded.drop(columns=["Customer_ID", "Churn"])
y = encoded["Churn"]

# STEP 8: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# STEP 9: Train AI/ML model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_train, y_train)

# STEP 10: Prediction
y_pred = model.predict(X_test)

print("\nSTEP 10 - MODEL RESULT")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# STEP 11: Feature importance
importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nSTEP 11 - FEATURE IMPORTANCE")
print(importance)

importance.sort_values().plot(kind="barh", figsize=(8,5))
plt.title("Feature Importance - Random Forest")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig("03_feature_importance.png")
plt.show()

# STEP 12: Predict a new customer
new_customer = pd.DataFrame([{
    "Age": 26,
    "Gender": "Female",
    "Tenure": 4,
    "MonthlyCharges": 949,
    "TotalCharges": 3796,
    "Contract": "Monthly",
    "InternetService": "Fiber",
    "PaymentMethod": "Credit Card",
    "SupportCalls": 6,
    "SatisfactionScore": 1
}])

for col in ["Gender", "Contract", "InternetService", "PaymentMethod"]:
    # Use the training encoder. Unknown categories need handling in a real production system.
    new_customer[col] = encoders[col].transform(new_customer[col])

prediction = model.predict(new_customer)[0]
probability = model.predict_proba(new_customer)[0][1]

churn_label = encoders["Churn"].inverse_transform([prediction])[0]

print("\nSTEP 12 - NEW CUSTOMER PREDICTION")
print("Predicted Churn:", churn_label)
print("Churn Risk:", round(probability * 100, 2), "%")

# STEP 13: Simple AI-based retention recommendation
if churn_label == "Yes":
    print("Recommendation: Contact the customer, investigate support issues, and offer a suitable retention plan.")
else:
    print("Recommendation: Continue normal engagement and monitor customer satisfaction.")

print("\nPROJECT COMPLETED")
