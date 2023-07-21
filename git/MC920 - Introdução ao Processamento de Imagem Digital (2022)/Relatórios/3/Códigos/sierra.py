import numpy as np
import cv2

def sierra(img, nc):
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
                arr[i, j + 1] += erro * (5/32)
            if (j+2) <= len(arr[i]) - 1:
                arr[i, j + 2] += erro * (3/32)

            if (i+1) <= len(arr) - 1:
                if (j-2) >= 0:
                    arr[i + 1, j - 2] += erro * (2/32)
                if (j-1) >= 0:
                    arr[i + 1, j - 1] += erro * (4/32)
                arr[i + 1, j] += erro * (5/32)
                if (j+1) <= len(arr[i]) - 1:
                    arr[i + 1, j + 1] += erro * (4/32)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 1, j + 2] += erro * (2/32)
            
            if(i+2) <= len(arr) - 1:
                if (j-1) >= 0:
                    arr[i + 2, j - 1] += erro * (2/32)
                arr[i + 2, j] += erro * (3/32)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 2, j + 2] += erro * (2/32)

                

        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux

    res = np.array(arr * 255, dtype=np.uint8)
    return res


# RGB
monalisa = cv2.imread("monalisa.png")
monalisa = sierra(monalisa, 2)
cv2.imwrite("monalisasierra.png", monalisa)

baboon = cv2.imread("baboon.png")
baboon = sierra(baboon, 2)
cv2.imwrite("baboonsierra.png", baboon)

peppers = cv2.imread("peppers.png")
peppers = sierra(peppers, 2)
cv2.imwrite("peppersSierra.png", peppers)

# Monocromático
baboon = cv2.imread("baboon.png", 0)
baboon = sierra(baboon, 2)
cv2.imwrite("baboonsierraBlack.png", baboon)

monalisa = cv2.imread("monalisa.png", 0)
monalisa = sierra(monalisa, 2)
cv2.imwrite("monalisasierraBlack.png", monalisa)

peppers = cv2.imread("peppers.png", 0)
peppers = sierra(peppers, 2)
cv2.imwrite("peppersSierraBlack.png", peppers)