import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import time
from concurrent.futures import ThreadPoolExecutor

# Function to split data into multiple clients
def split_data(X, y, num_clients):
    num_samples = X.shape[0]
    samples_per_client = num_samples // num_clients
    X_clients = []
    y_clients = []
    for i in range(num_clients):
        start_idx = i * samples_per_client
        end_idx = start_idx + samples_per_client
        X_clients.append(X[start_idx:end_idx])
        y_clients.append(y[start_idx:end_idx])
    return X_clients, y_clients

# Load preprocessed datasets
X_train = np.loadtxt('X_train_preprocessed.csv', delimiter=',', skiprows=1)
X_val = np.loadtxt('X_val_preprocessed.csv', delimiter=',', skiprows=1)
X_test = np.loadtxt('X_test_preprocessed.csv', delimiter=',', skiprows=1)
y_train = np.loadtxt('y_train_preprocessed.csv', delimiter=',', skiprows=1)
y_val = np.loadtxt('y_val_preprocessed.csv', delimiter=',', skiprows=1)
y_test = np.loadtxt('y_test_preprocessed.csv', delimiter=',', skiprows=1)

# Split data into multiple clients
num_clients = 5
X_train_clients, y_train_clients = split_data(X_train, y_train, num_clients)

# Define the model
global_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the global model
global_model.compile(optimizer=Adam(learning_rate=0.001),
                     loss='binary_crossentropy',
                     metrics=['accuracy'])

# Federated averaging algorithm
def federated_averaging(local_models):
    global_weights = [np.zeros_like(weights) for weights in local_models[0].get_weights()]
    for local_model in local_models:
        local_weights = local_model.get_weights()
        for i, weight in enumerate(local_weights):
            global_weights[i] += weight
    num_models = len(local_models)
    global_weights = [weight / num_models for weight in global_weights]
    global_model.set_weights(global_weights)

# Function to simulate local training on client devices
def simulate_local_training(X_train, y_train):
    local_model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    local_model.compile(optimizer=Adam(learning_rate=0.001),
                        loss='binary_crossentropy',
                        metrics=['accuracy'])
    local_model.fit(X_train, y_train, epochs=10, batch_size=64, verbose=0)
    return local_model

# Simulate federated learning rounds with multithreading
num_rounds = 10
start_time = time.time()  # Start time

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(simulate_local_training, X_train_clients[i], y_train_clients[i]) for i in range(num_clients)]
    local_models = [future.result() for future in futures]

for round in range(1, num_rounds):
    print(f"Round {round + 1}/{num_rounds}")
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(simulate_local_training, X_train_clients[i], y_train_clients[i]) for i in range(num_clients)]
        local_models = [future.result() for future in futures]
    federated_averaging(local_models)

end_time = time.time()  # End time
training_time = end_time - start_time  # Training time
print(f"Training time: {training_time} seconds")

# Evaluate the global model on test data
test_loss, test_accuracy = global_model.evaluate(X_test, y_test)
print(f'Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
