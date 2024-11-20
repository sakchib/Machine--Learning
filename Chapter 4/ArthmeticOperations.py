# Explanation:
# NumPy:

# np.dot(): For matrix multiplication (dot product).
# np.power(): Performs element-wise exponentiation.
# np.transpose(): Computes the transpose of the tensor.
# np.linalg.det(): Computes the determinant of a square matrix.
# np.linalg.inv(): Computes the inverse of a square matrix.


# PyTorch:
# torch.matmul(): Performs matrix multiplication.
# tensor.view(): Reshapes the tensor without changing the underlying data.
# GPU support: Move tensors to GPU for accelerated computation using .to("cuda").


import numpy as np

# Define two 2D tensors
tensor1 = np.array([[1, 2], [3, 4]])
tensor2 = np.array([[5, 6], [7, 8]])

print("Tensor 1:")
print(tensor1)

print("\nTensor 2:")
print(tensor2)

# Matrix multiplication (dot product)
dot_product = np.dot(tensor1, tensor2)
print("\nMatrix Multiplication (Dot Product):")
print(dot_product)

# Element-wise power (exponentiation)
power_result = np.power(tensor1, 2)
print("\nElement-wise Power (Tensor 1^2):")
print(power_result)

# Transpose of a tensor
transpose_result = np.transpose(tensor1)
print("\nTranspose of Tensor 1:")
print(transpose_result)

# Determinant of a tensor (only for square tensors)
determinant = np.linalg.det(tensor1)
print("\nDeterminant of Tensor 1:")
print(determinant)

# Inverse of a tensor (only for square tensors)
inverse_result = np.linalg.inv(tensor1)
print("\nInverse of Tensor 1:")
print(inverse_result)





import torch

# Create two tensors using PyTorch
tensor1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
tensor2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

print("Tensor 1 (PyTorch):")
print(tensor1)

print("\nTensor 2 (PyTorch):")
print(tensor2)

# Addition
add_result = tensor1 + tensor2
print("\nAddition (Tensor 1 + Tensor 2):")
print(add_result)

# Subtraction
sub_result = tensor1 - tensor2
print("\nSubtraction (Tensor 1 - Tensor 2):")
print(sub_result)

# Element-wise multiplication
mul_result = tensor1 * tensor2
print("\nElement-wise Multiplication (Tensor 1 * Tensor 2):")
print(mul_result)

# Matrix multiplication (dot product)
dot_result = torch.matmul(tensor1, tensor2)
print("\nMatrix Multiplication (Dot Product):")
print(dot_result)

# Reshaping tensors
reshaped_tensor = tensor1.view(4, 1)  # Reshape to 4 rows and 1 column
print("\nReshaped Tensor 1:")
print(reshaped_tensor)

# Move tensor to GPU if available
if torch.cuda.is_available():
    tensor1_gpu = tensor1.to("cuda")
    print("\nTensor 1 moved to GPU:")
    print(tensor1_gpu)
