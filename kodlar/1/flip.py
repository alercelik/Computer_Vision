import cv2
import numpy as np


image = cv2.imread("image2.jpg")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))


flip_x = np.flip(image, axis=0)
flip_y = np.flip(image, axis=1)

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

cv2.namedWindow("flip_x", cv2.WINDOW_FREERATIO)
cv2.imshow("flip_x", flip_x)

cv2.namedWindow("flip_y", cv2.WINDOW_FREERATIO)
cv2.imshow("flip_y", flip_y)


cv2.waitKey()
cv2.destroyAllWindows()
