class Grafo:
    def __init__(self, id):
        self.id = id
        self.n = 0
        self.nAmarelo = 0
        self.nVerde = 0
        self.nVermelho = 0
        self.prox = None
        self.visitado = 0
        
class No:
    def __init__(self, id, cor):
        self.id = id
        self.cor = cor
        self.prox = None
        
def criaGrafo(n):
    grafo = [0] * n
    for i in range(n):
        grafo[i] = Grafo(i)
    return grafo
    
def addAresta(grafo, u, v, cor):
        aux = No(v, cor)
        head = grafo[u]
        while grafo[u].prox != None:
            grafo[u] = grafo[u].prox
        grafo[u].prox = aux
        grafo[u] = head
        grafo[u].n += 1
        if cor == 0:
            grafo[u].nVerde += 1
        elif cor == 1:
            grafo[u].nAmarelo += 1
        else:
            grafo[u].nVermelho += 1
            
def dfs(grafo, s, lista):
    grafo[s].visitado = 1
    head = grafo[s]
    while grafo[s].prox != None:
        i = grafo[s].prox.id
        if grafo[i].visitado == 0:
            dfs(grafo, i, lista)
        grafo[s] = grafo[s].prox
    grafo[s] = head
    lista.insert(0, grafo[s])

def busca(id, ordenacao):
    for i in range(len(ordenacao)):
        if ordenacao[i].id == id:
            return i

def tNaOrd(grafo, s):
    for i in range(len(grafo)):
        head = grafo[i]
        grafo[i]= grafo[i].prox
        while grafo[i] != None:
            if grafo[i].id == s:
                grafo[i] = head
                return True
            grafo[i] = grafo[i].prox
        grafo[i] = head
    return False

def caminhos(ordenacao, s, t):
    for i in range(len(ordenacao) - 1, -1, -1):
        if ordenacao[i].id == t:
            ordenacao = ordenacao[0: i + 1]
            break
    for i in range(len(ordenacao)):
        if ordenacao[i].id == s:
            ordenacao = ordenacao[i:]
            break
        
    verde = [0] * len(ordenacao)
    amarelo = [0] * len(ordenacao)
    vermelho = [0] * len(ordenacao)
    verde[0] = 1
    
    ordenacao = ordenacao[::-1]
    copia = ordenacao.copy()
    
    for i in range(1, len(ordenacao)):
        head = ordenacao[i]
        ordenacao[i] = ordenacao[i].prox
        while ordenacao[i] != None:
            j = busca(ordenacao[i].id, copia)
            if j != None:
                if ordenacao[i].cor == 0:
                    verde[i] += verde[j] + amarelo[j] + vermelho[j]
                elif ordenacao[i].cor == 1:
                    amarelo[i] += verde[j] + amarelo[j]
                else:
                    vermelho[i] += verde[j]
            ordenacao[i] = ordenacao[i].prox
        ordenacao[i] = head
    k = len(ordenacao) - 1
    soma = vermelho[k] + verde[k] + amarelo[k]
    return soma

n, m, s, t = map(int, input().split())
grafo = criaGrafo(n)
for _ in range(m):
    u, v, cor = map(int, input().split())
    addAresta(grafo, u, v, cor)
ordenacao = []
dfs(grafo, 0, ordenacao)
if not tNaOrd(ordenacao, t):
    print(0)
else:
    print(caminhos(ordenacao, s, t))