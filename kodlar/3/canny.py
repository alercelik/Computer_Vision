import cv2
import numpy as np
import imutils


image = cv2.imread("../images/example_02.png")
image = imutils.resize(image, width=800)  # resizing with imutils is much easier than OpenCV

cv2.imshow("image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

canny_image = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny", canny_image)


cv2.waitKey()


# Now with a blur
blurred_gray = cv2.blur(gray, (7, 7))
cv2.imshow("blurred gray", blurred_gray)

blurred_canny_image = cv2.Canny(blurred_gray, 100, 200)
cv2.imshow("blurred Canny", blurred_canny_image)


cv2.waitKey()


# Now using median value as parameter
"""
https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
"""
median_canny = imutils.auto_canny(blurred_gray)
cv2.imshow("median Canny", median_canny)


cv2.waitKey()
cv2.destroyAllWindows()
