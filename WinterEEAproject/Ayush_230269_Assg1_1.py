import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread((r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2023-12-20 192847.png"), cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX)

sobel_combined = np.uint8(sobel_combined)
cv2.imshow('Original Image',img)
cv2.imshow('Sobel Edge Detection',sobel_combined)
cv2.waitKey(0)


