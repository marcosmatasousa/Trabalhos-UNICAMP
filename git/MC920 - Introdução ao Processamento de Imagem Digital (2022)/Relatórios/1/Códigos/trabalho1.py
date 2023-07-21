# MARCOS DA MATA SOUSA - 221519 - TRABALHO 1

from scipy import signal
import numpy as np
import imageio as im
import matplotlib.pyplot as plt

def brilho(imagem, gama):
    res = imagem / 255
    res = np.power(res, (1/gama))
    res = res * 255
    return res

def extrairPlano(imagem, plano):
    return np.where(imagem & np.power(2, plano), 1, 0)

def combinacao(imagemA, imagemB, p1, p2):
    return (p1 * imagemA) + (p2 * imagemB)


# leitura de city
city = im.imread('city.png')

# 1.1.B
plt.imshow(city)
b = 255 - city
plt.imshow(b)
im.imsave('1.1negativo.png', b)

# 1.1.C
c = np.where(city > 200, 200, city)
c = np.where(c < 100, 100, c)
im.imsave('1.1intervalo100_200.png', c)
plt.imshow(c)

# 1.1.D
d = np.copy(city)
d[0::2, :] = d[0::2, ::-1]
im.imsave('1.1inversão_linhas_pares.png', d)
plt.imshow(d)

# 1.1.E
e = np.copy(city)
e[256:, 0:] = np.flipud(e[0:256, 0:])
im.imsave('1.1espelhamento_superior.png', e)
plt.imshow(e)

# 1.1.F
f = np.flipud(city)
im.imsave('1.1espelhamento_vertical.png', f)
plt.imshow(f)

###
# 1.2
# leitura do baboon
baboon = im.imread('baboon.png')
im.imsave('1.2gama1.5.png', brilho(baboon, 1.5))
im.imsave('1.2gama.2.5.png', brilho(baboon, 2.5))
im.imsave('1.2gama3.5.png', brilho(baboon, 3.5))

###
# 1.3
im.imsave('1.3plano0.png', extrairPlano(baboon, 0))
im.imsave('1.3plano4.png', extrairPlano(baboon, 4))
im.imsave('1.3plano7.png', extrairPlano(baboon, 7))

###
# 1.4
mosaico = np.empty((512, 512))

mosaico[0:128, 0:128] = baboon[128:256, 128:256]
mosaico[0:128, 128:256] = baboon[256:384, 256:384]
mosaico[0:128, 256:384] = baboon[384:512, 0:128]
mosaico[0:128, 384:512] = baboon[0:128, 256:384]

mosaico[128:256, 0:128] = baboon[128:256, 384:512]
mosaico[128:256, 128:256] = baboon[384:512, 384:512]
mosaico[128:256, 256:384] = baboon[0:128, 0:128]
mosaico[128:256, 384:512] = baboon[256:384, 0:128]

mosaico[256:384, 0:128] = baboon[256:384, 384:512]
mosaico[256:384, 128:256] = baboon[384:512, 128:256]
mosaico[256:384, 256:384] = baboon[0:128, 128:256]
mosaico[256:384, 384:512] = baboon[128:256, 256:384]

mosaico[384:512, 0:128] = baboon[0:128, 384:512]
mosaico[384:512, 128:256] = baboon[384:512, 256:384]
mosaico[384:512, 256:384] = baboon[256:384, 128:256]
mosaico[384:512, 384:512] = baboon[128:256, 0:128]

im.imsave('1.4_mosaico.png', mosaico)
plt.imshow(mosaico)
###
# 1.5
#leitura da butterfly
butterfly = im.imread('butterfly.png')
im.imsave('1.5Combinacao1.png', combinacao(baboon, butterfly, 0.2, 0.8))
im.imsave('1.5Combinacao2.png', combinacao(baboon, butterfly, 0.5, 0.5))
im.imsave('1.5Combinacao3.png', combinacao(baboon, butterfly, 0.8, 0.2))

###
# 1.6
h1 = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0],
[-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])

h2 = (1/256) * np.array([[1, 4, 6, 4, 1], 
[4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],
[1, 4, 6, 4, 1]])

h3 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

h4 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

h5 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

h6 = (1/9) * np.full((3,3), 1)

h7 = np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]])

h8 = np.array([[2, -1, -1], [2, -1, -1], [-1, -1, 2]])

h9 = np.identity(9)

h10 = (1/8) * np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1],
[-1, 2, 2, 2, -1], [-1, 2, 2, 2, -1], [-1, -1, -1, -1, -1]])

h11 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])

filtro = signal.convolve2d(butterfly, h1)
plt.imsave("h1.png", filtro)

filtro = signal.convolve2d(butterfly, h2)
plt.imsave("h2.png", filtro)

filtro = signal.convolve2d(butterfly, h3)
plt.imsave("h3.png", filtro)

filtro = signal.convolve2d(butterfly, h4)
plt.imsave("h4.png", filtro)

filtro = signal.convolve2d(butterfly, h5)
plt.imsave("h5.png", filtro)

filtro = signal.convolve2d(butterfly, h6)
plt.imsave("h6.png", filtro)

filtro = signal.convolve2d(butterfly, h7)
plt.imsave("h7.png", filtro)

filtro = signal.convolve2d(butterfly, h8)
plt.imsave("h8.png", filtro)

filtro = signal.convolve2d(butterfly, h9)
plt.imsave("h9.png", filtro)

filtro = signal.convolve2d(butterfly, h10)
plt.imsave("h10.png", filtro)

filtro = signal.convolve2d(butterfly, h11)
plt.imsave("h11.png", filtro)

soma = np.sqrt((np.power(h3, 2)) + (np.power(h4, 2)))
plt.imsave("h3+h4.png", soma)
