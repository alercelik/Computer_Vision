import cv2
import numpy as np

image = cv2.imread("../images/renkler.png")

cv2.imshow("image", image)
cv2.waitKey()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_hsv = (23, 125, 175)
upper_hsv = (35, 255, 255)
filtered = cv2.inRange(hsv_image, (23, 125, 175), (35, 255, 255))

#filtered = cv2.inRange(image, (150, 0, 0), (255, 255, 255))

cv2.imshow("inRange", filtered)

cv2.waitKey()
