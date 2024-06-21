import cv2

s1=input("Enter the path of the first image")
s2=input("Enter the path of the second image")

img1 = cv2.imread(r's1')
img2 = cv2.imread(r's2')

img1 = cv2.resize(img1,(256,256,interpolation=cv2.INTER_CUBIC))
img2 = cv2.resize(img2,(256,256,interpolation=cv2.INTER_CUBIC))
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)