import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import time

# Load the cleaned dataset
df = pd.read_csv('cicddos2019_dataset_clean.csv')

# Preprocessing
# 1. Handling Missing Values (if any)
df.dropna(inplace=True)

encoder_protocol = LabelEncoder()
df['Protocol'] = encoder_protocol.fit_transform(df['Protocol'])

encoder_label = LabelEncoder()
df['Label'] = encoder_label.fit_transform(df['Label'])

# Update the 'Class' column values
df['Class'] = df['Class'].map({'Attack': 1, 'Benign': 0})


scaler = MinMaxScaler()
numerical_columns = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Fwd Packets Length Total',
                     'Bwd Packets Length Total', 'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Fwd Packet Length Mean',
                     'Fwd Packet Length Std', 'Bwd Packet Length Max', 'Bwd Packet Length Min', 'Bwd Packet Length Mean',
                     'Bwd Packet Length Std', 'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean', 'Flow IAT Std',
                     'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max',
                     'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min',
                     'Fwd Packets/s', 'Bwd Packets/s', 'Packet Length Min', 'Packet Length Max', 'Packet Length Mean',
                     'Packet Length Std', 'Packet Length Variance', 'Avg Packet Size', 'Avg Fwd Segment Size',
                     'Avg Bwd Segment Size', 'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate',
                     'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate', 'Subflow Fwd Packets',
                     'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes', 'Init Fwd Win Bytes',
                     'Init Bwd Win Bytes', 'Fwd Act Data Packets', 'Fwd Seg Size Min', 'Active Mean', 'Active Std',
                     'Active Max', 'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min']
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Remove non-numeric columns
df = df.select_dtypes(include=['float64', 'int64'])

# Print the first 5 rows of the dataframe
print(df.head())


# Splitting the dataset into features (X) and target (y)
X = df.drop(columns=['Class'])  # Features
y = df['Class']  # Target variable

# Splitting the dataset into training (70%), testing (15%), and validation (15%) sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Printing the shapes of the resulting datasets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)
print("Validation set shape:", X_val.shape, y_val.shape)

start_time = time.time()

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=64)

# Calculate the time taken for training
training_time = time.time() - start_time
print("Training time:", training_time, "seconds")

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test loss:", test_loss)
print("Test accuracy:", test_accuracy)

model.save('ddos.keras')