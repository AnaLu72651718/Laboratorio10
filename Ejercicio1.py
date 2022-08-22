import cv2

img = cv2.imread('matias.png', 0)

ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Umbral Binario', thresh1)
cv2.waitKey()
cv2.destroyAllWindows()