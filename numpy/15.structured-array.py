import numpy as np  # Importing the NumPy library

# Creating a structured array with fields: Id, Name, Age
# Defining data types: integer for Id and Age, Unicode string (max length 10) for Name
data = np.array([(1, 'Ahmed', 30), (2, 'Aairah', 10), (3, 'Sanaya', 15)],  
                dtype=[('Id', int), ('Name', 'U10'), ('Age', int)])  

# Printing the entire structured array
print('Stuctured Data:', data)  

# Heading for data access
print('\nAccessing specific data')

# Accessing only the 'Name' field
print("Names: ", data['Name'])

# Accessing only the 'Age' field
print("Ages: ", data['Age'])  
