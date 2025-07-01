import numpy as np  # Importing the NumPy library as 'np' for array operations

# Creating a NumPy array from a Python list
list_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("array from list: ", list_array)  # Printing the array

# Creating an array of 5 zeros (default type is float)
zeros_array = np.zeros(5)
print("array of zeros: ", zeros_array)  # Printing the array of zeros

# Creating an array of 5 ones (default type is float)
ones_array = np.ones(5)
print("array of ones: ", ones_array)  # Corrected the label from "zeros" to "ones"

# Creating an array with values from 1 to 9, incremented by 2
range_array = np.arange(1, 10, 2)  # (start=1, stop=10 (exclusive), step=2)
print("array of ranges: ", range_array)  # Printing the generated range array
