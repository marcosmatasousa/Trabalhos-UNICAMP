import numpy as np
import cv2

#padding
def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

# aux guarda o limiar de cada pixel
def phansalskar(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    k = 0.25
    R = 0.5
    p = 2
    q = 10
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            media = np.average(vizinhos)
            desvio = (np.std(vizinhos))
            aux[i][j] = media * (1 + p * np.exp(-q * media) + k * ((desvio / R) - 1))
    # binarizacao
    img = np.where(img > aux, 0, 255)
    return img

retina = cv2.imread("retina.pgm", 0)
retina = phansalskar(retina, 1)
cv2.imwrite("retinaPhansalskar.png", retina)
fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = phansalskar(fiducial, 1)
cv2.imwrite("fiducialPhansalskar.png", fiducial)