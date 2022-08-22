import cv2
def BrightnessContrast(brightness=0):
    brightness = cv2.getTrackbarPos('Brightness','GEEK')

    contrast = cv2.getTrackbarPos('Contrast',
                                  'GEEK')

    effect = controller(img, brightness,
                        contrast)

    cv2.imshow('Brillo', effect)


def controller(img, brightness=255,
               contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow

        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)

    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)

    cv2.putText(cal, 'B:{},C:{}'.format(brightness,
                                        contrast), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cal


if __name__ == '__main__':
    original = cv2.imread("matias.png")

    img = original.copy()

    cv2.namedWindow('GEEK')

    cv2.imshow('Original', original)

    cv2.createTrackbar('Brightness',
                       'GEEK', 255, 2 * 255,
                       BrightnessContrast)

    cv2.createTrackbar('Contrast', 'GEEK',
                       127, 2 * 127,
                       BrightnessContrast)

    BrightnessContrast(0)

cv2.waitKey(0)