import numpy as np

# Demonstrate list concatenation vs. NumPy array addition
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(f"List concatenation: {list1 + list2}")

# Create two random arrays for mathematical operations
array_a = np.random.randint(0, 10, (3, 3))
array_b = np.random.randint(10, 20, (3, 3))
print(f"\nArray A:\n{array_a}")
print(f"\nArray B:\n{array_b}")

# Element-wise addition using operator
print(f"\nAddition (A + B):\n{array_a + array_b}")

# Element-wise multiplication using operator
print(f"\nMultiplication (A * B):\n{array_a * array_b}")

# Using NumPy's ufuncs for element-wise operations
print(f"\nNumPy Add (np.add(A,B)):\n{np.add(array_a, array_b)}")
print(f"\nNumPy Subtract (np.subtract(A,B)):\n{np.subtract(array_a, array_b)}")
print(f"\nNumPy Multiply (np.multiply(A,B)):\n{np.multiply(array_a, array_b)}")
print(f"\nNumPy Divide (np.divide(A,B)):\n{np.divide(array_a, array_b)}")