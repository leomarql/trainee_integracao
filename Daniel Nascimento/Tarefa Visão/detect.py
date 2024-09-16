import cv2
import numpy as np

img = cv2.imread('objects.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([169, 215, 227],np.uint8)
upper_red = np.array([189, 235, 247],np.uint8)
lower_black = np.array([0, 0, 0],np.uint8)
upper_black = np.array([10, 10, 10],np.uint8)
lower_blue = np.array([89, 245, 222],np.uint8)
upper_blue = np.array([109, 255, 242],np.uint8)

mask_red = cv2.inRange(hsv_img, lower_red, upper_red)

mask_black = cv2.inRange(hsv_img, lower_black, upper_black)

mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)

contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt_red in contours_red:
    approx = cv2.approxPolyDP(cnt_red, 0.04 * cv2.arcLength(cnt_red, True), True)
    if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if abs(w-h) < 1.5:
                quadrado_vermelho = img[y: y + h, x: x + w]
                quadrado_vermelho = cv2.resize(quadrado_vermelho, (100, 100),interpolation = cv2.INTER_AREA)
                cv2.imwrite('quadrado_vermelho.png', quadrado_vermelho)

for cnt_black in contours_black:
    approx = cv2.approxPolyDP(cnt_black, 0.04 * cv2.arcLength(cnt_black, True), True)
    if len(approx) == 4:        
            x, y, w, h = cv2.boundingRect(approx)
            retangulo_preto = img[y:y + h, x:x + w]
            retangulo_preto = cv2.resize(retangulo_preto, (100, 100), interpolation=cv2.INTER_AREA)
            cv2.imwrite('retangulo_preto.png', retangulo_preto)

for cnt_blue in contours_blue:
    approx = cv2.approxPolyDP(cnt_blue, 0.04 * cv2.arcLength(cnt_blue, True), True)
    if len(approx) == 3:
            x, y, w, h = cv2.boundingRect(approx)
            triangulo_azul = img[y:y + h, x:x + w]
            triangulo_azul = cv2.resize(triangulo_azul, (100, 100))
            cv2.imwrite('triangulo_azul.jpg', triangulo_azul)

print("Objetos encontrados e salvos com sucesso.")
