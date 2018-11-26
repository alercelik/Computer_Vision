import cv2
import numpy as np

image = cv2.imread("../images/renkler.png")

cv2.imshow("image", image)
cv2.waitKey()


lower_bgr = (150, 0, 0)
upper_bgr = (255, 255, 255)
# -> all green and red values, but blue values that are higher than 150 

filtered = cv2.inRange(image, (150, 0, 0), (255, 255, 255))

cv2.imshow("inRange", filtered)

cv2.waitKey()
