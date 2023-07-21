import time

class No:
    def __init__(self, prox, id, cor, visitado):
        self.id = id
        self.prox = prox
        self.cor = cor
        self.visitado = visitado
        self.redundancia = None
    
    def add(self, id, cor, visitado):
        aux = No(None, id, cor, visitado)
        self.prox = aux
        return self.prox, self.prox
    
def totalmenteVisitado(grafo):
    # Verifica se todos as arestas do grafo já foram visitadas
    for i in range(len(grafo)):
        head = grafo[i]
        grafo[i] = grafo[i].prox
        while grafo[i] != None:
            if grafo[i].visitado == 0:
                grafo[i] = head
                grafo[i].visitado = 0
                return False
            grafo[i] = grafo[i].prox
        grafo[i] = head
        grafo[i].visitado = 1
    return True

def verificaParidade(grafo):
    # Retorna 1 se todos vértices possuírem grau par
    # Retorna 0 caso contrário
    for i in range(len(grafo)):
        head = grafo[i]
        grafo[i] = grafo[i].prox
        count0 = 0
        count1 = 0
        while grafo[i] != None:
            if grafo[i].cor == 0:
                count0 += 1
            else:
                count1 += 1
            grafo[i] = grafo[i].prox
        grafo[i] = head
        if (count0 + count1) % 2 != 0 or count0 != count1:
            return 0
    return 1

def trilhaMaximal(r, grafo, corAtual):
    trilha = [grafo[r]]
    while grafo[r] != None:
        if grafo[r].cor == None:
            head = grafo[r]
            grafo[r] = grafo[r].prox
        if grafo[r].visitado == 0 and grafo[r].cor != corAtual:
            corAtual = grafo[r].cor
            grafo[r].visitado = 1
            grafo[r].redundancia.visitado = 1
            trilha = trilha + [grafo[r]]
            aux = r
            r = grafo[r].id
            grafo[aux] = head
        else:
            grafo[r] = grafo[r].prox
    grafo[r] = head
    return trilha
            
def escolheVertice(grafo, trilha):
    i = 1
    while i < len(trilha):
        while grafo[trilha[i].id].visitado == 1:
            i += 1
        head = grafo[trilha[i].id]
        grafo[trilha[i].id] = grafo[trilha[i].id].prox
        while grafo[trilha[i].id] != None:
            if grafo[trilha[i].id].visitado == 0 and grafo[trilha[i].id].cor != trilha[i].cor:
                grafo[trilha[i].id] = head
                return trilha[i].id, i
            grafo[trilha[i].id] = grafo[trilha[i].id].prox
        grafo[trilha[i].id] = head
        i += 1
                
n, m = map(int, input().split(' '))
grafo = [0] * n
aux = [0] * n

for i in range(n):
    grafo[i] = No(None, i, None, None)
    aux[i] = grafo[i]
    
for i in range(m):
    adj = [int(i) for i in input().split(' ')]
    grafo[adj[0]], noA = grafo[adj[0]].add(adj[1], adj[2], 0)
    grafo[adj[1]], noB = grafo[adj[1]].add(adj[0], adj[2], 0)
    
    noA.redundancia = noB
    noB.redundancia = noA

for i in range(n):
    grafo[i] = aux[i]
    
tempo_inicial = (time.time())
if verificaParidade(grafo) == 0:
    print("Não possui trilha Euleriana alternante")
else:
    T = trilhaMaximal(0, grafo, None)
    while totalmenteVisitado(grafo) == False:
        s, i = escolheVertice(grafo, T)
        Taux = trilhaMaximal(s, grafo, T[i].cor)
        rTs = T[:i]
        sWr = T[i:]
        T = rTs + Taux[:len(Taux) - 1] + sWr
    
    for i in range(len(T)):
        T[i] = str(T[i].id)
    print(" ".join(T))

tempo_final = (time.time())

print((tempo_final - tempo_inicial), 'segundos')