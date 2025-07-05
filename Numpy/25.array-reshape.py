import numpy as np

# Creates a 1-dimensional NumPy array named 'arr_original' with elements from 1 to 6.
arr_orginal = np.array([1,2,3,4,5,6])

# Reshapes 'arr_original' into a 2x3 (2 rows, 3 columns) 2-dimensional array. By default, NumPy uses 'C' (row-major) order.
arr_reshape = arr_orginal.reshape(2,3)
# Reshapes 'arr_original' into a 2x3 2-dimensional array using 'C' (row-major) order, which is the default. This explicitly demonstrates row-major reshaping.
arr_row_major = arr_orginal.reshape(2,3, order='C')
# Reshapes 'arr_original' into a 2x3 2-dimensional array using 'F' (Fortran-style, column-major) order. This means elements are filled column by column.
arr_column_major = arr_orginal.reshape(2,3, order='F')

print("Orginal Array:\n",arr_orginal)
print("Reshaped Array:\n",arr_reshape)

print("Reshaped Array [Row]:\n",arr_row_major)
print("Reshaped Array [Column]:\n",arr_column_major)