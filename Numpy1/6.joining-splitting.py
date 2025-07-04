import numpy as np  # Importing the NumPy library with alias 'np'

# Creating two 1D arrays
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6])

# hstack is used to horizontally stack (join) arrays
array_hstack = np.hstack((ar1, ar2))
print("Horizontally stacked array \n", array_hstack)  # Output: [1 2 3 4 5 6]
print('-----------------------------------')

# Creating a 2D array with two rows and nine columns
large_arr = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
])
print("Original array before split\n", large_arr)

# hsplit is used to split the array horizontally into 3 parts (columns)
# This will result in three arrays with shape (2, 3)
array_hsplit = np.hsplit(large_arr, 3)

# Printing each split array
for spl_arr in array_hsplit:
    print("Split array of original array\n", spl_arr)
