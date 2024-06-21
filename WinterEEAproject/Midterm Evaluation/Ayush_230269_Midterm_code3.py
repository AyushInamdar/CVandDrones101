import cv2
import numpy as np

def colour(s, target_color=(0, 0, 255)):  

    img = cv2.imread(s)

    # Convert the image to HSV color space for more robust color detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_color = np.array([target_color[0] - 10, 50, 50])
    upper_color = np.array([target_color[0] + 10, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)               #mask for the required colour

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)            # Find contours in the mask

    # Draw contours on the original image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)  

    return img

image_path = r"C:\Users\Ayush's Galaxy Book\Downloads\cd8bc81847e77dd8756693d9702159a9.jpg"
result_img = colour(image_path, target_color=(0, 0, 255))

cv2.imshow("Contoured Image", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()