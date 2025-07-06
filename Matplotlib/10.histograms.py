import matplotlib.pyplot as plt
import numpy as np

# data = [2,3,3,4,6,6,4,4,5,7,7,7,7,7]
# plt.hist(data)
# plt.xlabel('value')
# plt.ylabel('frequency')
# plt.title("Histogram Plot")
# plt.show()

data = np.random.randint(100, size=(1, 10))

plt.hist(data, bins=3)
plt.title("Customize Histogram Plot")
plt.show()