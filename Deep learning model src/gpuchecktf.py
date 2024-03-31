import tensorflow as tf

# List all available GPUs
gpus = tf.config.list_physical_devices('GPU')

if gpus:
    print("Available GPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPUs available.")
