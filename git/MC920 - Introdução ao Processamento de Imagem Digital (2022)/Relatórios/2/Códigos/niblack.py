import numpy as np
import cv2

def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

def niblack(img, n, k):
    aux = addBordas(img, n)
    img = aux.copy()
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            aux[i][j] = np.average(vizinhos) + k * np.std(vizinhos)
    
    img = np.where(img > aux, 0, 255)
    return img

retina = cv2.imread("retina.pgm", 0)
retina = niblack(retina, 20, 1)
fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = niblack(fiducial, 2, 1)
cv2.imwrite("retinaNiblack.png", retina)
cv2.imwrite("fiducialNiblack.png", fiducial)