import cv2
import numpy as np

img = cv2.imread('objects.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#CÓDIGO DISPONIBILIZADO NAS REFERÊNCIAS DO DESAFIO - USEI COMO BASE

#-----------------------------------------------------------------------
#ret,thresh = cv2.threshold(img1,150,255,0)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
#print("Number of contours detected:",len(contours))
#
#for cnt in contours:
#   approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, True), True)
#   if len(approx) == 3:
#      img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
#      M = cv2.moments(cnt)
#      if M['m00'] != 0.0:
#         x = int(M['m10']/M['m00'])
#         y = int(M['m01']/M['m00'])
#      cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#
##cv2.imshow("Triangles", img)
##cv2.waitKey(0)
#cv2.destroyAllWindows()

#import cv2
#import numpy as np
#
## Carrega a imagem
#imagem = cv2.imread('caminho/para/imagem.jpg')

# Converte a imagem para o espaço de cores HSV
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define os limites inferior e superior para a cor desejada (azul, por exemplo)
# Os valores estão no formato HSV
#-------------------------------------------------------------------------

#ENCONTRANDO O TRIANGULO AZUL

limite_inferior_azul = np.array([60, 60, 200],dtype=np.uint8)
limite_superior_azul = np.array([130, 255, 255],dtype=np.uint8)


mascara_azul = cv2.inRange(img1, limite_inferior_azul, limite_superior_azul)
mascara_azul = cv2.morphologyEx(mascara_azul, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))


contornos_azuis, _ = cv2.findContours(mascara_azul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos_azuis:
   
    approx = cv2.approxPolyDP(contorno, 0.1 * cv2.arcLength(contorno, True), True)
    
    
    if len(approx) == 3:
        x, y, w, h = cv2.boundingRect(contorno)

        regiao_recortada = img[y:y+h, x:x+w]
        regiao_100_100 = cv2.resize(regiao_recortada, (100, 100))

        nova_imagem = np.zeros((100, 100, 3), dtype=np.uint8)

        nova_imagem[0:100, 0:100] = regiao_100_100
        
        cv2.imwrite('contorno_triangulo.png', nova_imagem)
        break  


cv2.drawContours(img, contornos_azuis, -1, (0, 255, 0), 2)
print(f"Número de contornos azuis detectados: {len(contornos_azuis)}")

#ENCONTRANDO O RETANGULO PRETO

limite_inferior_preto = np.array([0, 0, 0],dtype=np.uint8)
limite_superior_preto = np.array([60, 60, 60],dtype=np.uint8)


mascara_preto = cv2.inRange(img1, limite_inferior_preto, limite_superior_preto)
mascara_preto = cv2.morphologyEx(mascara_preto, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))


contornos_pretos, _ = cv2.findContours(mascara_preto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos_pretos:
   
    approx = cv2.approxPolyDP(contorno, 0.1 * cv2.arcLength(contorno, True), True)
    
    
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contorno)

        #novo_h = h*100/w
        regiao_recortada = img[y:y+h, x:x+w]
        #regiao_100_100 = cv2.resize(regiao_recortada, (100, 100))
#
        #nova_imagem = np.zeros((100, 100, 3), dtype=np.uint8)
#
        #nova_imagem[0:100, 0:100] = regiao_100_100

        cv2.imwrite('contorno_retangulo.png', regiao_recortada)
        break  


cv2.drawContours(img, contornos_pretos, -1, (0, 255, 0), 2)
print(f"Número de contornos pretos detectados: {len(contornos_pretos)}")

#ENCONTRANDO O quadrado vermelho

limite_inferior_vermelho = np.array([100, 50, 50],dtype=np.uint8)
limite_superior_vermelho = np.array([255, 250, 250],dtype=np.uint8)


mascara_vermelho = cv2.inRange(img1, limite_inferior_vermelho, limite_superior_vermelho)
mascara_vermelho = cv2.morphologyEx(mascara_vermelho, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))


contornos_vermelhos, _ = cv2.findContours(mascara_vermelho, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#nw = None 

for contorno in contornos_vermelhos:
   
   approx = cv2.approxPolyDP(contorno, 0.1 * cv2.arcLength(contorno, True), True)
   
   
   if len(approx) == 4:
      x, y, w, h = cv2.boundingRect(contorno)
      
      if h - 2 <= w <= h + 2: 
        
        regiao_recortada = img[y:y+h, x:x+w]
        regiao_100_100 = cv2.resize(regiao_recortada, (100, 100))

        nova_imagem = np.zeros((100, 100, 3), dtype=np.uint8)

        nova_imagem[0:100, 0:100] = regiao_100_100
        
        cv2.imwrite('contorno_quadrado.png', nova_imagem)
        break
         
#regiao_recortada = img[ny:ny+nh, nx:nx+nw]
#nova_imagem = np.zeros((nh, nw, 3), dtype=np.uint8)
#nova_imagem[0:nh, 0:nw] = regiao_recortada
#cv2.imwrite('contorno_quadrado.png', nova_imagem)
 


cv2.drawContours(img, contornos_vermelhos, -1, (0, 255, 0), 2)
print(f"Número de contornos vermelhos detectados: {len(contornos_vermelhos)}")


# Exibe a imagem resultante
cv2.imshow('Contornos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
