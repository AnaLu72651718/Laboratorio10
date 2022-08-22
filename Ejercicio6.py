import cv2
import numpy as np

image = cv2.imread('matias.png')
kernel = np.ones((5, 5), np.uint8)

open = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original', image)
cv2.imshow('Apertura', open)
cv2.waitKey()
cv2.destroyAllWindows()

