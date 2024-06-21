import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\EClub CV workshop\Images\Albert_einstein_by_zuzahin-d5pcbug.jpg")

plt.imshow(img[:,:,::-1]);plt.title("original image",img);plt.axis("off");

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap="gray");plt.title("original image");plt.axis("off");

gray_inv=cv2.bitwise_not(gray)
plt.imshow(gray_inv,cmap="gray");plt.title("original image");plt.axis("off");

contours, hierarchy= cv2.findContours(gray_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
img_copy=img.copy()

cv2.drawContours(img_copy,contours,-1(255,0,0),2)
plt.figure(figsize=[10,10])
plt.imshow(img_copy)

