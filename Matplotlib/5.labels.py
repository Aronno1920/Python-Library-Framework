import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting

xpoints = [1, 2, 3, 4, 5]  # Defining X-axis points
ypoints = [10, 15, 25, 30, 20]  # Defining Y-axis points

plt.plot(xpoints, ypoints)  # Plotting the line chart

plt.xlabel("X Points")  # Labeling the X-axis
plt.ylabel("Y Points")  # Labeling the Y-axis
plt.title("Label Style")  # Setting the plot title

plt.legend(loc='upper left', fontsize=16, frameon=False)  # Adding a legend with styling (note: no label is assigned to the line)

plt.show()  # Displaying the plot
