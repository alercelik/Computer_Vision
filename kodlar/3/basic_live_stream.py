import cv2
import imutils
import numpy as np

camera = cv2.VideoCapture(0)

while True:
	_, frame = camera.read()

	canny = imutils.auto_canny(frame)  # pip install imutils
	
	cv2.imshow("frame", frame)
	cv2.imshow("canny", canny)

	cv2.waitKey(5)
