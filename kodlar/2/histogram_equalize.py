import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('wiki.jpg') #, 0)  # 0 means load image as grayscale

# check if image is grayscale
if np.array_equal(image[:,:,0], image[:,:,1]) and np.array_equal(image[:,:,0], image[:,:,2]):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(image)

cv2.namedWindow("Original", cv2.WINDOW_FREERATIO)
cv2.imshow("Original", image)

cv2.namedWindow("equalized_image", cv2.WINDOW_FREERATIO)
cv2.imshow("equalized_image", equalized_image)

cv2.waitKey()

plt.hist(image.ravel(), 256, [0,256])
plt.hist(equalized_image.ravel(), 256, [0,256])
plt.show()


