import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import time

# Load preprocessed datasets
X_train = np.loadtxt('X_train_preprocessed.csv', delimiter=',', skiprows=1)
X_val = np.loadtxt('X_val_preprocessed.csv', delimiter=',', skiprows=1)
X_test = np.loadtxt('X_test_preprocessed.csv', delimiter=',', skiprows=1)
y_train = np.loadtxt('y_train_preprocessed.csv', delimiter=',', skiprows=1)
y_val = np.loadtxt('y_val_preprocessed.csv', delimiter=',', skiprows=1)
y_test = np.loadtxt('y_test_preprocessed.csv', delimiter=',', skiprows=1)

# Define the Decision Tree classifier
model = DecisionTreeClassifier()

# Train the model
start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()
training_time = end_time - start_time
print(f"Training time: {training_time} seconds")

# Predictions on validation data
val_predictions = model.predict(X_val)

# Calculate accuracy on validation data
val_accuracy = accuracy_score(y_val, val_predictions)
print(f'Validation Accuracy: {val_accuracy}')

# Predictions on test data
test_predictions = model.predict(X_test)

# Calculate accuracy on test data
test_accuracy = accuracy_score(y_test, test_predictions)
print(f'Test Accuracy: {test_accuracy}')
