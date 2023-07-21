from operator import concat
import numpy as np
from scipy import signal
import imageio as im
import matplotlib.pyplot as plt
from skimage.io import imread
import cv2

def addBordas(img, n):
    res = cv2.copyMakeBorder(img.copy(), n, n, n, n, 
    cv2.BORDER_CONSTANT, 0)
    return res

def sauvola(img, n):
    aux = addBordas(img, n)
    img = aux.copy()
    k = 0.5
    R = 128
    for i in range(n, len(img) - n):
        for j in range(n, len(img[i]) - n):
            vizinhos = img[i - n: i + n + 1, j - n: j + n + 1]
            media = np.average(vizinhos)
            desvio = np.std(vizinhos)
            aux[i][j] = media * (1 + k * ((desvio / R) - 1))
    
    img = np.where(img > aux, 0, 255)
    return img

retina = cv2.imread("retina.pgm", 0)
retina = sauvola(retina, 10)
fiducial = cv2.imread("fiducial.pgm", 0)
cv2.imwrite("fiducial.png", fiducial)
fiducial = sauvola(fiducial, 10)
cv2.imwrite("retinaSauvola.png", retina)
cv2.imwrite("fiducialSauvola.png", fiducial)