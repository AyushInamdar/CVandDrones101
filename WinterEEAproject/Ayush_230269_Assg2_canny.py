import cv2
#image_path=r"C:\Users\Ayush's Galaxy Book\Downloads\9ba25796112cad616be27e473ae1e149.jpg"
def display_edges():
    # Perform Canny edge detection
    img = r"C:\Users\Ayush's Galaxy Book\Downloads\9ba25796112cad616be27e473ae1e149.jpg"
    edges = cv2.Canny(img,100,200)

    # Read the original image
    original_img = cv2.imread(r"C:\Users\Ayush's Galaxy Book\Downloads\9ba25796112cad616be27e473ae1e149.jpg")

    # Display the original image
    cv2.imshow('Original Image', original_img)
    cv2.waitKey(0)
    

    # Display the Canny edges
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
