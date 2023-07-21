import numpy as np
import cv2

#padding
def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

#aux guarda o limiar de cada pixel
def mediana(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            aux[i][j] = np.median(vizinhos)
    # binarizacao
    img = np.where(img > aux, 0, 255)
    return img

retina = cv2.imread("retina.pgm", 0)
retina = mediana(retina, 10)
cv2.imwrite("retinaMediana.png", retina)

fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = mediana(fiducial, 10)
cv2.imwrite("fiducialMediana.png", fiducial)