import numpy as np  # Importing NumPy for array operations

# Creating two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 4, 3])

# Element-wise addition using np.add()
arr_sum = np.add(arr1, arr2)
print("Addition:\n", arr_sum)  # Output: [3 6 6]

# Element-wise subtraction using np.subtract()
arr_sub = np.subtract(arr1, arr2)
print("Subtraction:\n", arr_sub)  # Output: [-1 -2 0]

# Element-wise multiplication using np.multiply()
arr_multi = np.multiply(arr1, arr2)
print("Multiplication:\n", arr_multi)  # Output: [2 8 9]

# Element-wise division using np.divide()
arr_div = np.divide(arr1, arr2)
print("Division:\n", arr_div)  # Output: [0.5 0.5 1. ]
