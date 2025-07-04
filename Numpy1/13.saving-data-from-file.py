import numpy as np  # Importing the NumPy library

# Generating a 10x3 array with random float values between 0 and 1
data = np.random.rand(10,3)  
print("Show generated data:", data.size)

# Saving the data to a file with a .csv.xlsx extension using comma as delimiter
np.savetxt('generate_data.csv.xlsx', data, delimiter=',')  
print('Data has beed exported to csv file') 

# Saving the data to a text file with each row on a new line
np.savetxt('generate_data.txt', data, delimiter='\n')  
print('Data has beed exported to txt file')  

# Incorrect usage: savetxt cannot be used to save in .npy format
np.savetxt('generate_data.npy', data)  
print('Data has beed exported to npy file')  
