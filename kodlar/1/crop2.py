import cv2
import numpy as np


image = cv2.imread("image.jpg")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))

height_begin = 2000
height_end   = 3000

column_begin = 3000
column_end   = 4000


cropped_image = image[height_begin: height_end+1, column_begin: column_end+1]

cropped_image *= 0

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

cv2.namedWindow("cropped_image", cv2.WINDOW_FREERATIO)
cv2.imshow("cropped_image", cropped_image)

cv2.waitKey()


image_2 = cv2.imread("image.jpg")

cropped_image_2 = image_2[height_begin: height_end+1, column_begin: column_end+1].copy()

cropped_image_2 *= 0


cv2.namedWindow("image_2", cv2.WINDOW_FREERATIO)
cv2.imshow("image_2", image_2)

cv2.namedWindow("cropped_image_2", cv2.WINDOW_FREERATIO)
cv2.imshow("cropped_image_2", cropped_image_2)

cv2.waitKey()
cv2.destroyAllWindows()
