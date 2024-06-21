import cv2 
import numpy as np

img = cv2.imread(r"C:\EClub CV workshop\Images\Albert_einstein_by_zuzahin-d5pcbug.jpg") 
img = img.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (256, 256),) 
				#interpolation=cv2.INTER_CUBIC) 

# subtract the original image with the blurred image 
# after subtracting add 127 to the total result 
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127

# display both original image and filtered image 
cv2.imshow("Original", img) 
cv2.imshow("High Passed Filter", hpf) 

# cv2.waitkey is used to display 
# the image continuously 
# if you provide 1000 instead of 0 then 
# image will close in 1sec 
# you pass in milli second 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
