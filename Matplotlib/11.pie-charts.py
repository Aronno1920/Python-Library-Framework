import matplotlib.pyplot as plt
import numpy as np

data = np.array([23, 45, 63, 32, 20])
labels = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango']

plt.figure(figsize=(6, 6))
plt.pie(
    data,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    explode=[0, 0, 0.1, 0, 0],
    shadow=False
)

plt.title("Fruit Distribution")
plt.show()

