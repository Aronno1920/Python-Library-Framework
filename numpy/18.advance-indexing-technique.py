import numpy as np  # Importing the NumPy library

# Creating an array with values from 0 to 9
# arr = np.arange(10)  

# Selecting only even numbers using boolean indexing
# even_number = arr[arr % 2 == 0]  

# print("Orginal array:\n", arr)  # Printing the original array
# print("Even numbers:\n", even_number)  # Printing the even numbers

# print('--------------------------------')

# Creating a 3x3 array
array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])  

# Selecting elements at (0,2), (1,0), and (2,2)
selected_element = array[[0, 1, 2], [2, 0, 2]]  

print("Orginal array:\n", array)  # Printing the original array
print("Selectd Elements:\n", selected_element)  # Printing the selected elements
