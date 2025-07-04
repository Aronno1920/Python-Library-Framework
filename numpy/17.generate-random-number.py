import numpy as np  # Importing the NumPy library

# Generating a single random float between 0 and 1
random_float = np.random.rand()  
print("Generate single float number:\n", random_float)

# Generating a 1D array with 10 random float values
multi_float_num = np.random.rand(10)  
print("\nGenerate multiple random number:\n", multi_float_num)

# Generating a 2D array (3 rows, 4 columns) of random float values
random_float_array = np.random.rand(3, 4)  
print("\nGenerate 2D array:\n", random_float_array)

# Generating a 2D array with random choices from a list
random_array_choice = np.random.choice([1, 2, 3, 4, 5, 6], size=(2, 3))  
print("\nGenerate 2D array:\n", random_array_choice)

# Generating a 3D array with shape (3, 4, 2) of random float values
random_array = np.random.rand(3, 4, 2)  
print("\nGenerate 3D array:\n", random_array)

print('-------------------------------------------------')  # Printing a visual separator

# Generating a single random int between 0 and 50
random_int = np.random.randint(50)  
print("\nGenerate single int number:\n", random_int)

# Generating a 2D array (3 rows, 4 columns) of random integers between 0 and 999
random_int_array = np.random.randint(1000, size=(3, 4))  
print("\nGenerate 2D array:\n", random_int_array)
