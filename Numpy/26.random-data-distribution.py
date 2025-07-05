import numpy as np

# Generates a 1-dimensional NumPy array of 20 elements named 'arr'.
# The elements are randomly chosen from the list [3, 5, 9, 7].
# The 'p' parameter specifies the probability of choosing each corresponding element:
# - 3 has a 10% chance (0.1)
# - 5 has a 30% chance (0.3)
# - 5 has a 50% chance (0.5)
# - 7 has a 1% chance (0.1), meaning it will never be chosen.
arr = np.random.choice([3,5,9,7], p=[0.1,0.3,0.5,0.1], size=(20))
print("Random Data Distribution:\n", arr)

# Generates a 3x5 NumPy array (3 rows, 5 columns) named 'arr_2d'.
# The elements of the array are randomly chosen from the list [3, 5, 9, 7].
# The 'p' parameter specifies the probability of choosing each corresponding element:
# - 3 has a 10% chance (0.1)
# - 5 has a 30% chance (0.3)
# - 9 has a 40% chance (0.4)
# - 7 has a 2% chance (0.2), meaning it will never be chosen.
arr_2d = np.random.choice([3,5,9,7], p=[0.1,0.3,0.4,0.2], size=(3,5))
print("Random Data Distribution:\n", arr_2d)