import numpy as np

# Create a sample array for attribute analysis
attr_array = np.random.randint(10, 90, (5, 5))
print(f"Sample Array for Analysis:\n{attr_array}")

# Get array dimensions (shape)
print(f"\nShape of array: {attr_array.shape}")

# Get number of dimensions
print(f"Number of dimensions: {attr_array.ndim}")

# Get total number of elements
print(f"Total number of elements: {attr_array.size}")

# Get data type of elements
print(f"Data type of elements: {attr_array.dtype}")