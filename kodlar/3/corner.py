import cv2
import numpy as np
import imutils


filename = "../images/chessboard.jpg"
image = cv2.imread(filename)
image = imutils.resize(image, width=600)  # resizing with imutils is much easier than OpenCV

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
corner_image = cv2.cornerHarris(gray, 2, 3, 0.04)

print(corner_image)
"""
img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
"""

cv2.imshow("corner_image", corner_image)
cv2.waitKey()

# result is dilated for marking the corners, not important
kernel_5 = np.ones((5,5), np.uint8)
dilated_corner_image = cv2.dilate(corner_image, kernel_5)

cv2.imshow("dilated_corner_image", dilated_corner_image)
cv2.waitKey()

# Threshold for an optimal value, it may vary depending on the image.
image[dilated_corner_image > 0.01*dilated_corner_image.max()] = [0,0,255]  # draw corners on image

cv2.imshow('corner_image', image)


cv2.waitKey()
cv2.destroyAllWindows()
