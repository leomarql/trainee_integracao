import cv2
import numpy as np
img = cv2.imread('objects.png')
cv2.imshow('HSV image', img)

#Vermelho
red = np.uint8([[[36,28,237]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print( hsv_red )
#Azul
blue = np.uint8([[[232,162,0 ]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print( hsv_blue )
#Preto
hsv_black = np.uint8([[[0,0,0 ]]])
hsv_black = cv2.cvtColor(hsv_black,cv2.COLOR_BGR2HSV)
print( hsv_black )
