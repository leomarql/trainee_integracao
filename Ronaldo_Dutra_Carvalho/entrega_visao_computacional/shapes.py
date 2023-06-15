import cv2
import numpy as np

img = cv2.imread("objects.png")


vermelho_min = np.array([0, 0, 200], np.uint8)
vermelho_max = np.array([100, 100, 255], np.uint8)  

preto_min = np.array([0, 0, 0], np.uint8)
preto_max = np.array([30,30, 30], np.uint8) 

azul_min = np.array([50, 0, 0], np.uint8)
azul_max = np.array([255, 170,170], np.uint8)

mascara_azul = cv2.inRange(img, azul_min, azul_max)
mascara_vermelho = cv2.inRange(img, vermelho_min, vermelho_max)
mascara_preto = cv2.inRange(img, preto_min, preto_max)

def desenha_contorno_triangulo(mascara,img):
    ret,thresh = cv2.threshold(mascara,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours detected:",len(contours))
    for cnt in contours:
    
        perimetro = cv2.arcLength(cnt, True)
        aproximacao = cv2.approxPolyDP(cnt, 0.04 * perimetro, True)
        if len(aproximacao) == 3:
            x, y, largura, altura = cv2.boundingRect(aproximacao)
            regiao_recortada = img[y:y+altura, x:x+largura]
            cv2.imwrite(f'regiao_triangulo.png', regiao_recortada)



def desenha_contorno_quadrado(mascara,img):
    ret,thresh = cv2.threshold(mascara,150,255,0)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours detected:",len(contours))

    for cnt in contours:
        perimetro = cv2.arcLength(cnt, True)
        aproximacao = cv2.approxPolyDP(cnt, 0.04 * perimetro, True)
    if len(aproximacao) == 4:
            x, y, largura, altura = cv2.boundingRect(aproximacao)
            regiao_recortada = img[y:y+altura, x:x+largura]
            cv2.imwrite(f'regiao_quadrado.png', regiao_recortada)

def desenha_contorno_retangulo(mascara,img):
    ret,thresh = cv2.threshold(mascara,150,255,0)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours detected:",len(contours))

    for cnt in contours:
        perimetro = cv2.arcLength(cnt, True)
        aproximacao = cv2.approxPolyDP(cnt, 0.04 * perimetro, True)
    if len(aproximacao) == 4:
            x, y, largura, altura = cv2.boundingRect(aproximacao)
            regiao_recortada = img[y:y+altura, x:x+largura]
            cv2.imwrite(f'regiao_retangulo.png', regiao_recortada)
            


desenha_contorno_quadrado(mascara_vermelho,img)
desenha_contorno_triangulo(mascara_azul,img)
desenha_contorno_retangulo(mascara_preto,img)


        
        





cv2.imshow('contornos',img)






cv2.waitKey(0)

cv2.destroyAllWindows()