import cv2
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

# Correct file paths based on the directory contents
img1_path = '/kaggle/input/colorimage/immage1.jpeg'  # Corrected typo
img2_path = '/kaggle/input/colorimage/image2.jpeg'

# Function to remove least significant bits (LSBs) from color images
def remove_lsb(image, bits_to_remove=4):
    # Bitwise operation to shift right and left, removing LSBs
    image_modified = np.right_shift(image, bits_to_remove)  # Shift right to remove bits
    image_modified = np.left_shift(image_modified, bits_to_remove)  # Shift left to reset the bits
    return image_modified

# OpenCV part with file check for color image
img1_cv = cv2.imread(img1_path)
if img1_cv is None:
    print(f"Failed to load {img1_path}. Please check the file path.")
else:
    # Remove LSBs from the color image
    img1_cv_lsb_removed = remove_lsb(img1_cv)
    
    # Save and display the modified color image
    cv2.imwrite('/kaggle/working/color_image1_lsb_removed_cv.jpg', img1_cv_lsb_removed)
    print("Color Image 1 with LSB removed (OpenCV) saved successfully.")
    
    # Display the original and LSB-modified color images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1_cv, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    plt.title("Original Color Image 1 (OpenCV)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img1_cv_lsb_removed, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    plt.title("LSB Removed Color Image 1 (OpenCV)")
    plt.axis('off')
    plt.show()

# Pillow part with file check for color image
if os.path.exists(img2_path):
    img2_pil = Image.open(img2_path)

    # Convert Pillow image to numpy array for manipulation
    img2_pil_np = np.array(img2_pil)
    
    # Remove LSBs from the color image
    img2_pil_lsb_removed = remove_lsb(img2_pil_np)
    
    # Save and display the modified color image
    img2_pil_lsb_removed_img = Image.fromarray(img2_pil_lsb_removed)
    img2_pil_lsb_removed_img.save('/kaggle/working/color_image2_lsb_removed_pil.jpg')
    print("Color Image 2 with LSB removed (Pillow) saved successfully.")
    
    # Display the original and LSB-modified color images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img2_pil_np)
    plt.title("Original Color Image 2 (Pillow)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img2_pil_lsb_removed)
    plt.title("LSB Removed Color Image 2 (Pillow)")
    plt.axis('off')
    plt.show()
else:
    print(f"Failed to load {img2_path}. Please check the file path.")
