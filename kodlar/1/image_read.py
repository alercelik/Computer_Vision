import cv2
import numpy as np


image = cv2.imread("image.jpg")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
