import numpy as np  # Importing the NumPy library

# Generating a 3x3 array with random float values between 0 and 1
rand_data = np.random.rand(3,3)  
print("Generated Data:\n", rand_data)  # Printing the generated random data

# Loading data from 'data.csv', skipping the header, using comma delimiter, and handling missing or malformed values
data = np.genfromtxt("data.csv", delimiter=",", skip_header=1, dtype=None, encoding=None, errors='ignore', filling_values=np.nan)  
print("Loaded Data:\n", data)  # Printing the loaded data from the CSV file
