import numpy as np  # Importing the NumPy library
import time  # Importing the time module for performance measurement

# Generating a 1D array with 1,000,000 random float values
arr1 = np.random.rand(1000000)  

# Generating another 1D array with 1,000,000 random float values
arr2 = np.random.rand(1000000)

# Recording the start time for loop-based addition
start_time = time.time()  

# Creating an empty array with the same shape as arr1 for storing results
result_loop = np.zeros_like(arr1)  
for i in range(len(arr1)):  # Looping through each index of the arrays
    result_loop[i] = arr1[i] + arr2[i] 
loop_duration = time.time() - start_time  # Calculating loop duration

# Recording the start time for vectorized addition
start_time = time.time()  

# Performing vectorized addition using NumPy
result_vectorized = arr1 + arr2  

# Calculating vectorized duration
vectorized_duration = time.time() - start_time  

# Printing the time taken by the loop-based operation
print("Loop Duration: ", loop_duration)

# Printing the time taken by the vectorized operation
print("Vectorized Duration: ", vectorized_duration)  
