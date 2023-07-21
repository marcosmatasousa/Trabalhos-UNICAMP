# MARCOS DA MATA SOUSA, RA 221519
# MC558A 2S2023 TAREFA PRATICA 1

class No:
    def __init__(self, id, g, lista):
        self.id = id
        self.g = g
        self.lista = lista
        
def get_g(no):
    return no.g

def get_id(no):
    return no.id

def testePossibilidade(lista):
    # Se a soma de graus for impar ou algum vértice possuir
    # grau maior que a quantidade de vértices menos 1, então
    # é impossível haver sequência gráfica. (Não são condições suficientes, no entanto)
    soma = sum(lista)
    if soma % 2 != 0:
        return 0
    for i in range(len(lista)):
        if len(lista) - 1 < lista[i]:
            return 0
    return 1

def montaRes(D):
    res = []
    for i in range(len(D)):
        if D[i].g != 0:
            print("Não é sequência gráfica!")
            return None
        else:
            res.append(sorted(D[i].lista)) 
    return res

def imprimeRes(res):
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = str(res[i][j])
        print(" ".join(res[i]))
              
n = int(input())
D = [int(i) for i in input().split(" ")]
if testePossibilidade(D) == 0:
    print("Não é sequência gráfica!")
else:
    for i in range(n):
        aux = D[i]
        D[i] = No(i + 1, aux, [])
        
    i = 0
    k = 0
    while k < n:
        for j in range(i + 1, D[i].g + 1):
            D[i].g -= 1
            D[i].lista.append(D[j].id)
            D[j].g -= 1
            D[j].lista.append(D[i].id)
            j += 1
        D.sort(key=get_g, reverse=True)
        k += 1
    D.sort(key=get_id)
    res = montaRes(D)
    if res != None:
        imprimeRes(res)