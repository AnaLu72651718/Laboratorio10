import numpy as np
import cv2

#Leer una imagen
img = cv2.imread('matias.png')

#Cambiar el espacio de color en img2
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Muestro la imagen
cv2.imshow('Cambio de Formato HSV',img2)
cv2.waitKey()
cv2.destroyAllWindows()

