import pandas as pd  

# Creating a dictionary with student data
student_list = {  
    'name': ["Sanaya", "Ahmed", "Aairah", "Selim", "Afsara"], 
    'age': [6, 5, 7, 38, 26],  
    'dept': ["Bangla", "English", "Math", "ML", "English"]  
}
print("Orginal List: ", student_list)

# Converting the dictionary into a pandas DataFrame
pdlist = pd.DataFrame(student_list)  
print("\nPandas DataFrame:\n", pdlist)

# Displaying the first 5 rows of the DataFrame
print("\nShow Top 5 rows:\n",pdlist.head())

print("\nShow Top 10 rows:\n",pdlist.head(10))
print("\nShow tails rows:\n",pdlist.tail())

# Displaying summary information about the DataFrame
print("\nSummary Information:\n", pdlist.info())

# Generating descriptive statistics for numeric columns
print("\nDescriptive Statistics :\n",pdlist.describe())  
