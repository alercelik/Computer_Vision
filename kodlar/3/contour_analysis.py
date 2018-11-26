import cv2
import numpy as np
import imutils


image = cv2.imread("../images/birds.jpg")
image = imutils.resize(image, width=800)  # resizing with imutils is much easier than OpenCV

cv2.imshow("image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

ret, thresholded_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
not_thresholded_image = cv2.bitwise_not(thresholded_image)

cv2.namedWindow("thresholded", cv2.WINDOW_FREERATIO)
cv2.imshow("thresholded", thresholded_image)

cv2.namedWindow("not_thresholded_image", cv2.WINDOW_FREERATIO)
cv2.imshow("not_thresholded_image", not_thresholded_image)

cv2.waitKey()

_im, contours, hierarchy = cv2.findContours(not_thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("There are {} contours".format(len(contours)))
for i, contour in enumerate(contours):
	print("{}, this contour has {} pixels\ncontour coordinates->{} \nArea of this contour is = {}".format(i, len(contour), contour, cv2.contourArea(contour)))
	#if cv2.contourArea(contour) < 1000:

for i, contour in enumerate(contours):
	cv2.drawContours(image,[contour], 0, (255,0,255), 3)
	cv2.imshow("hebele",image)
	cv2.waitKey(0)

"""
#above for loop is the same is below loop
for i in range(0, len(contours)):
	contour = contours[i]
	cv2.drawContours(image,[contour], 0, (255,0,255), 3)
	cv2.imshow("hebele",image)
	cv2.waitKey(0)
"""


cv2.waitKey()
cv2.destroyAllWindows()
