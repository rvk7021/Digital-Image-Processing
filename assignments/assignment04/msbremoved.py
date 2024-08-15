import cv2
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

# Correct file paths based on the directory contents
img1_path = '/kaggle/input/colorimage/immage1.jpeg'  # Corrected typo
img2_path = '/kaggle/input/colorimage/image2.jpeg'

# Function to remove most significant bits (MSBs)
def remove_msb(image, bits_to_remove=4):
    # Clear the most significant bits by masking them out
    mask = (1 << (8 - bits_to_remove)) - 1  # Create a mask for lower bits
    image_modified = np.bitwise_and(image, mask)  # Apply the mask to retain lower bits
    return image_modified

# OpenCV part with file check
img1_cv = cv2.imread(img1_path)
if img1_cv is None:
    print(f"Failed to load {img1_path}. Please check the file path.")
else:
    gray_img1_cv = cv2.cvtColor(img1_cv, cv2.COLOR_BGR2GRAY)
    
    # Remove MSBs from the grayscale image
    gray_img1_cv_msb_removed = remove_msb(gray_img1_cv)
    
    # Save and display the modified grayscale image
    cv2.imwrite('/kaggle/working/grayscale_image1_msb_removed_cv.jpg', gray_img1_cv_msb_removed)
    print("Grayscale Image 1 with MSB removed (OpenCV) saved successfully.")
    
    # Display the original and MSB-modified grayscale images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(gray_img1_cv, cmap='gray')
    plt.title("Original Grayscale Image 1 (OpenCV)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(gray_img1_cv_msb_removed, cmap='gray')
    plt.title("MSB Removed Grayscale Image 1 (OpenCV)")
    plt.axis('off')
    plt.show()

# Pillow part with file check
if os.path.exists(img2_path):
    img2_pil = Image.open(img2_path)
    gray_img2_pil = img2_pil.convert('L')

    # Convert Pillow image to numpy array for manipulation
    gray_img2_pil_np = np.array(gray_img2_pil)
    
    # Remove MSBs from the grayscale image
    gray_img2_pil_msb_removed = remove_msb(gray_img2_pil_np)
    
    # Save and display the modified grayscale image
    gray_img2_pil_msb_removed_img = Image.fromarray(gray_img2_pil_msb_removed)
    gray_img2_pil_msb_removed_img.save('/kaggle/working/grayscale_image2_msb_removed_pil.jpg')
    print("Grayscale Image 2 with MSB removed (Pillow) saved successfully.")
    
    # Display the original and MSB-modified grayscale images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(gray_img2_pil_np, cmap='gray')
    plt.title("Original Grayscale Image 2 (Pillow)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(gray_img2_pil_msb_removed, cmap='gray')
    plt.title("MSB Removed Grayscale Image 2 (Pillow)")
    plt.axis('off')
    plt.show()
else:
    print(f"Failed to load {img2_path}. Please check the file path.")
