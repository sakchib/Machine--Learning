import tensorflow as tf
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Print dataset details
print(f"Training data shape: {x_train.shape}, Training labels shape: {y_train.shape}")
print(f"Testing data shape: {x_test.shape}, Testing labels shape: {y_test.shape}")

# Visualize some samples from the dataset
def plot_mnist_samples(images, labels, count=10):
    plt.figure(figsize=(10, 1))
    for i in range(count):
        plt.subplot(1, count, i + 1)
        plt.imshow(images[i], cmap="gray")
        plt.axis("off")
        plt.title(str(labels[i]))
    plt.show()

# Display 10 samples from the training set
plot_mnist_samples(x_train, y_train)
