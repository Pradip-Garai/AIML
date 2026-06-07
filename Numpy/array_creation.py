import numpy as np

# Create 1D array from a list
list_data = [1, 2, 3, 4, 5]
np_arr_from_list = np.array(list_data)
print(f"1D Array from list: {np_arr_from_list}, type: {type(np_arr_from_list)}")

# Create 2D array from a tuple of tuples
tuple_data = ((1, 2, 3), (4, 5, 6))
np_arr_2d = np.array(tuple_data)
print(f"\n2D Array from tuple: {np_arr_2d}")

# Create a float matrix explicitly defining dtype
float_matrix = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], dtype=float)
print(f"\nFloat Matrix: {float_matrix}")

# Create an array of zeros (3 rows, 5 columns)
zeros_array = np.zeros((3, 5))
print(f"\nZeros Array:\n{zeros_array}")

# Create an array of ones (3 rows, 3 columns)
ones_array = np.ones((3, 3))
print(f"\nOnes Array:\n{ones_array}")

# Create an array filled with a specific value (5 rows, 6 columns, value 7)
full_array = np.full((5, 6), 7)
print(f"\nFull Array (with 7s):\n{full_array}")

# Create an identity matrix (4x4)
identity_matrix = np.eye(4)
print(f"\nIdentity Matrix:\n{identity_matrix}")

# Create a NumPy array with random float values (3 rows, 4 columns)
random_floats = np.random.random((3, 4))
print(f"\nRandom Floats Array:\n{random_floats}")

# Create a NumPy array with random integer values in a specific range (10-19, 2 rows, 3 columns)
random_integers = np.random.randint(10, 20, (2, 3))
print(f"\nRandom Integers Array:\n{random_integers}")

# Create an array with evenly spaced values (linspace)
# 6 values from 10 to 50 (inclusive)
linspace_array = np.linspace(10, 50, 6)
print(f"\nLinspace Array: {linspace_array}")

# Create an array with values within a range (arange)
# from 10 to 50 (exclusive), with a step of 6
arange_array = np.arange(10, 50, 6)
print(f"\nArange Array: {arange_array}")

# Convert a Python list to a NumPy array using np.asarray
python_list = [1, 2, 3, 4, 5]
converted_np_array = np.asarray(python_list)
print(f"\nConverted List to NumPy Array: {converted_np_array}, type: {type(converted_np_array)}")