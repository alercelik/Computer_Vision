import cv2
import numpy as np

random_image = np.random.randint(255, size=(512,512)).astype("uint8")

cv2.namedWindow("random_image", cv2.WINDOW_FREERATIO)
cv2.imshow("random_image", random_image)
cv2.waitKey()
cv2.destroyAllWindows()
