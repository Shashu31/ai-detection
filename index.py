# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Sample Data - Medication types, Dosages, Side Effects, and Safety status
data = {
    'Medication_Type': ['Painkiller', 'Painkiller', 'Antibiotic', 'Antibiotic', 'Painkiller', 'Opioid'],
    'Dosage_mg': [500, 400, 250, 150, 200, 10],
    'Side_Effect': ['Dizziness', 'Headache', 'Nausea', 'Rash', 'Drowsiness', 'Constipation'],
    'Safe': [1, 1, 0, 0, 1, 0]  # 1 = Safe, 0 = Potential issue
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert categorical columns to numerical values
df['Medication_Type'] = df['Medication_Type'].map({'Painkiller': 0, 'Antibiotic': 1, 'Opioid': 2})
df['Side_Effect'] = df['Side_Effect'].map({'Dizziness': 0, 'Headache': 1, 'Nausea': 2, 'Rash': 3, 'Drowsiness': 4, 'Constipation': 5})

# Features and target
X = df[['Medication_Type', 'Dosage_mg', 'Side_Effect']]  # Features
y = df['Safe']  # Target (1 = safe, 0 = potential issue)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Example of a new prescription for checking
new_prescription = pd.DataFrame({
    'Medication_Type': [0],  # Painkiller
    'Dosage_mg': [400],  # Dosage in mg
    'Side_Effect': [1]  # Headache
})

# Predict if the new prescription is safe (1 = safe, 0 = potential issue)
prediction = clf.predict(new_prescription)
print(f"Is the prescription safe? {'Yes' if prediction[0] == 1 else 'No'}")
