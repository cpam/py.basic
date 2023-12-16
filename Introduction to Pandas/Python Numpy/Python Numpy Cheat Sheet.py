import numpy as np

# Example of NumPy operations
# Package/Method    Description    Syntax and Code Example

# Importing NumPy - Imports the NumPy library with the alias np.
# Syntax: import numpy as np
# Example:
imported_numpy = np

# np.array() - Creates a one or multi-dimensional array.
# Syntax:
# 1. array_1d = np.array([list1 values]) # 1D Array
# 2. array_2d = np.array([[list1 values], [list2 values]]) # 2D Array
# Example:
array_1d = np.array([1, 2, 3])  # 1D Array
array_2d = np.array([[1, 2], [3, 4]])  # 2D Array

# Numpy Array Attributes - Various operations that can be performed on NumPy arrays.
# Example:
# 1. Calculate the mean of array elements
mean_value = np.mean(array)

# 2. Calculate the sum of array elements
sum_value = np.sum(array)

# 3. Find the minimum value in the array
min_value = np.min(array)

# 4. Find the maximum value in the array
max_value = np.max(array)

# 5. Compute the dot product of two arrays
dot_product = np.dot(array_1, array_2)
