import cv2

# Load the image
img = cv2.imread(r"C:\Users\Ayush's Galaxy Book\Pictures\Screenshots\Screenshot 2023-12-20 223810.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find corners using Shi-Tomasi method
corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.01, minDistance=10)

# Draw corners on the image
for corner in corners:
    x, y = corner.ravel()  # Ensure x and y are integers
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


# Display the image with detected corners
cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
