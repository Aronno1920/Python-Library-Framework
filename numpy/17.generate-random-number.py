import numpy as np

# Generating a single random float between 0 and 1
random_num = np.random.rand()  
print("Generate single random number:\n", random_num)  # Printing the single random number

# Generating a 1D array with 10 random float values
multi_sample_num = np.random.rand(10)  
print("\nGenerate multiple random number:\n", multi_sample_num)

# Generating a 2D array (3 rows, 4 columns) of random float values
random_array = np.random.rand(3,4)  
print("\nGenerate 2D array:\n", random_array)

# Generating a 3D array with shape (3, 4, 2) of random float values
random_array = np.random.rand(3,4,2)  
print("\nGenerate 3D array:\n", random_array)


