import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.reshape(2,3)

print("Original 1D array:\n", arr1)
print("Resharped 2D array:\n", arr2)


# Flatten make multidimension to single
multi_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Multi-dimension array\n", multi_arr)

flatt_arr = multi_arr.flatten()
print("Flatten of array\n", flatt_arr)