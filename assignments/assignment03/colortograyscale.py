import cv2
from PIL import Image
import os
import matplotlib.pyplot as plt

img1_path = '/kaggle/input/colorimage/immage1.jpeg'  
img2_path = '/kaggle/input/colorimage/image2.jpeg'

# OpenCV part with file check
img1_cv = cv2.imread(img1_path)
if img1_cv is None:
    print(f"Failed to load {img1_path}. Please check the file path.")
else:
    gray_img1_cv = cv2.cvtColor(img1_cv, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('/kaggle/working/grayscale_image1_cv.jpg', gray_img1_cv)
    print("Grayscale Image 1 (OpenCV) saved successfully.")

    # Display the OpenCV grayscale image
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_img1_cv, cmap='gray')
    plt.title("Grayscale Image 1 (OpenCV)")
    plt.axis('off')
    plt.show()

# Pillow part with file check
if os.path.exists(img2_path):
    img2_pil = Image.open(img2_path)
    gray_img2_pil = img2_pil.convert('L')
    gray_img2_pil.save('/kaggle/working/grayscale_image2_pil.jpg')
    print("Grayscale Image 2 (Pillow) saved successfully.")

    # Display the Pillow grayscale image
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_img2_pil, cmap='gray')
    plt.title("Grayscale Image 2 (Pillow)")
    plt.axis('off')
    plt.show()
else:
    print(f"Failed to load {img2_path}. Please check the file path.")
