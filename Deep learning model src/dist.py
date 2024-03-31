import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import time

# Define a function to create a simple neural network model
def create_model(input_shape):
    model = Sequential([
        Dense(64, activation='relu', input_shape=input_shape),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    return model

# Load preprocessed datasets
X_train = np.loadtxt('X_train_preprocessed.csv', delimiter=',', skiprows=1)
X_val = np.loadtxt('X_val_preprocessed.csv', delimiter=',', skiprows=1)
X_test = np.loadtxt('X_test_preprocessed.csv', delimiter=',', skiprows=1)
y_train = np.loadtxt('y_train_preprocessed.csv', delimiter=',', skiprows=1)
y_val = np.loadtxt('y_val_preprocessed.csv', delimiter=',', skiprows=1)
y_test = np.loadtxt('y_test_preprocessed.csv', delimiter=',', skiprows=1)

# Split the data into clients (simulating federated learning)
num_clients = 10
client_data_size = len(X_train) // num_clients

# Train a separate model for each client
client_models = []
for i in range(num_clients):
    client_X_train = X_train[i * client_data_size : (i + 1) * client_data_size]
    client_y_train = y_train[i * client_data_size : (i + 1) * client_data_size]

    # Create a model for the client
    model = create_model(input_shape=(X_train.shape[1],))
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Train the model on the client's data
    start_time = time.time()
    history = model.fit(client_X_train, client_y_train, epochs=10, batch_size=64, validation_data=(X_val, y_val))
    end_time = time.time()
    training_time = end_time - start_time
    print(f"Client {i+1} training time: {training_time} seconds")

    # Evaluate the model on the client's test data
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f'Client {i+1} Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')

    # Save the trained model
    client_models.append(model)

# Federated averaging (simple averaging of model weights)
avg_model_weights = np.mean([model.get_weights() for model in client_models], axis=0)

# Create a global model with the averaged weights
global_model = create_model(input_shape=(X_train.shape[1],))
global_model.set_weights(avg_model_weights)

# Evaluate the global model on the test data
test_loss, test_accuracy = global_model.evaluate(X_test, y_test)
print(f'Global Model Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
