import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [6,4,3,4,5]

# plt.scatter(x,y)
# plt.title('Scatter Plot')
# plt.show()

plt.scatter(x,y, color='red', marker='o', s=100, edgecolors='black')
plt.title('Customized Scatter Plot')
plt.show()