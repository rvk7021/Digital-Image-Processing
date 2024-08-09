import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image
image_path = 'writemate.png'
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Image not found or path is incorrect")

# Split the image into RGB channels
b, g, r = cv2.split(image)

# Create an image with only the red channel
red_image = np.zeros_like(image)
red_image[:, :, 2] = r

# Create an image with only the green channel
green_image = np.zeros_like(image)
green_image[:, :, 1] = g

# Create an image with only the blue channel
blue_image = np.zeros_like(image)
blue_image[:, :, 0] = b

# Prepare the plots
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))
axes[1].set_title('Red Channel')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))
axes[2].set_title('Green Channel')
axes[2].axis('off')

axes[3].imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))
axes[3].set_title('Blue Channel')
axes[3].axis('off')

# Show the images
plt.show()

# Get the directory of the input image
image_dir = os.path.dirname(image_path)

# Construct the output paths
red_image_path = os.path.join(image_dir, 'red_channel.jpg')
green_image_path = os.path.join(image_dir, 'green_channel.jpg')
blue_image_path = os.path.join(image_dir, 'blue_channel.jpg')

# Save the images
cv2.imwrite(red_image_path, red_image)
cv2.imwrite(green_image_path, green_image)
cv2.imwrite(blue_image_path, blue_image)

print("Images saved successfully.")
