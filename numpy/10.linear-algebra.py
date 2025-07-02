import numpy as np  # Importing the NumPy library

# Defining the first 2x2 matrix
matrix1 = np.array([[1, 2],
                    [3, 4]])

# Defining the second 2x2 matrix
matrix2 = np.array([[5, 6],
                    [7, 8]])

# Performing matrix multiplication using np.dot()
result_dot = np.dot(matrix1, matrix2)

# Printing the first matrix
print("Matrix 1:\n", matrix1)

# Printing the second matrix
print("Matrix 2:\n", matrix2)

# Printing the result of matrix multiplication using np.dot()
print("Matrix multiplication:\n", result_dot)

# Performing matrix multiplication using the '@' operator (preferred in Python 3.5+)
result_set = matrix1 @ matrix2
print("Matrix set result:\n", result_set)
