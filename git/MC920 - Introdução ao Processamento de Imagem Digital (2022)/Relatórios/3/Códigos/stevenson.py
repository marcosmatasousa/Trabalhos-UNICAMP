import numpy as np
import cv2

def stevenson(img, nc):
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

            if (j + 2) <= len(arr[i]) - 1:
                arr[i, j + 2] += erro * (32/200)
            
            if (i + 1) <= len(arr) - 1:
                if j-3 >= 0:
                    arr[i + 1, j - 3] += erro * (12/200)
                if j-1 >= 0:
                    arr[i + 1, j - 1] += erro * (26/200)
                if j+1 <= len(arr[i]) - 1:
                    arr[i + 1, j + 1] += erro * (30/200)
                if j+3 <= len(arr[i]) - 1:
                    arr[i + 1, j + 3] += erro * (16/200)
            
            if (i+2) <= len(arr) - 1:
                if (j-2) >= 0:
                    arr[i + 2, j - 2] += erro * (12/200)
                arr[i + 2, j] += erro * (26/200)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 2, j + 2] += erro * (12/200)
            
            if (i+3) <= len(arr) - 1:
                if (j-3) >= 0:
                    arr[i + 3, j - 3] += erro * (5/200)
                if (j-1) >= 0:
                    arr[i + 3, j - 1] += erro * (12/200)
                if (j+1) <= len(arr[i]) - 1:
                    arr[i + 3, j + 1] += erro * (12/200)
                if (j+3) <= len(arr[i]) - 1:
                    arr[i + 3, j + 3] += erro * (5/200)

        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux

    res = np.array(arr * 255, dtype=np.uint8)
    return res


# RGB
monalisa = cv2.imread("monalisa.png")
monalisa = stevenson(monalisa, 2)
cv2.imwrite("monalisastevenson.png", monalisa)

baboon = cv2.imread("baboon.png")
baboon = stevenson(baboon, 2)
cv2.imwrite("baboonstevenson.png", baboon)

peppers = cv2.imread("peppers.png")
peppers = stevenson(peppers, 2)
cv2.imwrite("peppersStevenson.png", peppers)

# Monocromático
baboon = cv2.imread("baboon.png", 0)
baboon = stevenson(baboon, 2)
cv2.imwrite("baboonstevensonBlack.png", baboon)

monalisa = cv2.imread("monalisa.png", 0)
monalisa = stevenson(monalisa, 2)
cv2.imwrite("monalisastevensonBlack.png", monalisa)

peppers = cv2.imread("peppers.png", 0)
peppers = stevenson(peppers, 2)
cv2.imwrite("peppersStevensonBlack.png", peppers)
