import numpy as np  # Importing the NumPy library
import imageio.v2 as imaio  # Importing image reading module from imageio (v2 API)
import matplotlib.pyplot as plt  # Importing the plotting library

img = imaio.imread('color-image.jpg')  # Reading the image file into a NumPy array

# Converting the image to grayscale using weighted sum (commented out)
# gray_image = np.dot(img[..., :3], [0.2989, 1.5870, 0.1140])  
# plt.imshow(gray_image, cmap='gray')  # Displaying the grayscale image with gray color map
# plt.title('Grayscale Image')  # Adding title to the grayscale image
# plt.show()  # Showing the grayscale image plot

# Creating a negative image by subtracting pixel values from 255
nagative_image = 255 - img  
plt.imshow(nagative_image)  # Displaying the negative image
plt.title('Negetive Image')  # Adding title to the negative image
plt.show()  # Showing the negative image plot
