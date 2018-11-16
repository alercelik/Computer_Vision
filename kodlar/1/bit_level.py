import cv2
import numpy as np

# image_size = (512, 1024)
image_height = 512
image_width = 1024

for bit in [1, 2, 4, 8]:
	levels = 2**bit

	space = np.linspace(0, levels - 1, levels, dtype="uint8")
	space_repeated = np.repeat(space, image_width//levels)
	space_tiled = np.tile(space_repeated, (image_height, 1))
	image = space_tiled

	multiplier = 255 // (levels-1)
	image = space_tiled * multiplier

	window_name = "{} bit -> {} levels".format(bit, levels)
	cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
	cv2.imshow(window_name, image)
	cv2.waitKey()

cv2.destroyAllWindows()
