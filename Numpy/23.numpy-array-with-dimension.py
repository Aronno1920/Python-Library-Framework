import numpy as np 

# Creates a NumPy array named 'arr_of_2d' from the given list. The 'ndmin=2' argument ensures that the resulting array will have at least 2 dimensions.
arr_of_2d = np.array([1,2,3,4,5,6,7,8,9], ndmin=2) 

# Creates a NumPy array named 'arr_of_4d' from the given list. The 'ndmin=4' argument ensures that the resulting array will have at least 4 dimensions.
arr_of_4d = np.array([1,2,3,4,5,6,7,8,9], ndmin=4) 

# Creates a NumPy array named 'arr_of_5d' from the given list. The 'ndmin=5' argument ensures that the resulting array will have at least 5 dimensions.
arr_of_5d = np.array([1,2,3,4,5,6,7,8,9], ndmin=5) 

print(f"Number of Dimension {arr_of_2d.ndim} & Example of array: ", arr_of_2d)
print(f"Number of Dimension {arr_of_4d.ndim} & Example of array: ", arr_of_4d)
print(f"Number of Dimension {arr_of_5d.ndim} & Example of array: ", arr_of_5d)