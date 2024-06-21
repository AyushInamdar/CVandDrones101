import cv2
import numpy as np

original_image = cv2.imread(r"C:\Users\Ayush's Galaxy Book\Downloads\landscape.jpg")


brightness_multiplier = 0.5
darkened_image = cv2.multiply(original_image, brightness_multiplier)

# Step 2: Increase contrast to 1.5 of its initial value
contrast_multiplier = 1.5
increased_contrast_image = cv2.multiply(darkened_image, contrast_multiplier)

    # Step 3: Increase saturation to 1.5 of its initial value
hsv_image = cv2.cvtColor(increased_contrast_image, cv2.COLOR_BGR2HSV)
saturation_multiplier = 1.5
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_multiplier, 0, 255)

    # Convert back to BGR
final_filtered_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow('initial',original_image)
cv2.imshow('final',final_filtered_image)
cv2.waitKey(0)