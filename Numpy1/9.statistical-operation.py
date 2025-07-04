import numpy as np  # Importing the NumPy library

# Creating a 1D array of numerical data
data = np.array([10, 20, 30, 40, 50])

# Finding the maximum value in the array
v_max = data.max()

# Finding the minimum value in the array
v_min = data.min()

# Calculating the mean (average) of the array
v_mean = data.mean()

# Calculating the median (middle value) of the array
v_mediam = np.median(data)

# Calculating the standard deviation (spread of data)
v_std = data.std()

# Printing the results
print("Data:", data)
print("Max value:", v_max)
print("Min value:", v_min)
print("Mean value:", v_mean)
print("Median value:", v_mediam)
print("Standard Deviation value:", v_std)
