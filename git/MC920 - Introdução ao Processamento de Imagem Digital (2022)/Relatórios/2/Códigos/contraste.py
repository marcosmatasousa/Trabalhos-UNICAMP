import numpy as np
import matplotlib.pyplot as plt
import cv2

# padding
def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

def contraste(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            minimo = np.min(vizinhos)
            maximo = np.max(vizinhos)

            d_max = maximo - img[i][j]
            d_min = img[i][j] - minimo

            #binarizacao
            if d_min < d_max:
                aux[i][j] = 255
            else:
                aux[i][j] = 0

    return aux

retina = cv2.imread("retina.pgm", 0)
retina = contraste(retina, 3)
cv2.imwrite("retinaContraste.png", retina)

fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = contraste(fiducial, 3)
cv2.imwrite("fiducial.png", fiducial)