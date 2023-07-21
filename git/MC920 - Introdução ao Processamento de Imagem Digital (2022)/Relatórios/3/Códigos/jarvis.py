import numpy as np
import cv2

def jarvis(img, nc):
    arr = np.array(img, dtype=float) / 255

    for i in range(len(arr)):
        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux
        for j in range(len(arr[i])):
            antigo = arr[i][j].copy()
            novo = np.round(antigo * (nc - 1)) / (nc - 1)
            arr[i][j] = novo
            erro = antigo - novo

            if (j+1) <= len(arr[i]) - 1:
                arr[i, j + 1] += erro * (7/48)
            if (j+2) <= len(arr[i]) - 1:
                arr[i, j + 2] += erro * (5/48)

            if (i+1) <= len(arr) - 1:
                if (j-2) >= 0:
                    arr[i + 1, j - 2] += erro * (3/48)
                if (j-1) >= 0:
                    arr[i + 1, j - 1] += erro * (5/48)
                arr[i + 1, j] += erro * (7/48)
                if (j+1) <= len(arr[i]) - 1:
                    arr[i + 1, j + 1] += erro * (5/48)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 1, j + 2] += erro * (3/48)
            
            if(i+2) <= len(arr) - 1:
                if (j-2) >= 0:
                    arr[i + 2, j - 2] += erro * (1/48)
                if (j-1) >= 0:
                    arr[i + 2, j - 1] += erro * (3/48)
                arr[i + 2, j] += erro * (5/48)
                if (j+1) <= len(arr[i]) - 1:
                    arr[i + 2, j + 1] += erro * (3/48)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 2, j + 2] += erro * (1/48)

                

        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux

    res = np.array(arr * 255, dtype=np.uint8)
    return res


# RGB
monalisa = cv2.imread("monalisa.png")
monalisa = jarvis(monalisa, 2)
cv2.imwrite("monalisaJarvis.png", monalisa)

baboon = cv2.imread("baboon.png")
baboon = jarvis(baboon, 2)
cv2.imwrite("baboonJarvis.png", baboon)

peppers = cv2.imread("peppers.png")
peppers = jarvis(peppers, 2)
cv2.imwrite("peppersJarvis.png", peppers)

# Monocromático
baboon = cv2.imread("baboon.png", 0)
baboon = jarvis(baboon, 2)
cv2.imwrite("baboonJarvisBlack.png", baboon)

monalisa = cv2.imread("monalisa.png", 0)
monalisa = jarvis(monalisa, 2)
cv2.imwrite("monalisaJarvisBlack.png", monalisa)

peppers = cv2.imread("peppers.png", 0)
peppers = jarvis(peppers, 2)
cv2.imwrite("peppersJarvisBlack.png", peppers)
