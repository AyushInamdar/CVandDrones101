import cv2
import numpy as np

def increase_value_and_convert(image_path):
    # Load the BGR image
    bgr_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if bgr_image is None:
        print(f"Error: Unable to load image from {image_path}")
        return None

    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # Increase the value channel to 0.5 times its initial value
    value_multiplier = 0.5
    hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * value_multiplier, 0, 255)

    saturation_multiplier = 1.5
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_multiplier, 0, 255)

    # Convert HSV back to BGR
    final_bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return final_bgr_image

# Example usage:
input_image_path = r"C:\Users\Ayush's Galaxy Book\Downloads\landscape.jpg"
output_image = increase_value_and_convert(input_image_path)

# Display the original and filtered images (for testing purposes)
cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Modified Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()