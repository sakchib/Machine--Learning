# Linear Algebra is the study of vectors, matrices, and linear transformations.
# It is fundamental to many areas, including machine learning, physics, and computer science.

import numpy as np

# Example of a 2x2 matrix
matrix = np.array([[1, 2],  # Row 1
                   [3, 4]]) # Row 2
print("Matrix:")
print(matrix)

# Example of a vector (1D array)
vector = np.array([5, 6])  # A vector with 2 elements
print("\nVector:")
print(vector)

# Matrix-vector multiplication
# This operation combines the rows of the matrix with the elements of the vector
result = np.dot(matrix, vector)  # Dot product
print("\nMatrix-Vector Multiplication Result:")
print(result)
