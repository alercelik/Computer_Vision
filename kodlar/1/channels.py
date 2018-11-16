import cv2
import numpy as np

image_names = ["image.jpg", "renkler.png"]

for image_name in image_names:
	image = cv2.imread(image_name)

	rows, columns, channels = image.shape

	print("image consists of {} rows, {} columns and {} channels".format(rows, columns, channels))

	# fotoğrafı renkli olarak göstermek için 3 channel kullanmak şart
	# o yüzden örnek olarak blue channel'ı mavi olarak görmek için red ve green channel'larını komple siyah yapıyorum.
	B, G, R = cv2.split(image)

	blue_image = np.zeros(image.shape, np.uint8)
	blue_image[:,:,0] = B.copy()

	green_image = np.zeros(image.shape, np.uint8)
	green_image[:,:,1] = G.copy()

	red_image = np.zeros(image.shape, np.uint8)
	red_image[:,:,2] = R.copy()


	cv2.namedWindow("blue_image", cv2.WINDOW_FREERATIO)
	cv2.imshow("blue_image", blue_image)

	cv2.namedWindow("green_image", cv2.WINDOW_FREERATIO)
	cv2.imshow("green_image", green_image)

	cv2.namedWindow("red_image", cv2.WINDOW_FREERATIO)
	cv2.imshow("red_image", red_image)

	cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
	cv2.imshow("image", image)

	cv2.waitKey()
	cv2.destroyAllWindows()

