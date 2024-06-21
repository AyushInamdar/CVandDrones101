import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2023-12-22 021706.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

# Define parameters for Harris corner detection
block_size = 2  # neighborhood size for corner detection
ksize = 3  # aperture parameter for the Sobel derivative
k = 0.04  # Harris detector free parameter, typically in the range [0.04, 0.06]

# Apply Harris corner detection
corners = cv2.cornerHarris(gray, block_size, ksize, k)

# Threshold for corner response
threshold = 0.01 * corners.max()

# Mark corners on the image
image[corners > threshold] = [0, 0, 255] if len(image.shape) == 3 else 255  
# Display the result
cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

