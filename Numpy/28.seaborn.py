import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Creating a kernel density estimate (KDE) plot of the given data
sb.displot([0, 1, 2, 3, 4, 5, 6], kind='kde')  

# Displaying the plot
plt.show()  