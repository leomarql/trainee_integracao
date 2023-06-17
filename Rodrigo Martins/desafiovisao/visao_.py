import cv2
import numpy as np

img = cv2.imread('imagem.png', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_P = np.array([0, 0, 0])
upper_P = np.array([10, 10, 10])
mask_P = cv2.inRange(hsv, lower_P, upper_P)
contours_P, _ = cv2.findContours(mask_P, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
retangulo_P = cv2.bitwise_and(img, img, mask=mask_P)

lower_V = np.array([170, 220, 230])
upper_V = np.array([179, 230, 255])
mask_V = cv2.inRange(hsv, lower_V, upper_V)
contours_V, _ = cv2.findContours(mask_V, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
quadrado_V = cv2.bitwise_and(img, img, mask=mask_V)

lower_A = np.array([89, 245, 222])
upper_A = np.array([109, 255, 242])
mask_A = cv2.inRange(hsv, lower_A, upper_A)
contours_A, _ = cv2.findContours(mask_A, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
triangulo_A = cv2.bitwise_and(img, img, mask=mask_A)

if len(contours_P) > 0:
    for contour_P in contours_P:
        approx = cv2.approxPolyDP(contour_P, 0.04 * cv2.arcLength(contour_P, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cv2.putText(img, "retangulo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            cv2.imwrite('retangulo_P.png', retangulo_P)
            cv2.imshow('retangulo_P', retangulo_P)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

if len(contours_V) > 0:
    for contour_V in contours_V:
        approx = cv2.approxPolyDP(contour_V, 0.04 * cv2.arcLength(contour_V, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            print(aspectRatio)
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                cv2.putText(img, "quadrado_V", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                cv2.imwrite('quadrado_V.png', quadrado_V)
                cv2.imshow('quadrado_V', quadrado_V)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()

if len(contours_A) > 0:
    for contour_A in contours_A:
        approx = cv2.approxPolyDP(contour_A, 0.04 * cv2.arcLength(contour_A, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        if len(approx) == 3:
            cv2.putText(img, "triangulo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            cv2.imwrite('triangulo_A.png', triangulo_A)
            cv2.imshow('triangulo_A', triangulo_A)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
