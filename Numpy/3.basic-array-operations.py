import numpy as np  # Importing the NumPy library

# Creating two 1D arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Element-wise addition of arr1 and arr2
ar_sum = arr1 + arr2
print("Addition:", ar_sum)  # Output: [6 8 10 12]

# Element-wise multiplication of arr1 and arr2
ar_multi = arr1 * arr2
print("Multiplication:", ar_multi)  # Output: [5 12 21 32]

# Slicing arr1 to get elements from index 1 to 2 (exclusive)
slice_arr1 = arr1[1:2]
print("Slice of array 1:", slice_arr1)  # Output: [2]

# Step slicing arr1 with step size 3 (start to end with step 3)
st_slice_arr1 = arr1[::3]
print("Step slice of array 1:", st_slice_arr1)  # Output: [1 4]
