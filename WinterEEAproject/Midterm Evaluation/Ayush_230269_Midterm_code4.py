import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ayush's Galaxy Book\Downloads\types-of-polygons1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==4:
        x,y,w,h = cv2.boundingRect(approx)
        aspect_ratio=float(w)/h
        print(aspect_ratio)
        if 0.95<aspect_ratio and aspect_ratio <1.05:
            cv2.putText(img, "square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img, "rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==5:
        cv2.putText(img, "pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==6:
        cv2.putText(img, "hexagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==7:
        cv2.putText(img, "heptagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==8:
        cv2.putText(img, "octagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx)==9:
        cv2.putText(img, "nonagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, "circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()