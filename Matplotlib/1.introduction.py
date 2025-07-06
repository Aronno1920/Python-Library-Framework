import matplotlib.pyplot as plt

valuex = [1, 2, 3, 4, 5]
valuey = [10, 15, 22, 26, 15]

# Basic Style
# plt.plot(valuex, valuey)
# plt.show()

# Custmize Style
# Plotting with custom style (markers, dashed line, green color, and label)
plt.plot(valuex, valuey, marker='o', linestyle='--', color='green', label='My values')

plt.xlabel('X Axis') # Adding label to the X-axis
plt.ylabel('Y Axis') # Adding label to the Y-axis
plt.title("My first Matplotlib") # Adding a title to the plot
plt.legend() # Displaying the legend

plt.show()

