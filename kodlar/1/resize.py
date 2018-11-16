import cv2
import numpy as np


image = cv2.imread("image2.jpg")

height, width, channels = image.shape

print("image consists of {} rows, {} columns and {} channels".format(height, width, channels))

resized_image = cv2.resize(image, (2*width, 2*height))
#resized_image = cv2.resize(image, fx=2, fy=2)  #farklı gösterimi
# res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC) 

#cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)
cv2.imshow("resized_image", resized_image)
cv2.waitKey()
cv2.destroyAllWindows()
