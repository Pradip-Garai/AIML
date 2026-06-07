import numpy as np

# Create a sample array for aggregate functions
agg_array = np.array([1, 2, 3, 4, 5])
print(f"Sample Array: {agg_array}")

# Calculate the mean of the array
array_mean = agg_array.mean()
print(f"Mean of the array: {array_mean}")

# Calculate the sum of the array
array_sum = agg_array.sum()
print(f"Sum of the array: {array_sum}")

# Calculate the standard deviation of the array
array_std = agg_array.std()
print(f"Standard deviation of the array: {array_std}")

# Calculate the variance of the array
array_var = agg_array.var()
print(f"Variance of the array: {array_var}")