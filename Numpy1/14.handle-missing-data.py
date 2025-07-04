import numpy as np

# Creating an array with some NaN (missing) values
data = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8, 9])  
print("Orginal Data: ", data)

# Identifying which elements are NaN (returns a boolean array)
print("Identity missing data: ", np.isnan(data))  

# Replacing all NaN values with 0
replace_data = np.nan_to_num(data, nan=0)  
print("Replaced Data: ", replace_data)

# Removing all NaN values from the array
removed_data = data[~np.isnan(data)]  
print("Removed Data: ", removed_data)