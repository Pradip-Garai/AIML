import numpy as np

# Create a sample matrix for manipulation
manip_matrix = np.random.randint(1, 10, (2, 3))
print(f"Original Matrix:\n{manip_matrix}")

# Transpose using .T attribute
transposed_t = manip_matrix.T
print(f"\nTransposed Matrix (.T):\n{transposed_t}")

# Transpose using np.transpose() function
transposed_func = np.transpose(manip_matrix)
print(f"\nTransposed Matrix (np.transpose):\n{transposed_func}")

# Reshape an array
print(f"\nOriginal matrix shape: {manip_matrix.shape}")
reshaped_matrix = np.reshape(manip_matrix, (3, 2))
print(f"Reshaped Matrix (to 3x2):\n{reshaped_matrix}")