import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,15,25,30,40]
# plt.plot(x, y, label='Data Line')

x = [1,2,3,4,5]
y = [10,15,25,30,40]
y2= [30,30,20,50,5]
plt.plot(x, y, linestyle="--", color="green", label="Dashed Green Line")
plt.plot(x, y2, color="blue", label="Dashed Blue Line (Multiple)")

plt.xlabel("X Points")  # Labeling the X-axis
plt.ylabel("Y Points")  # Labeling the Y-axis
plt.title("Line Style")  # Setting the plot title
plt.legend()  # Displaying the legend

plt.show()  # Rendering the plot
