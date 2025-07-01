import numpy as np  # Importing the NumPy library and giving it the alias 'np'

###### one dimensional array
# array = np.array([1,2,3,4,5,6,7,8,9])  # Creating a 1D NumPy array with values 1 to 9
# print(type(array))                    # Printing the type of the object to confirm it's a NumPy array

# print(array)                          # Displaying the full array
# print("first element: ", array[0])    # Accessing the first element (index 0)
# print("last element: ", array[-1])    # Accessing the last element using negative indexing
# print("------------")                 # Printing a separator line

###### two dimensional array
# matrix = np.array([[1,2,3],[4,5,6]])  # Creating a 2D array (matrix) with two rows
# print(type(matrix))                  # Confirming that it is a NumPy ndarray

# reshaped_matrix = matrix.reshape(3,2)  # Reshaping the 2x3 matrix into a 3x2 matrix
# print(reshaped_matrix)                 # Printing the reshaped matrix
# print("------------")                  # Separator line

###### matrix addition
mat1 = np.array([[1,2,3],[4,5,6]])       # Creating first 2D matrix (2x3)
mat2 = np.array([[2,4,3],[4,1,5]])       # Creating second 2D matrix (2x3)

mat_sum = mat1 + mat2                    # Element-wise addition of mat1 and mat2
print ("matrix_sum:\n", mat_sum)        # Printing the result of matrix addition

mat_multi = mat1 * mat2                  # Element-wise multiplication (not matrix multiplication)
print("matrix_multiplication:\n", mat_multi)  # Printing the result of element-wise multiplication

mat_multi_scalar = mat1 + 5              # Adding scalar value 5 to each element of mat1
print ("matrix_multiplication_scalar:\n", mat_multi_scalar)  # Printing the result
