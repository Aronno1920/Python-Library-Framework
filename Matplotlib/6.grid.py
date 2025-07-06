import matplotlib.pyplot as plt  

xpoints = [1, 2, 3, 4, 5]
ypoints = [10, 15, 25, 30, 20]

# plt.plot(xpoints, ypoints)
# plt.grid(color='gray', linestyle='--', linewidth=0.4)
# plt.show()

# Create 1 row and 2 columns of subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # axs is an array of axes

# First subplot
axs[0].plot(xpoints, ypoints)
axs[0].grid(True)
axs[0].set_title("Original Y Points")

# Second subplot
axs[1].plot(xpoints, [i**2 for i in ypoints])
axs[1].grid(color='gray', linestyle='--', linewidth=0.4)
axs[1].set_title("Y Points Squared")

plt.tight_layout()  # optional: improves spacing
plt.show()