class No:
    def __init__(self, head, id, peso):
        self.peso = peso
        self.pai = None
        self.rank = None

def makeset(x):
    x.pai = x
    x.rank = 0

def findset(x):
    if x != x.pai:
        x.pai = findset(x.pai)
    return x.pai

def link(x, y):
    if x.rank > y.rank:
        y.pai = x
    else:
        x.pai = y
    if x.rank == y.rank:
        y.rank = y.rank + 1

def union(x, y):
    link(findset(x), findset(y))
    
def kruskal(grafo, k, n):
    A = []
    for i in range(len(grafo)):
        makeset(grafo[i])
    arestas.sort()
    for i in range(len(arestas)):
        id1 = arestas[i][1]
        id2 = arestas[i][2]
        if findset(grafo[id1]) != findset(grafo[id2]):
            A += [arestas[i]]
            union(grafo[id1], grafo[id2])
            n -= 1
            if n == k:
                break
    return A

n, m, k = map(int, input().split(" "))
grafo = []

for i in range(n):
    grafo.append(No(True, i, None))

arestas = []
for i in range(m):
    a, b, w = map(int, input().split(" "))
    arestas.append((w, a, b))

res = kruskal(grafo, k, n)
soma = 0
for i in range(len(res)):
    soma += res[i][0]
print(soma,end='\n')

