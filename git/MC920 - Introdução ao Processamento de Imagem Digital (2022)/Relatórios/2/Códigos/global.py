import numpy as np
import matplotlib.pyplot as plt
import cv2

def histograma(img):
    aux = img.copy() / 255
    plt.hist(aux)

retina = cv2.imread("retina.pgm", 0)
histograma(retina)
retina = np.where(retina > 128, 0, 255) # binarizacao
cv2.imwrite("retinaGlobal.png", retina)
fiducial = cv2.imread("fiducial.pgm", 0)
histograma(fiducial)
fiducial = np.where(fiducial > 128, 0, 255)
cv2.imwrite("fiducialGlobal.png", fiducial)



