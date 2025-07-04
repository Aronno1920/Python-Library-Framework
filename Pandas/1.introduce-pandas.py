import pandas as pd  

# Creating a dictionary with student data
student_list = {  
    'name': ["Sanaya", "Ahmed", "Aairah", "Selim", "Afsara"], 
    'age': [6, 5, 7, 38, 26],  
    'dept': ["Bangla", "English", "Math", "ML", "English"]  
}
print("Orginal List:\n", student_list)

# Converting the dictionary into a pandas DataFrame
pdlist = pd.DataFrame(student_list)  
print("\nPandas DataFrame:\n", pdlist)
