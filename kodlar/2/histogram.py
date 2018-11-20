import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('itu.jpg')

# check if image is grayscale
if np.array_equal(image[:,:,0], image[:,:,1]) and np.array_equal(image[:,:,0], image[:,:,2]):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Original", cv2.WINDOW_FREERATIO)
cv2.imshow("Original", image)

if image.ndim == 2:  # 2D image
	plt.hist(image.ravel(), 256, [0,256])
	plt.show()

elif image.ndim == 3:  # 3D image
	color = ('b','g','r')
	for i, col in enumerate(color):
		hist = cv2.calcHist([image],[i],None,[256],[0,256])
		plt.plot(hist, color=col)
		plt.xlim([0,256])
	plt.show()
