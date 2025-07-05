import numpy as np

# Creates a 1-dimensional NumPy array named 'arr_original' with elements from 1 to 6.
arr_orginal = np.array([1, 2, 3, 4, 5, 6])  # Initializing a 1D array
print("Orginal Array:\n", arr_orginal)

np.random.shuffle(arr_orginal)  # Shuffling the elements of the array in-place
print("Permuted Array:\n", arr_orginal)

print('\n------------------- Random Permutation -------------------\n')

arr_multi_dimention = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Creating a 2D array

premut_rows = np.random.permutation(arr_multi_dimention)  # Randomly permuting the rows of the array

permut_cols = np.random.permutation(arr_multi_dimention.T).T  # Transposing, permuting rows (i.e., columns), then transposing back

print("Multi-dimention Array:\n", arr_multi_dimention)
print("Permutated Rows:\n", premut_rows)
print("Permutated Columns:\n", permut_cols)

