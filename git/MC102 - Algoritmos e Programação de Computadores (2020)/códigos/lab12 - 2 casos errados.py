#######################################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 30/07/2020
## Descrição: Este programa simula o funcionamento Trapaça, um jogo de baralho no qual
## o objetivo é descartar todas as cartas da mão.
########################################################################################

#  entradas
mao_atual = input().split(" ")
pilha = input().split(" ")
alvo = input()
duvida = input()
jogada = []

#  trocando letras "problematicas" para facilitar a ordenação
if alvo == "K":
    alvo = "R"
if alvo == "A":
    alvo = "."
if alvo == "10":
    alvo = "I"
for i in range(len(mao_atual)):
    mao_atual[i] = mao_atual[i].replace("K", "R")
    mao_atual[i] = mao_atual[i].replace("A", ".")
    mao_atual[i] = mao_atual[i].replace("10", "I")

#  ordenação das cartas
for i in range(1, len(mao_atual)):
    aux = mao_atual[i]
    j = i
    while j > 0 and mao_atual[j - 1] > aux:
        mao_atual[j] = mao_atual[j - 1]
        j -= 1
    mao_atual[j] = aux
left = 0
right = len(mao_atual) - 1
while left <= right:
    m = (left + right) // 2
    if len(jogada) == 4:
        break
    if len(mao_atual) == 0:
        break
    if m == len(mao_atual):
        m = 0
    if mao_atual[m].count(alvo) > 0:
        jogada.append(mao_atual[m])
        del (mao_atual[m])
    else:
        if alvo < mao_atual[m]:
            right = m - 1
        else:
            left = m + 1

#  retornando às letras originais
if alvo == "R":
    alvo = "K"
if alvo == ".":
    alvo = "A"
if alvo == "I":
    alvo = "10"
for i in range(len(mao_atual)):
    mao_atual[i] = mao_atual[i].replace("R", "K")
    mao_atual[i] = mao_atual[i].replace("I", "10")
    mao_atual[i] = mao_atual[i].replace(".", "A")
for i in range(len(jogada)):
    jogada[i] = jogada[i].replace("R", "K")
    jogada[i] = jogada[i].replace("I", "10")
    jogada[i] = jogada[i].replace(".", "A")

# com blefe, sem duvida
if len(jogada) == 0 and duvida == "N":
    play = list(mao_atual[0])
    if play[0] + play[1] == "10":
        par = "10"
        for i in range(len(mao_atual)):
            if mao_atual[i].count(par) > 0:
                jogada.append(mao_atual[i])
        for i in range(len(jogada)):
            if mao_atual[i] in jogada:
                del (mao_atual[i])
    else:
        play = list(mao_atual[0])
        for i in range(len(mao_atual)):
            if mao_atual[i].count(play[0]) > 0:
                jogada.append(mao_atual[i])
        for i in range(len(jogada)):
            if mao_atual[i] in jogada:
                del (mao_atual[i])
    print("Jogada:", " ".join(jogada))
    print("Nenhum bot duvidou")
    print("Mão:", " ".join(mao_atual))
    for i in range(len(jogada)):
        pilha.append(jogada[i])
    if pilha[0] == "":
        del (pilha[0])
    print("Pilha:", " ".join(pilha))
    if len(mao_atual) == 0:
        print("O bot venceu o jogo")


# com blefe, com duvida
elif len(jogada) == 0 and duvida == "S":
    play = list(mao_atual[0])
    if play[0] + play[1] == "10":
        par = "10"
        for i in range(len(mao_atual)):
            if mao_atual[i].count(par) > 0:
                jogada.append(mao_atual[i])
    else:
        play = list(mao_atual[0])
        for i in range(len(mao_atual)):
            if mao_atual[i].count(play[0]) > 0:
                jogada.append(mao_atual[i])
    print("Jogada:", " ".join(jogada))
    print("Um bot adversário duvidou")
    print("O bot estava blefando")
    for i in range(len(pilha)):
        mao_atual.append(pilha[i])
    pilha = []
    for i in range(len(mao_atual)):
        mao_atual[i] = mao_atual[i].replace("K", "R")
        mao_atual[i] = mao_atual[i].replace("A", ".")
        mao_atual[i] = mao_atual[i].replace("10", "I")

    for i in range(1, len(mao_atual)):  # ordenação
        aux = mao_atual[i]
        j = i
        while j > 0 and mao_atual[j - 1] > aux:
            mao_atual[j] = mao_atual[j - 1]
            j -= 1
        mao_atual[j] = aux
    for i in range(len(mao_atual)):
        mao_atual[i] = mao_atual[i].replace("R", "K")
        mao_atual[i] = mao_atual[i].replace("I", "10")
        mao_atual[i] = mao_atual[i].replace(".", "A")

    print("Mão:", " ".join(mao_atual))
    print("Pilha:", " ".join(pilha))


# sem blefe, sem duvida
elif len(jogada) > 0 and duvida == "N":
    for i in range(1, len(jogada)):
        aux = jogada[i]
        j = i
        while j > 0 and jogada[j - 1] > aux:
            jogada[j] = jogada[j - 1]
            j -= 1
        jogada[j] = aux
    print("Jogada:", " ".join(jogada))
    print("Nenhum bot duvidou")
    for i in range(len(mao_atual)):
        if mao_atual[i] in jogada:
            del (mao_atual[i])
    for i in range(len(jogada)):
        pilha.append(jogada[i])
    print("Mão:", " ".join(mao_atual))
    if pilha[0] == "":
        del (pilha[0])
    print("Pilha:", " ".join(pilha))
    if len(mao_atual) == 0:
        print("O bot venceu o jogo")


# sem blefe, com duvida
elif len(jogada) > 0 and duvida == "S":
    for i in range(1, len(jogada)):
        aux = jogada[i]
        j = i
        while j > 0 and jogada[j - 1] > aux:
            jogada[j] = jogada[j - 1]
            j -= 1
        jogada[j] = aux
    print("Jogada:", " ".join(jogada))
    print("Um bot adversário duvidou")
    print("O bot não estava blefando")
    pilha = []
    print("Mão:", " ".join(mao_atual))
    print("Pilha:", " ".join(pilha))
    if len(mao_atual) == 0:
        print("O bot venceu o jogo")
