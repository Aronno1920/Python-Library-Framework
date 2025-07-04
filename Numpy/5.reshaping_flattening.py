import numpy as np  # Importing the NumPy library

# Creating a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5, 6])

# Reshaping the 1D array into a 2D array with 2 rows and 3 columns
arr2 = arr1.reshape(2, 3)

print("Original 1D array:\n", arr1)  # Output: [1 2 3 4 5 6]
print("Resharped 2D array:\n", arr2)  # Output: [[1 2 3], [4 5 6]]

# Creating a 2D (multi-dimensional) array with 3 rows and 3 columns
multi_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Multi-dimension array\n", multi_arr)  # Output: 3x3 matrix

# Flattening the 2D array into a 1D array
flatt_arr = multi_arr.flatten()
print("Flatten of array\n", flatt_arr)  # Output: [1 2 3 4 5 6 7 8 9]
