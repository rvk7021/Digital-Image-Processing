import cv2
import matplotlib.pyplot as plt
import numpy as np
import pywt

# Load image from earlier path
path = '/kaggle/input/dataset/immage1.jpeg'
img_bgr = cv2.imread(path)

if img_bgr is None:
    print(f"Error: Unable to read the image {path}.")
else:
    # Convert image to grayscale
    original = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Wavelet transform of the image
    titles = ['Approximation', 'Horizontal detail', 'Vertical detail', 'Diagonal detail']
    coeffs2 = pywt.dwt2(original, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    components = [LL, LH, HL, HH]

    # Save the original grayscale image
    plt.imsave('/kaggle/working/original_image.png', original, cmap='gray')

    # Create a figure to show the results with colored edges
    for i, (component, title) in enumerate(zip(components, titles)):
        # Create the plot for each component
        plt.figure(figsize=(3, 3))
        plt.imshow(component, cmap=plt.cm.gray)
        plt.title(title, fontsize=10)
        plt.xticks([])
        plt.yticks([])

        # Save each view separately
        save_path = f'/kaggle/working/{title.replace(" ", "_").lower()}.png'
        plt.savefig(save_path)
        plt.close()  # Close the figure after saving to prevent display

    print("Images saved successfully.")
