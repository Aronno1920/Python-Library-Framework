import numpy as np

###### one dimensional array
# array = np.array([1,2,3,4,5,6,7,8,9])
# print(type(array))

# print(array)
# print("first element: ", array[0])
# print("last element: ", array[-1])
# print("------------")

###### two dimensional array
# matrix = np.array([[1,2,3],[4,5,6]])
# print(type(matrix))

# reshaped_matrix = matrix.reshape(3,2)
# print(reshaped_matrix)
# print("------------")

###### matrix addition
mat1 = np.array([[1,2,3],[4,5,6]])
mat2 = np.array([[2,4,3],[4,1,5]])

mat_sum = mat1+mat2
print ("matrix_sum:\n", mat_sum)

mat_multi = mat1 * mat2
print("matrix_multiplication:\n", mat_multi)

mat_multi_scalar = mat1+5
print ("matrix_multiplication_scalar:\n", mat_multi_scalar)