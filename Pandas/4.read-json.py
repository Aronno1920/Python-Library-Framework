import pandas as pd

file_path = 'Pandas\data.json'
data_frame = pd.read_json(file_path)

print("Dataframe from JSON:\n", data_frame)
print("Get max rows:\n", pd.options.display.max_rows)
