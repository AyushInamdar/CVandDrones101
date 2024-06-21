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
generate()

