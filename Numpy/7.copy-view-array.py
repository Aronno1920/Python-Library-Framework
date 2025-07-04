import numpy as np  # Import the NumPy library

# Creating the original array
orginal_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Creating a deep copy of the original array (independent copy)
copy_arr = orginal_arr.copy()

# Creating a view of the original array (shares the same data in memory)
view_arr = orginal_arr.view()

# Printing all arrays
print("Original array: ", orginal_arr)  # Output: [1 2 3 4 5 6 7 8 9]
print("Copied array: ", copy_arr)       # Output: [1 2 3 4 5 6 7 8 9]
print("Viewed array: ", view_arr)       # Output: [1 2 3 4 5 6 7 8 9]

# Modifying the view array — this will affect the original array too
view_arr[0] = 0
print("Modification of viewed array: ", view_arr)       # Output: [0 2 3 4 5 6 7 8 9]
