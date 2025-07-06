import matplotlib.pyplot as plt

# Create 2 rows and 2 columns of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 5))  # axs is a 2x2 array

# Plot 1 (Top-left)
axs[0, 0].plot([10, 20, 30], [14, 25, 16])
axs[0, 0].set_title('Plot 1: Axis[0, 0]')

# Plot 2 (Top-right)
axs[0, 1].plot([23, 22, 21], [62, 55, 94])
axs[0, 1].set_title('Plot 2: Axis[0, 1]')

# Plot 3 (Bottom-left)
axs[1, 0].plot([91, 42, 23], [43, 25, 96])
axs[1, 0].set_title('Red Plot: Axis[1, 0]', color='red')

# Plot 4 (Bottom-right)
axs[1, 1].plot([3, 2, 1], [60, 15, 74], color='purple')
axs[1, 1].set_title('Purple Plot: Axis[1, 1]')

plt.tight_layout()
plt.show()
