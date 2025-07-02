import numpy as np  # Importing the NumPy library

arr1 = np.array([1,2,3])  # Creating a 1D array
arr2 = np.array([[10],[20],[30]])  # Creating a 2D column vector

result = arr1 + arr2  # Broadcasting addition between arr1 and arr2

print("Array 1:\n", arr1)  # Printing arr1
print("Array 2:\n", arr2)  # Printing arr2
print("Broadcasting Addition Result:\n", result)  # Printing the result of broadcasting addition
print('------------------------------------')  # Separator for output

data = np.array([1,2,3,4,5,6])  # Creating a 1D array

squared_data = data ** 2  # Squaring each element in the array

print("Orginal Data:\n", data)  # Printing the original array
print("Squared Result:\n", squared_data)  # Printing the squared result
