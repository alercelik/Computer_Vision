import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("birds.jpg")

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("gray", cv2.WINDOW_FREERATIO)
cv2.imshow("gray", gray)

cv2.waitKey()


ret, thresholded_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.namedWindow("thresholded_image", cv2.WINDOW_FREERATIO)
cv2.imshow("thresholded_image", thresholded_image)

cv2.waitKey()


not_image = cv2.bitwise_not(thresholded_image)

cv2.namedWindow("not_image", cv2.WINDOW_FREERATIO)
cv2.imshow("not_image", not_image)

cv2.waitKey()


background_image = cv2.bitwise_and(image, image, mask=not_image)
foreground_image = cv2.bitwise_and(image, image, mask=thresholded_image)

cv2.namedWindow("background_image", cv2.WINDOW_FREERATIO)
cv2.imshow("background_image", background_image)
cv2.namedWindow("foreground_image", cv2.WINDOW_FREERATIO)
cv2.imshow("foreground_image", foreground_image)
cv2.waitKey()


"""
for threshold_value in range(10, 255, 50):
	ret, thresholded_image = cv2.threshold(image, threshold_value, 255,cv2.THRESH_BINARY)

	window_name = "trehshold at {}".format(threshold_value)
	cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
	cv2.imshow(window_name, thresholded_image)
	cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
"""
