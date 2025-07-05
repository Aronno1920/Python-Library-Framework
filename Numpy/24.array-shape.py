import numpy as np

# Creates a 1-dimensional NumPy array.
arr_1d = np.array([1,2,3,4,5])

# Creates a 2-dimensional NumPy array, representing rows and columns.
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])

# Creates a 3-dimensional NumPy array, representing a single 3x3 matrix within a dimension.
arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# Creates a NumPy array, the 'ndmin=4' argument explicitly ensures that the resulting array will have at least 4 dimensions, even if the data itself only requires one.
arr_4d = np.array([1,2,3,4,5], ndmin=4)


# For a 1D array with 5 elements, the shape will be (5,).
print("Shape of 1D Array: ",arr_1d.shape)
# For a 2D array with 2 rows and 4 columns, the shape will be (2, 4).
print("Shape of 2D Array: ",arr_2d.shape)
# For a 3D array with 1 "layer", 3 rows, and 3 columns, the shape will be (1, 3, 3).
print("Shape of 3D Array: ",arr_3d.shape)
# For a 4D array with 1 "layer", 1 rows, 1 columns and 5 elements, the shape will be (1, 1, 1, 5).
print("Shape of 4D Array: ",arr_4d.shape)