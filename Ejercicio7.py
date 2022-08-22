import cv2

image = cv2.imread('matias.png')
scale = 1
delta = 0
ddepth = cv2.CV_16S

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv2.imshow('Horizontal Sobel Filter', grad)
cv2.waitKey()
cv2.destroyAllWindows()