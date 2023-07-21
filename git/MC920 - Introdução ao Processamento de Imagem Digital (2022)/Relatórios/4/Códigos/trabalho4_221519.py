import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def contornos(img):
    # Convertendo para níveis de cinza e binarizando
    binaria = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binaria = np.where(binaria != 255, 0, 255)
    binaria = binaria.astype('uint8')

    # Desenhando contornos
    contours, _ = cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    aux = img.copy()
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    res = aux - img
    res = np.where(res == 0, 255, res)
    return res, binaria

def metricas(img, binaria):
    # O scikit detecta os objetos de cor branca
    binaria_inv = np.where(binaria == 255, 0, 255)
    
    # Formatação do texto de enumeração
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.25
    cor = (255, 255, 255)
    espessura = 1

    props = label(binaria_inv)
    properties = regionprops(props)

    p = 0
    m = 0
    g = 0
    # Extraindo medidas
    for i in range(len(properties)):
        area = properties[i].area
        perim = properties[i].perimeter
        solidez = properties[i].solidity
        excentricidade = properties[i].eccentricity
    
        if area < 1500:
            p += 1
        elif area >= 3000:
            g += 1
        else:
            m += 1
        print("região", str(i) + ": área:", area, "perímetro:", round(perim, 6), "solidez:", 
        round(solidez, 6), "excentricidade:", round(excentricidade, 6))
        
        # Identificação dos objetos por número
        coord = properties[i].centroid
        a = int(coord[1])
        b = int(coord[0])
        tupla = (a, b)
        cv2.putText(img, str(i), tupla, font, fontScale, cor, espessura, cv2.LINE_AA)

    print('')
    print("número de regiões pequenas:", p)
    print("número de regiões médias:", m)
    print("número de regiões grandes:", g)
    print('######')

    return p, m, g

def histograma(p, m, g):
    bins = 0
    if p > 0:
      bins += 1
    if m > 0:
        bins += 1
    if g > 0:
        bins += 1  

    list1 = [500] * p  
    list2 = [2000] * m  
    list3 = [4000] * g
    hist = list1 + list2 + list3
    
    plt.title("Área dos objetos")
    plt.xlabel("Área")
    plt.ylabel("Número de objetos")
    plt.hist(hist, bins)
    plt.close()

img1 = cv2.imread('objetos1.png')
res1, bin = contornos(img1.copy())
p, m, g = metricas(img1, bin)
histograma(p, m, g)
cv2.imwrite("binarizada1.png", bin)
cv2.imwrite("contorno1.png", res1)
cv2.imwrite("numerada1.png", img1)

img2 = cv2.imread('objetos3.png')
res2, bin = contornos(img2.copy())
p, m, g = metricas(img2, bin)
histograma(p, m, g)
cv2.imwrite("binarizada2.png", bin)
cv2.imwrite("contorno2.png", res2)
cv2.imwrite("numerada2.png", img2) 