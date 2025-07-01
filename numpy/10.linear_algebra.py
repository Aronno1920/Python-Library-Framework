import numpy as np  # Importing the NumPy library

# Defining first 2x2 matrix
matrix1 = np.array([[1, 2],
                    [3, 4]])

# Defining second 2x2 matrix
matrix2 = np.array([[5, 6],
                    [7, 8]])

# Performing matrix multiplication (dot product) of matrix1 and matrix2
result_dot = np.dot(matrix1, matrix2)

# Printing the first matrix
print("Matrix 1: ", matrix1)

# Printing the second matrix
print("Matrix 2: ", matrix2)

# Printing the result of matrix multiplication
print("Matrix multiplication: ", result_dot)
