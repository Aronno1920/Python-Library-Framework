import pandas as pd

file_path = 'Pandas\data.csv'
data_frame = pd.read_csv(file_path)

print("Dataframe from CSV:\n", data_frame)
print("Get max rows:\n", pd.options.display.max_rows)
