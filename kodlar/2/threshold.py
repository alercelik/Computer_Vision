import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("gradient.jpg")  # birds.jpg

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)


for threshold_value in range(10, 255, 50):
	ret, thresholded_image = cv2.threshold(image, threshold_value, 255,cv2.THRESH_BINARY)

	window_name = "trehshold at {}".format(threshold_value)
	cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
	cv2.imshow(window_name, thresholded_image)
	cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()



"""
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()
"""
