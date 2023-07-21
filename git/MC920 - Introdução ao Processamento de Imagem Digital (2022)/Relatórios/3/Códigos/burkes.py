import numpy as np
import cv2

def burkes(img, nc):
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
                arr[i, j + 1] += erro * (8/32)
            if (j+2) <= len(arr[i]) - 1:
                arr[i, j + 2] += erro * (4/32)

            if (i+1) <= len(arr) - 1:
                if (j-2) >= 0:
                    arr[i + 1, j - 2] += erro * (2/32)
                if (j-1) >= 0:
                    arr[i + 1, j - 1] += erro * (4/32)
                arr[i + 1, j] += erro *(8/32)
                if (j+1) <= len(arr[i]) - 1:
                    arr[i + 1, j + 1] += erro * (4/32)
                if (j+2) <= len(arr[i]) - 1:
                    arr[i + 1, j + 2] += erro * (2/32)

        if i % 2 != 0:
            aux = arr[i]
            aux = aux[::-1]
            arr[i] = aux

    res = np.array(arr * 255, dtype=np.uint8)
    return res


# RGB
monalisa = cv2.imread("monalisa.png")
monalisa = burkes(monalisa, 2)
cv2.imwrite("monalisaburkes.png", monalisa)

baboon = cv2.imread("baboon.png")
baboon = burkes(baboon, 2)
cv2.imwrite("baboonburkes.png", baboon)

peppers = cv2.imread("peppers.png")
peppers = burkes(peppers, 2)
cv2.imwrite("peppersBurkes.png", peppers)

# Monocromático
baboon = cv2.imread("baboon.png", 0)
baboon = burkes(baboon, 2)
cv2.imwrite("baboonburkesBlack.png", baboon)

monalisa = cv2.imread("monalisa.png", 0)
monalisa = burkes(monalisa, 2)
cv2.imwrite("monalisaburkesBlack.png", monalisa)

peppers = cv2.imread("peppers.png", 0)
peppers = burkes(peppers, 2)
cv2.imwrite("peppersBurkesBlack.png", peppers)
