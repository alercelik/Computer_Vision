import cv2
import numpy as np


image = cv2.imread("renkler.png")

rows, columns, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))

# bu fonksiyon ile görüntü farklı renk uzaylarına da çevrilebilir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(gray.shape)

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

cv2.namedWindow("gray", cv2.WINDOW_FREERATIO)
cv2.imshow("gray", gray)

cv2.waitKey()
cv2.destroyAllWindows()
