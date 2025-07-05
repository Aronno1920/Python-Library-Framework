import pandas as pd  

myvariable = [1,2,3,4,5,6]
myseries = pd.Series(myvariable)
print("Pandas Series:\n", myseries)


# Creating a dictionary with student data
student_list = {  
    'name': ["Sanaya", "Ahmed", "Aairah", "Selim", "Afsara"], 
    'age': [6, 5, 7, 38, 26],  
    'dept': ["Bangla", "English", "Math", "ML", "English"]  
}
print("\nOrginal List:\n", student_list)

# Converting the dictionary into a pandas DataFrame
pdlist = pd.DataFrame(student_list)  
print("\nPandas DataFrame:\n", pdlist)
