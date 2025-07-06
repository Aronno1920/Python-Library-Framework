import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting
import numpy as np  # Importing the NumPy library

# ypoints = np.array([3, 8, 1, 10])  # Defining Y-axis points (commented out)
# plt.plot(ypoints, marker='o')  # Plotting with circle markers (commented out)
# plt.show()  # Displaying the plot (commented out)

xpoints = np.array([1, 2, 3, 4, 5])  # Defining X-axis points
ypoints = np.array([10, 15, 25, 30, 20])  # Defining Y-axis points

plt.plot(xpoints, ypoints, marker='o', label="Circle")  # Plotting with circle markers
plt.plot(xpoints, ypoints, marker='s', label="Square")  # Plotting with square markers
plt.plot(xpoints, ypoints, marker='^', label="Triangle")  # Plotting with triangle markers
plt.plot(xpoints, ypoints, marker='*', label="Start")  # Plotting with star markers

plt.xlabel("X Points")  # Labeling the X-axis
plt.ylabel("Y Points")  # Labeling the Y-axis
plt.title("Basic Marker Types")  # Setting the plot title
plt.legend()  # Displaying the legend

plt.show()  # Rendering the plot
