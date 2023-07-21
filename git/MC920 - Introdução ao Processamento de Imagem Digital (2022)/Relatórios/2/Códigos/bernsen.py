import numpy as np
import cv2
import matplotlib.pyplot as plt

def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

def histograma(img):
    aux = img.copy() / 255
    plt.hist(aux)
    

def bernsen(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            aux[i][j] = (np.min(vizinhos) / 2 + np.max(vizinhos) / 2) 
    img = np.where(img > aux, 0, 255)
    return img


retina = cv2.imread("retina.pgm", 0)
retina = bernsen(retina, 3)
cv2.imwrite("retinaBernsen.png", retina)

fiducial = cv2.imread("fiducial.pgm", 0)
fiducial = bernsen(fiducial, 3)
cv2.imwrite("fiducialBernsen.png", fiducial)
