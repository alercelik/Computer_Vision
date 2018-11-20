import cv2
import numpy as np

"""
https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/
"""
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


image = cv2.imread('example_01.png')
cv2.namedWindow("Original", cv2.WINDOW_FREERATIO)
cv2.imshow("Original", image)


for gamma in [0.5, 0.8, 1.2, 1.5, 2, 2.5]:
	gamma_adjusted = adjust_gamma(image, gamma=gamma)

	window_name = "gamma {}".format(gamma)
	cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
	cv2.imshow(window_name, gamma_adjusted)
	cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
