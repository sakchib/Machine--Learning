# pip install pillow numpy matplotlib
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Path to your images (adjust to your folder path)
image_dir = r'C:\Users\ACER\Desktop\Linear ALgebra\Chapter 3\img' # Change this path to where your images are stored
image_size = (28, 28)  # MNIST image size (28x28)

# Prepare empty lists to hold images and labels
images = []
labels = []

# Loop through the images (assuming names are '1.jpg', '2.jpg', etc.)
for i in range(1, 6):  # For images 1.jpg to 5.jpg
    filename = f"{i}.jpg"  # Image file name
    img_path = os.path.join(image_dir, filename)
    
    # Load the image
    img = Image.open(img_path).convert('L')  # Convert to grayscale
    img = img.resize(image_size)  # Resize to 28x28
    
    # Convert image to numpy array and normalize (values between 0 and 1)
    img_array = np.array(img) / 255.0
    
    # Append the image data to the images list
    images.append(img_array)
    
    # Append the label (digit) to the labels list
    labels.append(i)  # Label is the digit itself (1 for '1.jpg', etc.)

# Convert images and labels to numpy arrays
images = np.array(images)  # Shape: (5, 28, 28)
labels = np.array(labels)  # Shape: (5,)

# Save the images and labels as .npy files (optional, for later use)
np.save('handwritten_images.npy', images)
np.save('handwritten_labels.npy', labels)

# Plotting the images
fig, axes = plt.subplots(1, 5, figsize=(15, 5))  # 1 row, 5 columns for 5 images
for i, ax in enumerate(axes):
    ax.imshow(images[i], cmap='gray')  # Show image in grayscale
    ax.set_title(f"Label: {labels[i]}")  # Set label as title
    ax.axis('off')  # Hide axes

plt.tight_layout()
plt.show()

# Print shape to verify
print(f"Images shape: {images.shape}")
print(f"Labels shape: {labels.shape}")
