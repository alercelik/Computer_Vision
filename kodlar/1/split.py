import cv2
import numpy as np


image = cv2.imread("image.jpg")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))


# 1. yöntem
B, G, R = cv2.split(image)

cv2.namedWindow("B", cv2.WINDOW_FREERATIO)
cv2.imshow("B", B)

cv2.namedWindow("G", cv2.WINDOW_FREERATIO)
cv2.imshow("G", G)

cv2.namedWindow("R", cv2.WINDOW_FREERATIO)
cv2.imshow("R", R)

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()


# 2. yöntem

for channel in range(channels):
	image_to_display = image[:,:,channel]
	
	cv2.namedWindow("{}".format(channel), cv2.WINDOW_FREERATIO)
	cv2.imshow("{}".format(channel), image_to_display)

cv2.waitKey()
cv2.destroyAllWindows()
