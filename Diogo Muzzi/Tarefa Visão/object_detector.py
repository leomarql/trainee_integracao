import cv2
import numpy as np

img = cv2.imread('objects.png', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Quadrado Vermelho
lower_red = np.array([170,220,230])
upper_red = np.array([179,230,255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)
img_red = cv2.bitwise_and(img, img, mask=mask_red)
ret,thresh_img = cv2.threshold(mask_red, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        object = img[y - 10:y + h + 10, x - 10:x + w + 10]
        resized_object = cv2.resize(object, (100, 100))
        cv2.imwrite('quadrado_vermelho.png', resized_object)

# Triângulo Azul
lower_blue = np.array([90,245,220])
upper_blue = np.array([110,255,245])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
img_blue = cv2.bitwise_and(img, img, mask=mask_blue)
ret,thresh_img = cv2.threshold(mask_blue, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 3:
        x, y, w, h = cv2.boundingRect(cnt)
        object = img[y - 10:y + h + 10, x - 10:x + w + 10]
        resized_object = cv2.resize(object, (100, 100))
        cv2.imwrite('triangulo_azul.png', resized_object)

# Retângulo Preto
lower_black = np.array([0,0,0])
upper_black = np.array([10,10,10])
mask_black = cv2.inRange(hsv, lower_black, upper_black)
img_black = cv2.bitwise_and(img, img, mask=mask_black)
ret,thresh_img = cv2.threshold(mask_black, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        object = img[y - 10:y + h + 10, x - 10:x + w + 10]
        resized_object = cv2.resize(object, (100, 100))
        cv2.imwrite('retangulo_preto.png', resized_object)