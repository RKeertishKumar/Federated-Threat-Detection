import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load preprocessed datasets
X_train = np.loadtxt('X_train_preprocessed.csv', delimiter=',', skiprows=1)
X_val = np.loadtxt('X_val_preprocessed.csv', delimiter=',', skiprows=1)
X_test = np.loadtxt('X_test_preprocessed.csv', delimiter=',', skiprows=1)
y_train = np.loadtxt('y_train_preprocessed.csv', delimiter=',', skiprows=1)
y_val = np.loadtxt('y_val_preprocessed.csv', delimiter=',', skiprows=1)
y_test = np.loadtxt('y_test_preprocessed.csv', delimiter=',', skiprows=1)

# Define the Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()
training_time = end_time - start_time
print(f"Training time: {training_time} seconds")

# Evaluate the model on validation data
val_preds = model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_preds)
print(f'Validation Accuracy: {val_accuracy}')

# Evaluate the model on test data
test_preds = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_preds)
print(f'Test Accuracy: {test_accuracy}')
