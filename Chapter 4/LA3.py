# Tensors are generalizations of vectors and matrices to higher dimensions.
# A scalar is a 0-dimensional tensor, a vector is 1-dimensional, and a matrix is 2-dimensional.
# Tensors are widely used in machine learning frameworks like TensorFlow and PyTorch.

import numpy as np

# Creating a 3D tensor (2x2x2 array)
tensor = np.array([[[1, 2], [3, 4]],  # Layer 1
                   [[5, 6], [7, 8]]]) # Layer 2
print("3D Tensor:")
print(tensor)

# Accessing a specific element from the tensor
# Example: Access element in Layer 2, Row 1, Column 2
element = tensor[1, 0, 1]
print("\nAccessed Element:", element)
