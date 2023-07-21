#######################################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 26/07/2020
## Descrição: Este programa simula o funcionamento do game “Onde está Carmen Sandiego?”
## de maneira recursiva.
########################################################################################

def search_r(dic, destino, i, carmem):  # recursiva

    """ Função recursiva que recebe um dicionário, o destino inicial, um índice (inicialmente 0)
    e uma lista de comparação, carmem. Se o primeiro país da lista de candidatos for o país a ser investigado,
    inicia-se a investigação, contagem de pistas e etc. Caso contrário, a função chama a si mesma com índice i+1
    até que o país seja encontrado. Em meio a investigação, quando descobre-se o próximo país a ser investigado,
    a função chama a si mesma com o índice no qual se encontra o próximo país na lista candidatos_cópia,
    até que Carmen seja encontrada."""

    candidatos = list(dic.keys())
    candidatos.sort()
    candidatos_copia = list(dic.keys())
    candidatos_copia.sort()
    if destino == candidatos[i]:
        contagem = 0
        texto = ''
        country = dic[destino]
        teste = ''.join(country)
        teste = list(teste)
        teste.sort()

        for i in range(len(country)):
            if (len(candidatos) == 1 and teste != carmem) or len(candidatos) == 0:
                break
            contagem += 1
            texto += country[i]
            letras = list(texto)
            for j in reversed(range(len(candidatos))):
                paises = list(candidatos[j])
                for k in range(len(letras)):
                    if paises.count(letras[k]) < texto.count(letras[k]):
                        del(candidatos[j])
                        break
            if contagem == 3:
                for j in reversed(range(len(candidatos))):
                    tamanho = list(candidatos[j])
                    if len(tamanho) > len(teste):
                        del (candidatos[j])

        if len(candidatos) == 1:
            print("Descobri com", contagem, "pistas que devo viajar para", candidatos[0])
            destino = candidatos[0]
            search_r(dic, destino, candidatos_copia.index(destino), carmem)
        elif len(candidatos) == 0:
            print("Descobri com", contagem, "pistas que Carmen Sandiego está no país")

    else:
        search_r(dic, destino, i+1, carmem)


def search(i, dic, destino, carmem):  # casca da função recursiva
    return search_r(dic, destino, i, carmem)

#  entradas
destino = input()
print("Iniciando as buscas em", destino)
carmem = ['a', 'c', 'e', 'm', 'n', 'r']

#  criando dicionário com as entradas
dic = {}
passe = 0
while passe == 0:
    pais = input().split(":")
    if pais[0] == "X":
        passe = 1
    else:
        dic[pais[0]] = pais[1].split(",")

search(0, dic, destino, carmem) # chamando a casca

