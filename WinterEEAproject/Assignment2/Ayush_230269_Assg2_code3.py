import cv2
import numpy as np

def generate():
    flag = np.ones((600, 600, 3), dtype=np.uint8) * 255

    cv2.rectangle(flag, (0, 400), (600, 600), (0, 128, 0), thickness=cv2.FILLED)
    cv2.rectangle(flag, (0, 0), (600, 200), (0, 165, 255), thickness=cv2.FILLED)  

    cv2.circle(flag, (300, 300), 100, (128, 0, 0), thickness=2)  

    for i in range(0, 360, 360 // 24):
        x1 = int(300 )
        y1 = int(300 )
        x2 = int(300 + 100 * np.cos(np.radians(i)))
        y2 = int(300 + 100 * np.sin(np.radians(i)))

        cv2.line(flag, (x1, y1), (x2, y2), (128, 0, 0), thickness=1)    
    cv2.imshow("Indian Flag", flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return flag

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

colours = []

skew = cv2.imread(r"C:\WinterEEAproject\Assignment2\test1.jpeg")
height = skew.shape[0]
for i in range (height):
    color = skew[i][300]
    colours.append(color)

colours 

##we check the horizontal and vertical middle lines for the colours present and the order they are present in, and then determine
# which orientation of the flag is present
# i was out of station for the past 4-5 days and hence could not submit the assignment, but i have been keeping up with the project