import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

path = '/kaggle/input/dataset/immage1.jpeg'

if not os.path.exists(path):
    print(f"Error: The file {path} does not exist.")
else:
    img_bgr = cv2.imread(path, 1)

    if img_bgr is None:
        print(f"Error: Unable to read the image {path}. It may be corrupted or the path is incorrect.")
    else:
        height, width, _ = img_bgr.shape
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        img_lbp = np.zeros((height, width), np.uint8)

        def get_pixel(img, center, x, y):
            new_value = 0
            try:
                if img[x][y] >= center:
                    new_value = 1
            except IndexError:
                pass
            return new_value

        def lbp_calculated_pixel(img, x, y):
            center = img[x][y]
            val_ar = [
                get_pixel(img, center, x - 1, y - 1),
                get_pixel(img, center, x - 1, y),
                get_pixel(img, center, x - 1, y + 1),
                get_pixel(img, center, x, y + 1),
                get_pixel(img, center, x + 1, y + 1),
                get_pixel(img, center, x + 1, y),
                get_pixel(img, center, x + 1, y - 1),
                get_pixel(img, center, x, y - 1),
            ]
            power_val = [1, 2, 4, 8, 16, 32, 64, 128]
            val = sum(val_ar[i] * power_val[i] for i in range(len(val_ar)))
            return val

        for i in range(height):
            for j in range(width):
                img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)

        plt.imsave('original_image_output.png', cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
        plt.imsave('lbp_image_output.png', img_lbp, cmap='gray')

        print("LBP Program is finished. Images saved as 'original_image_output.png' and 'lbp_image_output.png'.")
