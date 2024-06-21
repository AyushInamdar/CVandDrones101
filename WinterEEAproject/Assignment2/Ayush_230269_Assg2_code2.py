import cv2
import numpy as np
 
img = np.ones((600, 600, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (0, 400), (600, 600), (0, 128, 0), thickness=cv2.FILLED)
cv2.rectangle(img, (0, 0), (600, 200), (0, 165, 255), thickness=cv2.FILLED)  

cv2.circle(img, (300, 300), 100, (128, 0, 0), thickness=2)  
for i in range(0, 360, 360 // 24):
    x1 = int(300)
    y1 = int(300)
    x2 = int(300 + 100 * np.cos(np.radians(i)))
    y2 = int(300 + 100 * np.sin(np.radians(i)))
    cv2.line(img, (x1, y1), (x2, y2), (128, 0, 0), thickness=1)    
cv2.imshow("Indian img", img)


image = img


def rotate(img,y):
    if y == 90:
        rotimg= cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif y == 180:
        rotimg = cv2.rotate(img,cv2.ROTATE_180)
    elif y == 270:
        rotimg = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    else:
        print("invalid input")

    return rotimg

#rotate(image,90)

def rotatedFlags():
    rotate(image,90)
    rotate(image,180)
    rotate(image,270)

rotatedFlags()

