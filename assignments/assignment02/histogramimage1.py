import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load the image from the dataset folder
img = cv.imread('image1.png', cv.IMREAD_GRAYSCALE)

# Check if the image is loaded
if img is None:
    raise ValueError("Image not found or path is incorrect")

# Compute histogram and CDF for the original image
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

# Apply histogram equalization
img_equalized = cv.equalizeHist(img)

# Compute histogram and CDF for the equalized image
hist_eq, bins_eq = np.histogram(img_equalized.flatten(), 256, [0, 256])
cdf_eq = hist_eq.cumsum()
cdf_normalized_eq = cdf_eq * float(hist_eq.max()) / cdf_eq.max()

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Display the original grayscale image
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Grayscale Image')
axes[0, 0].axis('off')

# Plot CDF and histogram for the original image
axes[0, 1].plot(cdf_normalized, color='b')
axes[0, 1].hist(img.flatten(), 256, [0, 256], color='r')
axes[0, 1].set_xlim([0, 256])
axes[0, 1].set_title('Histogram and CDF (Original)')
axes[0, 1].legend(('CDF', 'Histogram'), loc='upper left')

# Display the equalized image
axes[1, 0].imshow(img_equalized, cmap='gray')
axes[1, 0].set_title('Histogram Equalized Image')
axes[1, 0].axis('off')

# Plot CDF and histogram for the equalized image
axes[1, 1].plot(cdf_normalized_eq, color='b')
axes[1, 1].hist(img_equalized.flatten(), 256, [0, 256], color='r')
axes[1, 1].set_xlim([0, 256])
axes[1, 1].set_title('Histogram and CDF (Equalized)')
axes[1, 1].legend(('CDF', 'Histogram'), loc='upper left')

# Show the plots
plt.show()

# Save the figure as an image
fig.savefig('image_with_histogram_and_equalization.png')

print("Image with histogram and CDF saved as 'image_with_histogram_and_equalization.png'.")
