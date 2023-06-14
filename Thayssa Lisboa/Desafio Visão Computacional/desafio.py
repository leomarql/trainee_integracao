import cv2
import numpy as np
import os.path

class Detect_Shapes:
    def Recorta(objects, hsv):
        # define os limites de cores na escala hsv
        # para definir as cores na escala hsv foi usado o link número 4 nas referências
        red = np.array([179, 225, 237])
        blue = np.array([99, 255, 232])
        black = np.array([0, 0, 0])

        # criar as mascaras para facilitar a detecção
        red_m = cv2.inRange(hsv, red, red)
        blue_m = cv2.inRange(hsv, blue, blue)
        black_m = cv2.inRange(hsv, black, black)

        # contornos de cada cor
        red_c, _ = cv2.findContours(red_m, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        blue_c, _ = cv2.findContours(blue_m, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        black_c, _ = cv2.findContours(black_m, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # percorrer os contornos de cada cor de interesse
        for rc in red_c:
            approx = cv2.approxPolyDP(rc, 0.01 * cv2.arcLength(rc, True), True)
            t = len(approx)
            if t == 4:
                x, y, w, h = cv2.boundingRect(rc)
                red_s = objects[y:y+h, x:x+w] # recorta com os contornos desejados
                dim = (100, 100) # dimensões desejadas 
                red_s = cv2.resize(red_s, dim, interpolation = cv2.INTER_AREA) # resize
                cv2.imwrite('imagens/red_s.png', red_s) # salvar

        for bc in blue_c:
            approx = cv2.approxPolyDP(bc, 0.01 * cv2.arcLength(bc, True), True)
            t = len(approx)
            if t == 3:
                x, y, w, h = cv2.boundingRect(bc)
                blue_t = objects[y:y+h, x:x+w] 
                dim = (100, 100)  
                blue_t = cv2.resize(blue_t, dim) 
                cv2.imwrite('imagens/blue_t.png', blue_t)

        for bcc in black_c:
            approx = cv2.approxPolyDP(bcc, 0.01 * cv2.arcLength(bcc, True), True)
            t = len(approx)
            if t == 4:
                x, y, w, h = cv2.boundingRect(bcc)
                black_r = objects[y:y+h, x:x+w] 
                dim = (100, 100) 
                black_r = cv2.resize(black_r, dim, interpolation = cv2.INTER_AREA) 
                cv2.imwrite('imagens/black_r.png', black_r)
        if os.path.isfile('imagens/red_s.png') and os.path.isfile('imagens/black_r.png') and os.path.isfile('imagens/blue_t.png'):
            mensagem = 'todos os objetos foram encontrados, recortados e salvos'

        return mensagem

    objects = cv2.imread('objects.png')
    hsv = cv2.cvtColor(objects, cv2.COLOR_BGR2HSV) # converter imagem pra escala hsv    

    print(Recorta(objects, hsv))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
referências:
1 - contornos: https://www.tutorialspoint.com/how-to-detect-a-rectangle-and-square-in-an-image-using-opencv-python
2 - mascaras: https://stackoverflow.com/questions/44073156/detecting-red-and-blue-squares-beanbags-using-python-and-cv2
hsv: 
3 - https://visioncompy.com/segmentacao-usando-espaco-de-cor/
4 - https://offsouza.medium.com/segmentando-objetos-pela-cor-opencv-487d5181b473
5 - resize: https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
6 - recorte: https://dandelion-cent-479.notion.site/Introdu-o-ao-OpenCV-0b6322ee103f40108298a42cf11c9401 
7 - salvar imagem: https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/
8 - checar se as imagens foram salvas: https://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python
'''
