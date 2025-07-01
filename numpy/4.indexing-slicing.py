import numpy as np  # Importing NumPy library for numerical operations

# Creating a NumPy array with values from 9 to 1
arr = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

# Accessing the first element (index 0)
first_el = arr[0]
print("first element: ", first_el)  # Output: 9

# Accessing the last element using negative indexing (index -1)
last_el = arr[-1]
print("last element: ", last_el)  # Output: 1

# Slicing the array from index 1 to 2 (2 is exclusive)
slice_arr = arr[1:2]
print("Slice of array 1:", slice_arr)  # Output: [8]
