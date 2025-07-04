import numpy as np  

# Generating a large array with 1,000,000 random float values
arr = np.random.rand(1000000)  

# Defining a function to sum array elements using a loop
def sum_with_loop(array):  
    total = 0 
    for num in array:
        total += num
    return total

# Defining a function to sum array elements using NumPy, Returning the sum using NumPy's optimized function
def sum_with_numpy(array):  
    return np.sum(array)


# Printing the sum calculated with a loop
print("Sum with loop: ", sum_with_loop(arr))  

# Printing the sum calculated with NumPy
print("Sum with numpy: ", sum_with_numpy(arr))  
