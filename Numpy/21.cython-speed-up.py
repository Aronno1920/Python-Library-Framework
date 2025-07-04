import numpy as np  
import time

# Defining a function to calculate the sum of squares
def sum_of_squares(x):  
    return np.sum(x ** 2)

# Generating an array with 1,000,000 random float values
arr = np.random.rand(1000000)  

# Recording the start time
start_time = time.time()  
result = sum_of_squares(arr)  # Calling the function to compute the sum of squares
end_time = time.time()  

print(f"Result: ", result)
print(f"Time Different: {end_time - start_time} seconds.")

