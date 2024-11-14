# Import necessary library
import numpy as np

# Define a sample vector
vector = np.array([3, -4, 5])

# L1 Norm (Manhattan Norm)
# The L1 norm is the sum of the absolute values of each element
l1_norm = np.sum(np.abs(vector))
print("L1 Norm (Manhattan Norm):", l1_norm)  # Expected result: 3 + 4 + 5 = 12


# L2 Norm (Euclidean Norm)
# The L2 norm is the square root of the sum of the squares of each element
l2_norm = np.sqrt(np.sum(vector ** 2))
print("L2 Norm (Euclidean Norm):", l2_norm)  # Expected result: √(3^2 + (-4)^2 + 5^2) = √50 ≈ 7.071

# Alternatively, using numpy's norm function for L2 norm
l2_norm_alt = np.linalg.norm(vector)
print("L2 Norm (Using numpy's norm function):", l2_norm_alt)


# Infinity Norm (Max Norm)
# The Infinity norm is the maximum absolute value of the elements
inf_norm = np.max(np.abs(vector))
print("Infinity Norm (Max Norm):", inf_norm)  # Expected result: max(|3|, |-4|, |5|) = 5
