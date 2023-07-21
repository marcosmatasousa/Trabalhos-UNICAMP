######################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 06/06/2020
## Descrição: Este programa simula o funcionamento de um autômato celular, o Jogo da Vida
######################################################################


def criamatriz(n, m, padrao="."):
    matriz = []
    for i in range(n):
        linha = []
        for i in range(m):
            linha.append(padrao)
        matriz.append(linha)
    return (matriz)


def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j == len(m[i]) - 1:
                print(m[i][j])
            else:
                print(m[i][j], end="")


def verifica(matriz, copia):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            vizinhos = 0
            if i - 1 < 0 and j - 1 < 0:  # Análise de elementos na quina superior esquerda
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
            elif i + 1 >= len(matriz) and j - 1 < 0:  # Análise de elementos na quina inferior esquerda
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
            elif i - 1 < 0 and j + 1 >= len(matriz[i]):  # Análise de elementos na quina superior direita
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
            elif i + 1 >= len(matriz) and j + 1 >= len(matriz[i]):  # Análise de elementos na quina inferior direita
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
            elif i - 1 < 0 and j - 1 >= 0:  # Análise de elementos na borda superior
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
                if matriz[i + 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
            elif (i - 1) >= 0 and (j - 1) < 0:  # Análise de elementos na borda esquerda
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
            elif (i + 1) >= len(matriz) and (j - 1) >= 0:  # Análise de elementos na borda inferior
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
                if matriz[i - 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
            elif (i - 1) >= 0 and (j + 1) >= len(matriz[i]):  # Análise de elementos na borda direita
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
            elif i - 1 >= 0 and j - 1 >= 0:
                if matriz[i - 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i - 1][j] == "+":
                    vizinhos += 1
                if matriz[i - 1][j + 1] == "+":
                    vizinhos += 1
                if matriz[i][j - 1] == "+":
                    vizinhos += 1
                if matriz[i][j + 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j - 1] == "+":
                    vizinhos += 1
                if matriz[i + 1][j] == "+":
                    vizinhos += 1
                if matriz[i + 1][j + 1] == "+":
                    vizinhos += 1
            if matriz[i][j] == "+": # Casos para células vivas
                if vizinhos < 2:
                    copia[i][j] = "."
                elif vizinhos > 3:
                    copia[i][j] = "."
                elif vizinhos == 3 or vizinhos == 2:
                    copia[i][j] = matriz[i][j]
            elif matriz[i][j] == ".": # Casos para célular mortas
                if vizinhos == 3:
                    copia[i][j] = "+"
                else:
                    copia[i][j] = "."
    return copia

# Entradas
n = int(input())
m = int(input())
i = int(input())
qtd = int(input())

# Matrizes
matriz = criamatriz(n, m)
copia = criamatriz(n, m)

# Adicionando células vivas
for j in range(qtd):
    p = input().split(",")
    matriz[int(p[0])][int(p[1])] = "+"
imprime(matriz)
print("-")

# Verificações
z = 0
while z < i:
    matriz = verifica(matriz, copia)
    copia = criamatriz(n, m)
    imprime(matriz)
    print("-")
    z += 1
