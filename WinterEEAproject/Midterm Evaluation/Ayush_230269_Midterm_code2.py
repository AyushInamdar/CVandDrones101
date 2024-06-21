import cv2
import numpy as np

def hough_line(s):
    img = cv2.imread(s)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 140, minLineLength=20, maxLineGap=10)

    # Drawing detected lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  

    return img


image_path = r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2023-12-20 192847.png"
output_img = hough_line(image_path)
cv2.imshow("Image with Detected Lines", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
