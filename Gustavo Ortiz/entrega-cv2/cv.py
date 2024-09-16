import numpy as np
import cv2

data = {'Quadrado_Vermelho': {'Geometria': 4, 'Cor': 54}, 'Retangulo_Preto': {'Geometria': 4, 'Cor': 0}, 'Triangulo_Azul': {'Geometria': 3, 'Cor': 164}}
imagem = cv2.imread('objects.png')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

for chave in data.keys():
    filtro = np.where(imagemCinza != data[chave]['Cor'], 255, imagemCinza)
    bordas = cv2.Canny(filtro, 100, 200)
    contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        epsilon = 0.01 * cv2.arcLength(contorno, True)
        aproximacao = cv2.approxPolyDP(contorno, epsilon, True)
        if cv2.isContourConvex(aproximacao) and len(aproximacao) == data[chave]['Geometria']:
            localizacao = aproximacao
    x, y, w, h = cv2.boundingRect(localizacao)
    figura = imagem[y:y+h, x:x+w]
    cv2.imwrite(f'{chave}.png', figura)