import numpy as np
import pandas as pd

# Generate a 5x3 matrix of random float numbers between 0 and 1
data = np.random.rand(5, 3)

# Create a DataFrame from the NumPy array with column names A, B, and C
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Print the raw NumPy array
print("Numpy array:\n", data)

# Print the formatted DataFrame
print("\nPandas DataFrame:\n", df)
