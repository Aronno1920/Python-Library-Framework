import pandas as pd  

new_var = [1,2,3]

series1 = pd.Series(new_var)
print("Pandas Series:\n", series1)

series2 = pd.Series(new_var, index=["a","b","c"])
print("\nPandas series index:\n", series2)

series3 = pd.Series(new_var)

data_dict = {'a':1,'b':2, 'c':3}
print(series3,)