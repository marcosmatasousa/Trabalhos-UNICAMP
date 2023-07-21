#######################################################################################
## MC102 W - 2020 1S
## Aluno: MARCOS DA MATA SOUSA
## RA: 221519
## Data: 05/08/2020
## Descrição: Este programa simula, através de um relatório,
## o impacto de fake news dentro de uma rede de amigos,
########################################################################################


def relatorio(dic, gerador, compartilhador, retorno, i):
    """Função recursiva que recebe um dicionário, uma lista de geradores de fake news,
    uma lista de compartilhadores, uma lista na qual serão retornados os indivíduos que
    receberam a notícia e um índice (inicialmente 0)."""

    avaliando = list(dic.keys())
    if avaliando[i] in gerador or avaliando[i] in compartilhador:
        amigos = dic[avaliando[i]]
        for j in range(len(amigos)):
            retorno.append((amigos[j]))
        if avaliando[i] in compartilhador:
            if len(amigos) == 0:
                for k in reversed(range(len(compartilhador))):
                    if compartilhador[k] == avaliando[i]:
                        del(compartilhador[k])
        if i < len(avaliando) - 1:
            relatorio(dic, gerador, compartilhador, retorno, i + 1)
    elif i < len(avaliando) - 1:
        relatorio(dic, gerador, compartilhador, retorno, i + 1)


n = int(input())
dic = {}
compartilhador = []
gerador = []
retorno = []

#  Adicionando valores ao dicionário, as chaves são indivíduos,
#  os valores são listas de amigos
for i in range(n):
    lista = []
    acao = input().split(" ")
    if acao[0] == "0":
        for j in range(1, len(acao)):
            lista.append(acao[j])
        del(lista[0])
        dic[acao[1]] = lista
    elif acao[0] == "1":
        for j in range(1, len(acao)):
            lista.append(acao[j])
        del(lista[0])
        dic[acao[1]] = lista
        gerador.append(acao[1])
    elif acao[0] == "2":
        for j in range(1, len(acao)):
            lista.append(acao[j])
        del(lista[0])
        dic[acao[1]] = lista
        compartilhador.append(acao[1])

#  Chamando função recursiva
relatorio(dic, gerador, compartilhador, retorno, 0)

#  Relatório final e ordenação
relatorio_final = retorno + gerador + compartilhador
relatorio_final.sort()
if len(relatorio_final) > 1:
    for i in reversed(range(len(relatorio_final))):
        if relatorio_final[i] == relatorio_final[i - 1]:
            del(relatorio_final[i])

#  Impressão
print("Ordenação por nome")
for i in range(len(relatorio_final)):
    print(relatorio_final[i])
