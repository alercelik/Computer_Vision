import cv2
import numpy as np

image = cv2.imread("birds2.jpg")

cv2.imshow("(window name) image", image)

for b in [111, 201, 301]:
	blurred_image = cv2.blur(image, (b,b))
	cv2.imshow("blurred_image using {}x{} kernel".format(b, b), blurred_image)
	cv2.waitKey()

