import cv2
import numpy as np

# Captura do vídeo
capture = cv2.VideoCapture("Woodpecker.mp4")

# extraindo o frame atual e o anterior
ret, frame1 = capture.read()
ret, frame2 = capture.read()

while ret == True:
    cv2.imwrite("FrameAtual.png", frame2)
    cv2.imwrite("FrameAnterior.png", frame1)

    # extraindo a diferença entre frames e convertendo em níveis de cinza
    diferenca = cv2.absdiff(frame1, frame2)
    dif_cinza = cv2.cvtColor(diferenca, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Diferenca_gray", dif_cinza)
    cv2.imwrite("Diferenca_gray.png", dif_cinza)

    # aplicando filtro gaussiano
    filtrada = cv2.GaussianBlur(dif_cinza, (5, 5), 0)

    # aplicando um threshold com limiar igual a 25
    _, limiar = cv2.threshold(filtrada, 25, 255, cv2.THRESH_BINARY)

    # dilatacao
    dilatada = cv2.dilate(limiar, None, iterations=3)

    #cv2.imshow("Dilatacao", dilatada)
    cv2.imwrite("DilatadaTresholdFiltro.png", dilatada)

    # Contornos
    contornos, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Posicionando retângulos em objetos com área > 1000
    aux = np.full((720, 1280), 255).astype(dtype='uint8')
    if len(contornos) > 0:
        for i in range(len(contornos)):
            area = cv2.contourArea(contornos[i])
            if area > 1000:
                x,y,w,h = cv2.boundingRect(contornos[i])
                cv2.rectangle(aux,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.drawContours(aux, contornos, -1, (0,255,0), 1)
    cv2.imwrite("Resultado.png", aux)

    ret, frame1 = capture.read()
    ret, frame2 = capture.read()