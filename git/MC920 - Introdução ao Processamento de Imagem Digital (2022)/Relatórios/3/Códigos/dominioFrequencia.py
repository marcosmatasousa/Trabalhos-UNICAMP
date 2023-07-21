from skimage.draw import disk
import numpy as np
import cv2
import numpy.fft as fft
import matplotlib.pyplot as plt

def circulo(img, raio):
    centro = (len(img) // 2, len(img[1]) // 2)
    rr, cc = disk(centro, raio)
    return rr, cc

def espectro(img):
    transformada = fft.fft2(img.copy())
    shift = fft.fftshift(transformada)
    res_espec = 20 * np.log(np.abs(shift))
    return res_espec, shift

def inversa(img):
    inv = fft.ifftshift(img)
    res = fft.ifft2(inv)
    res = np.abs(res)
    return res

def passabaixa(img):
    black = np.zeros((len(img[0]), len(img)), dtype=np.complex128)
    espec_img, shift = espectro(img)
    a, b = circulo(img, 60)
    black[a, b] = shift[a, b]
    black= inversa(black)
    return black

def passaalta(img):
    espec_img, shift = espectro(img)
    a, b = circulo(img, 60)
    shift[a, b] = 0
    shift = inversa(shift)
    return shift

def passafaixa(img):
    black = np.zeros((len(img[0]), len(img)), dtype=np.complex128)
    espec_img, shift = espectro(img)
    a, b = circulo(img, 60)
    black[a, b] = shift[a, b]
    x, y = circulo(img, 20)
    black[x, y] = 0
    black = inversa(black)
    return black

def rejeitafaixa(img):
    espec_img, shift = espectro(img)
    shift_rejeita = shift.copy()
    a, b = circulo(img, 60)
    shift_rejeita[a, b] = 0
    x, y = circulo(img, 20)
    shift_rejeita[x, y] = shift[x, y]
    shift_rejeita = inversa(shift_rejeita)
    return shift_rejeita

def compressao(img):
    espec_img, shift = espectro(img)
    shift = np.where(shift < 20000, 0, shift)
    shift = inversa(shift)
    return shift


# leitura da imagem e transformada de fourier (BABOON)
baboon = cv2.imread("baboon.png", 0)
plt.hist(baboon)
espec_baboon, shift = espectro(baboon)
cv2.imwrite("espectro_baboon.png", espec_baboon)
peppers = cv2.imread("peppers.png", 0)
plt.hist(peppers)
espec_peppers, shift = espectro(peppers)
cv2.imwrite("espectro_peppers.png", espec_peppers)


# passa-baixa
cv2.imwrite("baboon_pbaixa.png", passabaixa(baboon.copy()))
cv2.imwrite("peppers_pbaixa.png", passabaixa(peppers.copy()))

# passa-alta
cv2.imwrite("baboon_palta.png", passaalta(baboon.copy()))
cv2.imwrite("peppers_palta.png", passaalta(peppers.copy()))

# passa-faixa
cv2.imwrite("baboon_pfaixa.png", passafaixa(baboon.copy()))
cv2.imwrite("peppers_pfaixa.png", passafaixa(peppers.copy()))

# rejeita-faixa
cv2.imwrite("baboon_rfaixa.png", rejeitafaixa(baboon.copy()))
cv2.imwrite("peppers_rfaixa.png", rejeitafaixa(peppers.copy()))

# compressao
baboon_compress = compressao(baboon.copy())
cv2.imwrite("baboon_compress.png", baboon_compress)
baboon = np.array(baboon_compress, dtype=np.uint8)
plt.hist(baboon)

peppers_compress = compressao(peppers.copy())
cv2.imwrite("peppers_compress.png", peppers_compress)
peppers = np.array(peppers_compress, dtype=np.uint8)
plt.hist(peppers)













print('pare')
