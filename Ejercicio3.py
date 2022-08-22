import cv2
imagen1 = cv2.imread('Figura1.jpeg')
imagen2 = cv2.imread('Figura2.jpeg')
# Concatenando imágenes, 2 filas por 4 columnas
concat_h1 = cv2.hconcat([imagen1, imagen2, imagen1, imagen2])
concat_h2 = cv2.hconcat([imagen2, imagen1, imagen2, imagen1])
concat_v = cv2.vconcat([concat_h1, concat_h2])
cv2.imshow('Combinar Imagenes', concat_v)
cv2.waitKey(0)
cv2.destroyAllWindows()