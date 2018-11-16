import cv2
import numpy as np

import imutils  # pip install imutils


image = cv2.imread("image.jpg")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))


# translation
M1 = np.float32([[1,0,1000],[0,1,500]])  # x ve y
translated = cv2.warpAffine(image, M1, (columns, rows))

cv2.namedWindow("translated", cv2.WINDOW_FREERATIO)
cv2.imshow("translated", translated)
cv2.waitKey()

# rotation
M2 = cv2.getRotationMatrix2D((columns/2, rows/2), -30, 1)  # center of rotation (x,y) ve açı
rotated = cv2.warpAffine(image, M2, (columns, rows))


cv2.namedWindow("rotated", cv2.WINDOW_FREERATIO)
cv2.imshow("rotated", rotated)
cv2.waitKey()


rotated2 = imutils.rotate_bound(image, 30)

cv2.namedWindow("rotated2", cv2.WINDOW_FREERATIO)
cv2.imshow("rotated2", rotated2)
cv2.waitKey()


cv2.destroyAllWindows()
