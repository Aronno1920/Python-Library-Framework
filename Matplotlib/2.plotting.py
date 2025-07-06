import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting
import numpy as np  # Importing the NumPy library

# xpoint = np.array([1, 8])
# ypoint = np.array([3, 10])
# Plotting only points without a line (commented out)
# plt.plot(xpoint, ypoint, "o")  

xpoint = np.array([1, 2, 6, 8])  
ypoint = np.array([3, 8, 1, 10])
# Plotting a line connecting the points
plt.plot(xpoint, ypoint)  

plt.xlabel("X Point")  
plt.ylabel("Y Point")
plt.title("Matplotlab Plotting")

plt.show()
