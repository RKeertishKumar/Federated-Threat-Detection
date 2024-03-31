import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import time

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Load preprocessed datasets using Pandas with specified dtype as object and error handling
X_train = pd.read_csv('X_train_preprocessed.csv', dtype=object, error_bad_lines=False).values[:, :79]
X_val = pd.read_csv('X_val_preprocessed.csv', dtype=object, error_bad_lines=False).values[:, :79]
X_test = pd.read_csv('X_test_preprocessed.csv', dtype=object, error_bad_lines=False).values[:, :79]
y_train = pd.read_csv('y_train_preprocessed.csv').values
y_val = pd.read_csv('y_val_preprocessed.csv').values
y_test = pd.read_csv('y_test_preprocessed.csv').values

# Convert data to TensorFlow tensors
X_train_tf = tf.convert_to_tensor(X_train, dtype=tf.float32)
X_val_tf = tf.convert_to_tensor(X_val, dtype=tf.float32)
X_test_tf = tf.convert_to_tensor(X_test, dtype=tf.float32)
y_train_tf = tf.convert_to_tensor(y_train, dtype=tf.float32)
y_val_tf = tf.convert_to_tensor(y_val, dtype=tf.float32)
y_test_tf = tf.convert_to_tensor(y_test, dtype=tf.float32)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
start_time = time.time()
history = model.fit(X_train_tf, y_train_tf, epochs=10, batch_size=64, validation_data=(X_val_tf, y_val_tf))
end_time = time.time()
training_time = end_time - start_time
print(f"Training time: {training_time} seconds")

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(X_test_tf, y_test_tf)
print(f'Test Loss: {test_loss}, Test Accuracy: {test_accuracy}')
