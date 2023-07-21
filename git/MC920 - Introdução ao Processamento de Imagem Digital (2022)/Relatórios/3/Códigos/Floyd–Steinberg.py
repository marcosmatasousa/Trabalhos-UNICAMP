import numpy as np
import cv2

''' Os princípios do algoritmo do método de floyd
são válidos para os outros algoritmos de dithering
com a única diferença da máscara utilizada no processo.'''

def floyd(img, nc):
    arr = np.array(img, dtype=float) / 255

    # iterando sobre as coordenadas (i, j) da imagem:

    for i in range(len(arr)):
        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1] # Inversão das linhas ímpares, para varredura alternada
            arr[i] = aux
        for j in range(len(arr[i])):
            # calculando o erro
            antigo = arr[i][j].copy()
            novo = np.round(antigo * (nc - 1)) / (nc - 1)
            arr[i][j] = novo
            erro = antigo - novo

            # Aplicação da máscara
            if j + 1 <= len(arr[i]) - 1:
                arr[i, j+1] += erro * (7/16)
            if (i+1) <= len(arr) - 1 and (j-1) >= 0:
                arr[i+1,j-1] += erro * (3/16)
            if (i+1) <= len(arr) - 1 and j+1 <= len(arr[i]) - 1:
                arr[i+1,j+1] += erro / 16
            if (i+1) <= len(arr) - 1:
                arr[i+1,j] += erro * (5/16)
        
        #Reinversão da linha, caso esta seja ímpar
        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux

    res = np.array(arr * 255, dtype=np.uint8)
    return res

# RGB
monalisa = cv2.imread("monalisa.png")
monalisa = floyd(monalisa, 3)
cv2.imwrite("monalisaFloyd.png", monalisa)

baboon = cv2.imread("baboon.png")
baboon = floyd(baboon, 2)
cv2.imwrite("baboonFloyd.png", baboon)

peppers = cv2.imread("peppers.png")
peppers = floyd(peppers, 2)
cv2.imwrite("peppersFloyd.png", peppers)

# Monocromático
baboon = cv2.imread("baboon.png", 0)
baboon = floyd(baboon, 2)
cv2.imwrite("baboonFloydBlack.png", baboon)

monalisa = cv2.imread("monalisa.png", 0)
monalisa = floyd(monalisa, 3)
cv2.imwrite("monalisaFloydBlack.png", monalisa)

peppers = cv2.imread("peppers.png", 0)
peppers = floyd(peppers, 2)
cv2.imwrite("peppersFloydBlack.png", peppers)

