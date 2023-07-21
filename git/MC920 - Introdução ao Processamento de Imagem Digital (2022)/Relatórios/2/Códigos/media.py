import numpy as np
import cv2

#padding
def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

#aux guarda o valor de cada limiar
def media(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            aux[i][j] = np.average(vizinhos)
    
    img = np.where(img > aux, 0, 255)
    return img

retina = cv2.imread("retina.pgm", 0)
retina = media(retina, 20)
cv2.imwrite("retinaMedia.png", retina)

fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = media(fiducial, 20)
cv2.imwrite("fiducialMedia.png", fiducial)